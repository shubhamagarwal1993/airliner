"""
The communication module provides a Communication Service for sending commands
over UDP to the vehicle.

Services:
    Communication  Handles UDP interface with physical vehicle.
"""

import threading

import queue
import socketserver

from pyliner import pyliner_exceptions
from pyliner.action import ACTION_SEND_COMMAND, ACTION_SEND_BYTES, ACTION_TELEM, \
    ACTION_CONTROL_REQUEST, ACTION_CONTROL_GRANT, ACTION_CONTROL_REVOKE, \
    ACTION_CONTROL_RELEASE
from pyliner.arte_ccsds import CCSDS_TlmPkt_t, CCSDS_CmdPkt_t
from pyliner.intent import IntentFilter, Intent
from pyliner.pyliner_exceptions import PylinerError
from pyliner.python_pb import pyliner_msgs
from pyliner.app import App
from pyliner.util import init_socket, handler_factory, CallableDefaultDict

# TODO Python3 does not see telemetry
# TODO Put all this somewhere vehicle specific
from pyliner.util.periodic_executor import PeriodicExecutor

SEND_TIME = 0.1
DEFAULT_CI_PORT = 5008
DEFAULT_TO_PORT = 5011


class _Telemetry(object):
    def __init__(self, name=None, time=None, value=None):
        self.name = name
        self.time = time
        self.value = value

        self._listener = set()

    def add_listener(self, listener):
        if not callable(listener):
            raise TypeError('Listener must be callable.')
        self._listener.add(listener)

    def remove_listener(self, listener):
        self._listener.remove(listener)

    def update(self, value, time=None):
        self.time = time
        self.value = value
        for listener in self._listener:
            listener(self)


class ControlToken(object):
    def __init__(self, app_name):
        self.app_name = app_name
        # self._token =

    def request(self, data):
        return ControlRequest(self, data)


class ControlRequest(object):
    def __init__(self, token, data):
        self.token = token
        """:type: ControlToken"""
        self.data = data


class CommandAuthorizationError(PylinerError):
    """Raised if an App does not have permission to send commands."""
    pass


