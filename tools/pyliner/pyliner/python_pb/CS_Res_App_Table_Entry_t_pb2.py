# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_CS_Res_App_Table_Entry_t.proto

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
  name='_py_CS_Res_App_Table_Entry_t.proto',
  package='',
  serialized_pb=_b('\n\"_py_CS_Res_App_Table_Entry_t.proto\"\xc9\x01\n\x1b\x43S_Res_App_Table_Entry_t_pb\x12\x1a\n\x12NumBytesToChecksum\x18\x01 \x02(\r\x12\x13\n\x0b\x43omputedYet\x18\x02 \x02(\r\x12\x19\n\x11TempChecksumValue\x18\x03 \x02(\r\x12\x0c\n\x04Name\x18\x04 \x02(\t\x12\r\n\x05State\x18\x05 \x02(\r\x12\x17\n\x0f\x43omparisonValue\x18\x06 \x02(\r\x12\x14\n\x0cStartAddress\x18\x07 \x02(\r\x12\x12\n\nByteOffset\x18\x08 \x02(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CS_RES_APP_TABLE_ENTRY_T_PB = _descriptor.Descriptor(
  name='CS_Res_App_Table_Entry_t_pb',
  full_name='CS_Res_App_Table_Entry_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='NumBytesToChecksum', full_name='CS_Res_App_Table_Entry_t_pb.NumBytesToChecksum', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ComputedYet', full_name='CS_Res_App_Table_Entry_t_pb.ComputedYet', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TempChecksumValue', full_name='CS_Res_App_Table_Entry_t_pb.TempChecksumValue', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Name', full_name='CS_Res_App_Table_Entry_t_pb.Name', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='State', full_name='CS_Res_App_Table_Entry_t_pb.State', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ComparisonValue', full_name='CS_Res_App_Table_Entry_t_pb.ComparisonValue', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StartAddress', full_name='CS_Res_App_Table_Entry_t_pb.StartAddress', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ByteOffset', full_name='CS_Res_App_Table_Entry_t_pb.ByteOffset', index=7,
      number=8, type=13, cpp_type=3, label=2,
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
  serialized_end=240,
)

DESCRIPTOR.message_types_by_name['CS_Res_App_Table_Entry_t_pb'] = _CS_RES_APP_TABLE_ENTRY_T_PB

CS_Res_App_Table_Entry_t_pb = _reflection.GeneratedProtocolMessageType('CS_Res_App_Table_Entry_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _CS_RES_APP_TABLE_ENTRY_T_PB,
  __module__ = '_py_CS_Res_App_Table_Entry_t_pb2'
  # @@protoc_insertion_point(class_scope:CS_Res_App_Table_Entry_t_pb)
  ))
_sym_db.RegisterMessage(CS_Res_App_Table_Entry_t_pb)


# @@protoc_insertion_point(module_scope)
