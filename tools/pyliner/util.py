import SocketServer
import json
import socket
from datetime import datetime

from flufl.enum import Enum


class LogLevel(Enum):
    Debug = 1
    Info = 2
    Warn = 3
    Error = 4


class ThreadedUDPRequestHandler(SocketServer.BaseRequestHandler):
    def __init__(self, callback, *args, **keys):
        self.callback = callback
        SocketServer.BaseRequestHandler.__init__(self, *args, **keys)

    def handle(self):
        self.callback(self.request)


def get_time():
    return int((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds() * 10000)


def init_socket():
    """ Creates a UDP socket object and returns it """
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def read_json(file_path):
    """ Parses the required JSON input file containing Airliner mappings """
    try:
        with open(file_path, 'r') as airliner_map:
            return json.load(airliner_map)
    except IOError:
        print "Specified input file (%s) does not exist" % file_path
    except Exception as e:
        print e


def serialize(header, payload):
    """
    Receive a CCSDS message and payload then returns the
    serialized concatenation of them.
    """
    if not payload:
        return str(header.get_encoded())
    else:
        return str(header.get_encoded()) + payload.SerializeToString()


def server_factory(callback):
    """ Creates server object and sets the callback """
    def create_handler(*args, **kwargs):
        return ThreadedUDPRequestHandler(callback, *args, **kwargs)
    return create_handler