class Communication(App):
    """Provide methods to send and receive telemetry to a vehicle.

    In some ways this service acts more like a singleton that is guaranteed to
    be present on the vehicle, because there is only one link to the software
    bus, and if there is no link the user could not communicate. As much as
    possible, this service tries not to act like a God Object, but occasionally
    it happens.
    """

    def __init__(self, airliner_map, address='localhost',
                 ci_port=DEFAULT_CI_PORT, to_port=DEFAULT_TO_PORT):
        """
        Args:
            airliner_map (dict): Airliner Mapping, typically read from a JSON.
            address (str): Address to connect to the vehicle.
            ci_port (int): Command-Ingest port
            to_port (int): Telemetry-Output port
        """
        super(Communication, self).__init__()

        # Telemetry variables
        self.address = address
        self.airliner_map = airliner_map
        self.all_telemetry = []
        self.ci_port = ci_port
        self.ci_socket = init_socket()
        self.control_current = None
        """:type: ControlToken"""
        self.control_lock = threading.RLock()
        self.control_thread = None
        """:type: PeriodicExecutor"""
        self.control_waiting = queue.Queue()
        self.subscribers = []
        self.to_port = to_port

        self._telemetry = CallableDefaultDict(
            default_factory=lambda k: self.subscribe(k))
        """:type: dict[str, _Telemetry]"""

        # Receive Telemetry
        self.tlm_listener = socketserver.UDPServer(
            ("0.0.0.0", self.to_port), handler_factory(self._on_recv_telemetry))
        self.listener_thread = threading.Thread(
            target=self.tlm_listener.serve_forever)
        self.listener_thread.daemon = True
        self.listener_thread.start()

    def attach(self, vehicle):
        super(Communication, self).attach(vehicle)
        self.control_thread = PeriodicExecutor(
            self.control_rotate, every=0.5, name='ControlRotateThread')
        self.control_thread.start()

        def filter_control(data, call):
            if not isinstance(data, ControlRequest):
                raise TypeError(
                    'Sending data must be wrapped in a ControlRequest produced '
                    'from a valid ControlToken.')
            if data.token is not self.control_current:
                raise CommandAuthorizationError(
                    'App is not authorized to send commands.')
            else:
                return call(data.data)

        self.vehicle.add_filter(
            IntentFilter(actions=[ACTION_SEND_COMMAND]),
            lambda i: filter_control(i.data, self.send_command)
        )
        self.vehicle.add_filter(
            IntentFilter(actions=[ACTION_SEND_BYTES]),
            lambda i: filter_control(i.data, self.send_bytes)
        )
        self.vehicle.add_filter(
            IntentFilter(actions=[ACTION_TELEM]),
            lambda i: self.telemetry(i.data)
        )
        self.vehicle.add_filter(
            IntentFilter(actions=[ACTION_CONTROL_REQUEST]),
            self.control_request
        )
        self.vehicle.add_filter(
            IntentFilter(actions=[ACTION_CONTROL_RELEASE]),
            self.control_release
        )

    def detach(self):
        self.vehicle.clear_filter()
        self.control_thread.stop()
        super(Communication, self).detach()

    def control_grant(self, request):
        """Generate a ControlToken and pass it to the App which was granted
        control.
        """
        self.control_lock.acquire()
        self.debug('Grant Control: {}'.format(request))
        self.control_current = ControlToken(app_name=request)
        reply = self.vehicle.broadcast(Intent(
            action=ACTION_CONTROL_GRANT,
            component=request,
            data=self.control_current
        )).first(0.01).result
        if reply is not True:
            self.debug('{} refused control.')
            self.control_revoke()
            if not self.control_waiting.empty():
                self.control_grant(self.control_waiting.get())
        self.control_lock.release()

    def control_release(self, intent):
        """Called if an App willingly releases control."""
        self.control_lock.acquire()
        if self.control_current is None or intent.data != self.control_current:
            success = False
        else:
            success = True
            self.debug('Release Control: {}'.format(intent.data.app_name))
            if self.control_waiting.empty():
                self.control_current = None
            else:
                self.control_grant(self.control_waiting.get())
        self.control_lock.release()
        return success

    def control_request(self, intent):
        """Called when an App requests to be given control."""
        self.control_lock.acquire()
        if not self.control_current and self.control_waiting.empty():
            self.control_grant(intent.data)
        else:
            self.control_waiting.put(intent.data)
        self.control_lock.release()

    def control_revoke(self):
        self.vehicle.broadcast(Intent(
            action=ACTION_CONTROL_REVOKE,
            component=self.control_current.app_name
        ))

    def control_rotate(self):
        """If other Apps are waiting for control, rotate control.

        Put App which was rotated out back into queue.
        """
        self.control_lock.acquire()
        if self.control_current is not None \
                and not self.control_waiting.empty():
            self.debug('Rotate Out: {}'.format(self.control_current.app_name))
            self.control_revoke()
            self.control_waiting.put(self.control_current.app_name)
            self.control_grant(self.control_waiting.get())
        self.control_lock.release()

    @property
    def qualified_name(self):
        return 'com.windhover.pyliner.app.communication'

    def send_bytes(self, message):
        self.ci_socket.sendto(message, (self.address, self.ci_port))
        return True

    def send_command(self, telemetry):
        msg = self._serialize(telemetry)
        self.vehicle.debug(
            'Sending telemetry to airliner: %s', telemetry.to_json())
        return self.send_bytes(msg)

    def telemetry(self, args):
        if isinstance(args, str):
            return self._telemetry[args]
        elif isinstance(args, dict):
            return {k: self._telemetry[v] for k, v in args.items()}
        elif isinstance(args, list):
            return [self._telemetry[t] for t in args]
        else:
            raise TypeError('Can only parse str, dict, and list data.')

    def _get_airliner_op(self, op_path):
        """
        Receive a ops path and returns the dict for that op defined in
        the input file.

        Args:
            op_path (str): Operational path of command to retrieve. Leading "/"
                is required. "/Airliner/CNTL/ManualSetpoint"

        Returns:
            dict: Operational dictionary of requested path.

        Raises:
            KeyError: If any part of the Airliner map is invalid. Including if
                the requested path does not exist.
        """
        ops_names = op_path.split('/')[1:]

        def get_app(app_ops_name):
            for app in self.airliner_map[ops_names[0]]['apps'].values():
                if app['app_ops_name'] == app_ops_name:
                    return app
        return get_app(ops_names[1])['operations'][ops_names[2]]

    @staticmethod
    def _get_ccsds_msg(op):
        """Receive a ops dict and returns a ccsds msg

        Args:
            op (dict): Operational dictionary of an app operation.

        Returns:
            Union[CCSDS_TlmPkt_t, CCSDS_CmdPkt_t]: Ctypes packet structure
                based on the operational dictionary.
        """
        # If the command code is -1 this is telemetry
        if op["airliner_cc"] == -1:
            ret_msg = CCSDS_TlmPkt_t()
            ret_msg.clear_packet()
            ret_msg.init_packet()
            ret_msg.PriHdr.StreamId.bits.app_id = int(op["airliner_mid"], 0)
        else:
            ret_msg = CCSDS_CmdPkt_t()
            ret_msg.clear_packet()
            ret_msg.init_packet()
            ret_msg.PriHdr.StreamId.bits.app_id = int(op["airliner_mid"], 0)
            ret_msg.SecHdr.Command.bits.code = int(op["airliner_cc"])
        return ret_msg

    def _get_op_attr(self, op_path):
        """ Gets the operation path from airliner data for a specified attribute

        Args:
            op_path (str): Operation path as located in input file
                (E.g. "/Airliner/ES/Noop")

        Returns:
            True path to access this attribute in protobuf message
                (E.g. Payload.CmdCounter)
        """
        op = self._get_airliner_op(op_path)
        ops_names = op_path.split('/')[1:]
        for fsw, fsw_data in self.airliner_map.items():
            if fsw == ops_names[0]:
                for app, app_data in fsw_data["apps"].items():
                    if app_data["app_ops_name"] == ops_names[1]:
                        for op_name, op_data in app_data["proto_msgs"] \
                                [op["airliner_msg"]] \
                                ["operational_names"].items():
                            if op_name == ops_names[3]:
                                return op_data["field_path"]
        return None

    def _get_pb_decode_obj(self, raw_tlm, op_path):
        """ Generates protobuf object from raw telemetry

        Args:
            raw_tlm (str): Raw bytes received from socket
            op_path (str): Operation path as located in input file
                (E.g. "/Airliner/ES/Noop")

        Returns:
            Protobuf object for this specific message with set values
        """
        op = self._get_airliner_op(op_path)
        if not op:
            return None

        # Check if no args cmd
        if len(op["airliner_msg"]) == 0:
            return None

        # Call the correct protobuf constructor for this command
        pb_msg = self._proto_obj_factory(op["airliner_msg"])
        pb_msg.ParseFromString(raw_tlm)
        return pb_msg

    def _get_pb_encode_obj(self, json, op):
        """ Generates protobuf object from user script command

        Args:
            json (dict): User command specifying op and args
            op (dict): Operation dictionary

        Returns:
            Protobuf object for this specific message with set values
        """
        # Check if no args cmd
        if not op["airliner_msg"]:
            return None

        # Call the correct protobuf constructor for this command
        pb_obj = self._proto_obj_factory(op["airliner_msg"])

        # Generate executable string assigning correct values to pb object
        for arg in json["args"]:
            arg_path = self._get_op_attr(json["name"] + '/' + arg["name"])
            if not arg_path:
                raise pyliner_exceptions.InvalidCommandException(
                    "Invalid command received. Argument operational name (%s) "
                    "not found." % arg["name"])
            stmt = "pb_obj.{} = {}".format(arg_path, arg["value"])
            try:
                exec(stmt)
            except Exception as e:
                print('Problem with {}\n{}'.format(stmt, e))

        return pb_obj

    def _get_pb_value(self, pb_msg, op_path):
        """ Get value from protobuf object

        Args:
            pb_msg (ProtoObj): Protobuf object for this message
            op_path (str): Operation path as located in input file
                (E.g. "/Airliner/ES/Noop")

        Returns:
            Value of attribute for passed proto message
        """
        arg_path = self._get_op_attr(op_path)
        if not arg_path:
            return None
        # value = getattr(pb_msg, arg_path)
        value = None
        exec('value = pb_msg.' + arg_path)
        return value

    def _on_recv_telemetry(self, tlm):
        """ Callback for TO socket listener

        Args:
            tlm(str): Raw bytes received from socket
        """
        self.all_telemetry.append(tlm)
        # self.vehicle.debug("Recvd tlm: %s", tlm)

        # TODO: Check if needed
        hdr = tlm[0][:12]
        if len(hdr) < 12:
            self.vehicle.error(
                "Rcvd tlm with header length: %s", len(hdr))

        # Get python CCSDS object
        # TODO: Check what causes this to fail on some tlm packets
        try:
            header = bytearray(hdr)
            tlm_pkt = CCSDS_TlmPkt_t()
            tlm_pkt.set_decoded(header)
            tlm_time = tlm_pkt.get_time()
        except Exception as e:
            self.vehicle.error(
                "Exception when decoding tlm in ccsds: %s", e)
            return

        # Iterate over subscribed telemetry to check if we care
        for subscribed_tlm in self.subscribers:
            if int(subscribed_tlm['airliner_mid'], 0) == \
                    int(tlm_pkt.PriHdr.StreamId.data):
                # Get pb msg for this msg
                op_path = subscribed_tlm['op_path']
                pb_msg = self._get_pb_decode_obj(tlm[0][12:], op_path)

                # Update telemetry dictionary with fresh data
                self._telemetry[op_path].update(
                    value=self._get_pb_value(pb_msg, op_path), time=tlm_time)

    @staticmethod
    def _proto_obj_factory(msg):
        """ Returns a protobuf object for the type of airliner msg passed """
        return pyliner_msgs.proto_msg_map[msg]()

    @staticmethod
    def serialize(header, payload):
        """
        Receive a CCSDS message and payload then returns the
        serialized concatenation of them.
        """
        ser = header.get_encoded()
        if payload:
            ser += payload.SerializeToString()
        return ser

    def _serialize(self, telemetry):
        """ User accessible function to send a command to the software bus.

        Args:
            telemetry (Telemetry): Telemetry specifying the operation to execute
                and any args for it.
        """
        json = telemetry.to_json()
        if "name" not in json:
            raise pyliner_exceptions.InvalidCommandException(
                "Invalid command received. Missing \"name\" attribute")

        # Check if no args tlm
        args_present = "args" in json

        # Get command operation
        op = self._get_airliner_op(json["name"])
        if not op:
            raise pyliner_exceptions.InvalidCommandException(
                "Invalid telemetry received. Operation ({}) not "
                "defined.".format(json["name"]))

        # Generate airliner cmd
        header = self._get_ccsds_msg(op)
        payload = self._get_pb_encode_obj(json, op) if args_present else None

        # Set header correctly
        payload_size = payload.ByteSize() if args_present else 0
        header.set_user_data_length(payload_size)

        serial_cmd = Communication.serialize(header, payload)
        return serial_cmd

    def subscribe(self, tlm_item):
        """
        Receives an operational path to an airliner msg attribute to subscribe
        to, as well as an optional callback function.

        Args:
            tlm (dict[str, list[str]]): Dictionary specifying the telemetry
                items to subscribe to, using the telemetry item's operational
                names.
                E.g. {'tlm': ['/Airliner/ES/HK/CmdCounter']}
                    or
                     {'tlm': ['/Airliner/ES/HK/CmdCounter',
                              '/Airliner/ES/HK/ErrCounter']}
        """
        self.vehicle.info('Subscribing to: {}'.format(tlm_item))
        # Get operation for specified telemetry
        op = self._get_airliner_op(tlm_item)
        if not op:
            err_msg = "Invalid telemetry operational name received. " \
                      "Operation (%s) not defined." % tlm_item
            self.vehicle.error(err_msg)
            raise pyliner_exceptions.InvalidOperationException(err_msg)

        # Add entry to subscribers list
        self.subscribers.append({'op_path': tlm_item,
                                 'airliner_mid': op['airliner_mid'],
                                 'tlmSeqNum': 0})

        # Add entry to telemetry dictionary to prevent key errors
        # in user scripts and set default values.
        return _Telemetry(name=tlm_item)
