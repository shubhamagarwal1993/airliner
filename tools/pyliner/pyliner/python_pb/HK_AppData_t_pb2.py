# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_HK_AppData_t.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='_py_HK_AppData_t.proto',
  package='',
  serialized_pb=_b('\n\x16_py_HK_AppData_t.proto\"\xaa\x01\n\x10HK_HkPacket_t_pb\x12\x16\n\x0eMissingDataCtr\x18\x01 \x02(\r\x12\x12\n\nCmdCounter\x18\x02 \x02(\r\x12\x0f\n\x07Padding\x18\x03 \x02(\r\x12\x12\n\nErrCounter\x18\x04 \x02(\r\x12\x11\n\tTlmHeader\x18\x05 \x03(\r\x12\x1b\n\x13\x43ombinedPacketsSent\x18\x06 \x02(\r\x12\x15\n\rMemPoolHandle\x18\x07 \x02(\r\"\xe8\x02\n\x0fHK_AppData_t_pb\x12\x16\n\x0eMissingDataCtr\x18\x01 \x02(\r\x12\x12\n\nErrCounter\x18\x02 \x02(\r\x12\x1a\n\x12RuntimeTableHandle\x18\x03 \x02(\x05\x12\x0f\n\x07\x43mdPipe\x18\x04 \x02(\t\x12\x11\n\tRunStatus\x18\x05 \x02(\r\x12\x12\n\nCmdCounter\x18\x06 \x02(\r\x12\x0e\n\x06MsgPtr\x18\x07 \x02(\r\x12\x15\n\rMemPoolBuffer\x18\x08 \x03(\r\x12\r\n\x05Spare\x18\t \x02(\r\x12\x1b\n\x13\x43ombinedPacketsSent\x18\n \x02(\r\x12\x17\n\x0fRuntimeTablePtr\x18\x0b \x02(\r\x12\x17\n\x0f\x43opyTableHandle\x18\x0c \x02(\x05\x12\x14\n\x0c\x43opyTablePtr\x18\r \x02(\r\x12\x15\n\rMemPoolHandle\x18\x0e \x02(\r\x12#\n\x08HkPacket\x18\x0f \x02(\x0b\x32\x11.HK_HkPacket_t_pb')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_HK_HKPACKET_T_PB = _descriptor.Descriptor(
  name='HK_HkPacket_t_pb',
  full_name='HK_HkPacket_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='MissingDataCtr', full_name='HK_HkPacket_t_pb.MissingDataCtr', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CmdCounter', full_name='HK_HkPacket_t_pb.CmdCounter', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Padding', full_name='HK_HkPacket_t_pb.Padding', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ErrCounter', full_name='HK_HkPacket_t_pb.ErrCounter', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TlmHeader', full_name='HK_HkPacket_t_pb.TlmHeader', index=4,
      number=5, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CombinedPacketsSent', full_name='HK_HkPacket_t_pb.CombinedPacketsSent', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MemPoolHandle', full_name='HK_HkPacket_t_pb.MemPoolHandle', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=197,
)


_HK_APPDATA_T_PB = _descriptor.Descriptor(
  name='HK_AppData_t_pb',
  full_name='HK_AppData_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='MissingDataCtr', full_name='HK_AppData_t_pb.MissingDataCtr', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ErrCounter', full_name='HK_AppData_t_pb.ErrCounter', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RuntimeTableHandle', full_name='HK_AppData_t_pb.RuntimeTableHandle', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CmdPipe', full_name='HK_AppData_t_pb.CmdPipe', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RunStatus', full_name='HK_AppData_t_pb.RunStatus', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CmdCounter', full_name='HK_AppData_t_pb.CmdCounter', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MsgPtr', full_name='HK_AppData_t_pb.MsgPtr', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MemPoolBuffer', full_name='HK_AppData_t_pb.MemPoolBuffer', index=7,
      number=8, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Spare', full_name='HK_AppData_t_pb.Spare', index=8,
      number=9, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CombinedPacketsSent', full_name='HK_AppData_t_pb.CombinedPacketsSent', index=9,
      number=10, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RuntimeTablePtr', full_name='HK_AppData_t_pb.RuntimeTablePtr', index=10,
      number=11, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CopyTableHandle', full_name='HK_AppData_t_pb.CopyTableHandle', index=11,
      number=12, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CopyTablePtr', full_name='HK_AppData_t_pb.CopyTablePtr', index=12,
      number=13, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MemPoolHandle', full_name='HK_AppData_t_pb.MemPoolHandle', index=13,
      number=14, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='HkPacket', full_name='HK_AppData_t_pb.HkPacket', index=14,
      number=15, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=200,
  serialized_end=560,
)

_HK_APPDATA_T_PB.fields_by_name['HkPacket'].message_type = _HK_HKPACKET_T_PB
DESCRIPTOR.message_types_by_name['HK_HkPacket_t_pb'] = _HK_HKPACKET_T_PB
DESCRIPTOR.message_types_by_name['HK_AppData_t_pb'] = _HK_APPDATA_T_PB

HK_HkPacket_t_pb = _reflection.GeneratedProtocolMessageType('HK_HkPacket_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _HK_HKPACKET_T_PB,
  __module__ = '_py_HK_AppData_t_pb2'
  # @@protoc_insertion_point(class_scope:HK_HkPacket_t_pb)
  ))
_sym_db.RegisterMessage(HK_HkPacket_t_pb)

HK_AppData_t_pb = _reflection.GeneratedProtocolMessageType('HK_AppData_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _HK_APPDATA_T_PB,
  __module__ = '_py_HK_AppData_t_pb2'
  # @@protoc_insertion_point(class_scope:HK_AppData_t_pb)
  ))
_sym_db.RegisterMessage(HK_AppData_t_pb)


# @@protoc_insertion_point(module_scope)
