# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_CFE_ES_PerfMetaData_t.proto

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
  name='_py_CFE_ES_PerfMetaData_t.proto',
  package='',
  serialized_pb=_b('\n\x1f_py_CFE_ES_PerfMetaData_t.proto\"\xd4\x02\n\x18\x43\x46\x45_ES_PerfMetaData_t_pb\x12\x12\n\nFilterMask\x18\x01 \x03(\r\x12\x1d\n\x15InvalidMarkerReported\x18\x02 \x02(\r\x12\x1a\n\x12TimerLow32Rollover\x18\x03 \x02(\r\x12\x0e\n\x06\x45ndian\x18\x04 \x02(\r\x12\x14\n\x0cTriggerCount\x18\x05 \x02(\r\x12\x13\n\x0bTriggerMask\x18\x06 \x03(\r\x12\r\n\x05State\x18\x07 \x02(\r\x12\x0f\n\x07Version\x18\x08 \x02(\r\x12\r\n\x05Spare\x18\t \x03(\r\x12\x11\n\tDataStart\x18\n \x02(\r\x12\x11\n\tDataCount\x18\x0b \x02(\r\x12\x1b\n\x13TimerTicksPerSecond\x18\x0c \x02(\r\x12\x0f\n\x07\x44\x61taEnd\x18\r \x02(\r\x12\x1d\n\x15\x46ilterTriggerMaskSize\x18\x0e \x02(\r\x12\x0c\n\x04Mode\x18\x0f \x02(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CFE_ES_PERFMETADATA_T_PB = _descriptor.Descriptor(
  name='CFE_ES_PerfMetaData_t_pb',
  full_name='CFE_ES_PerfMetaData_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='FilterMask', full_name='CFE_ES_PerfMetaData_t_pb.FilterMask', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='InvalidMarkerReported', full_name='CFE_ES_PerfMetaData_t_pb.InvalidMarkerReported', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TimerLow32Rollover', full_name='CFE_ES_PerfMetaData_t_pb.TimerLow32Rollover', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Endian', full_name='CFE_ES_PerfMetaData_t_pb.Endian', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TriggerCount', full_name='CFE_ES_PerfMetaData_t_pb.TriggerCount', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TriggerMask', full_name='CFE_ES_PerfMetaData_t_pb.TriggerMask', index=5,
      number=6, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='State', full_name='CFE_ES_PerfMetaData_t_pb.State', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Version', full_name='CFE_ES_PerfMetaData_t_pb.Version', index=7,
      number=8, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Spare', full_name='CFE_ES_PerfMetaData_t_pb.Spare', index=8,
      number=9, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DataStart', full_name='CFE_ES_PerfMetaData_t_pb.DataStart', index=9,
      number=10, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DataCount', full_name='CFE_ES_PerfMetaData_t_pb.DataCount', index=10,
      number=11, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TimerTicksPerSecond', full_name='CFE_ES_PerfMetaData_t_pb.TimerTicksPerSecond', index=11,
      number=12, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DataEnd', full_name='CFE_ES_PerfMetaData_t_pb.DataEnd', index=12,
      number=13, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FilterTriggerMaskSize', full_name='CFE_ES_PerfMetaData_t_pb.FilterTriggerMaskSize', index=13,
      number=14, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Mode', full_name='CFE_ES_PerfMetaData_t_pb.Mode', index=14,
      number=15, type=13, cpp_type=3, label=2,
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
  serialized_start=36,
  serialized_end=376,
)

DESCRIPTOR.message_types_by_name['CFE_ES_PerfMetaData_t_pb'] = _CFE_ES_PERFMETADATA_T_PB

CFE_ES_PerfMetaData_t_pb = _reflection.GeneratedProtocolMessageType('CFE_ES_PerfMetaData_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _CFE_ES_PERFMETADATA_T_PB,
  __module__ = '_py_CFE_ES_PerfMetaData_t_pb2'
  # @@protoc_insertion_point(class_scope:CFE_ES_PerfMetaData_t_pb)
  ))
_sym_db.RegisterMessage(CFE_ES_PerfMetaData_t_pb)


# @@protoc_insertion_point(module_scope)
