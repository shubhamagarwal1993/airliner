# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_RGBLED_Device_Settings_t.proto

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
  name='_py_RGBLED_Device_Settings_t.proto',
  package='',
  serialized_pb=_b('\n\"_py_RGBLED_Device_Settings_t.proto\"\x89\x01\n\x1bRGBLED_Device_Settings_t_pb\x12\x14\n\x0cNotPowerSave\x18\x01 \x02(\x08\x12\x16\n\x0eGreenDutyCycle\x18\x02 \x02(\r\x12\x0f\n\x07\x45nabled\x18\x03 \x02(\x08\x12\x14\n\x0cRedDutyCycle\x18\x04 \x02(\r\x12\x15\n\rBlueDutyCycle\x18\x05 \x02(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RGBLED_DEVICE_SETTINGS_T_PB = _descriptor.Descriptor(
  name='RGBLED_Device_Settings_t_pb',
  full_name='RGBLED_Device_Settings_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='NotPowerSave', full_name='RGBLED_Device_Settings_t_pb.NotPowerSave', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GreenDutyCycle', full_name='RGBLED_Device_Settings_t_pb.GreenDutyCycle', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Enabled', full_name='RGBLED_Device_Settings_t_pb.Enabled', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RedDutyCycle', full_name='RGBLED_Device_Settings_t_pb.RedDutyCycle', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BlueDutyCycle', full_name='RGBLED_Device_Settings_t_pb.BlueDutyCycle', index=4,
      number=5, type=13, cpp_type=3, label=2,
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
  serialized_start=39,
  serialized_end=176,
)

DESCRIPTOR.message_types_by_name['RGBLED_Device_Settings_t_pb'] = _RGBLED_DEVICE_SETTINGS_T_PB

RGBLED_Device_Settings_t_pb = _reflection.GeneratedProtocolMessageType('RGBLED_Device_Settings_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _RGBLED_DEVICE_SETTINGS_T_PB,
  __module__ = '_py_RGBLED_Device_Settings_t_pb2'
  # @@protoc_insertion_point(class_scope:RGBLED_Device_Settings_t_pb)
  ))
_sym_db.RegisterMessage(RGBLED_Device_Settings_t_pb)


# @@protoc_insertion_point(module_scope)
