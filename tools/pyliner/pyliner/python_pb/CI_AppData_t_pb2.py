# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_CI_AppData_t.proto

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
  name='_py_CI_AppData_t.proto',
  package='',
  serialized_pb=_b('\n\x16_py_CI_AppData_t.proto\"9\n\x0f\x43I_OutData_t_pb\x12\x13\n\x0bucTlmHeader\x18\x01 \x03(\r\x12\x11\n\tuiCounter\x18\x02 \x02(\r\" \n\x0e\x43I_CdsTbl_t_pb\x12\x0e\n\x06iParam\x18\x01 \x02(\x05\"7\n\x16\x43\x46\x45_EVS_BinFilter_t_pb\x12\x0f\n\x07\x45ventID\x18\x01 \x02(\r\x12\x0c\n\x04Mask\x18\x02 \x02(\r\"\x8c\x01\n\rCI_HkTlm_t_pb\x12\x10\n\x08usCmdCnt\x18\x01 \x02(\r\x12\x16\n\x0eIngestMsgCount\x18\x02 \x02(\r\x12\x0f\n\x07padding\x18\x03 \x03(\r\x12\x11\n\tTlmHeader\x18\x04 \x03(\r\x12\x13\n\x0busCmdErrCnt\x18\x05 \x02(\r\x12\x18\n\x10IngestErrorCount\x18\x06 \x02(\r\"8\n\x17\x43I_TimeoutTblEntry_t_pb\x12\x0f\n\x07TableID\x18\x01 \x02(\r\x12\x0c\n\x04time\x18\x02 \x03(\r\"4\n\x0e\x43I_InData_t_pb\x12\x11\n\tTlmHeader\x18\x01 \x03(\r\x12\x0f\n\x07\x63ounter\x18\x02 \x02(\r\"\xda\x04\n\x0f\x43I_AppData_t_pb\x12\x1a\n\x12SerialIngestBuffer\x18\x01 \x03(\r\x12\x1f\n\x06\x43\x64sTbl\x18\x02 \x02(\x0b\x32\x0f.CI_CdsTbl_t_pb\x12\x16\n\x0e\x43onfigTblMutex\x18\x03 \x02(\r\x12\x1d\n\x05HkTlm\x18\x04 \x02(\x0b\x32\x0e.CI_HkTlm_t_pb\x12!\n\x07OutData\x18\x05 \x02(\x0b\x32\x10.CI_OutData_t_pb\x12\x15\n\rTimeoutTblHdl\x18\x06 \x02(\x05\x12\x14\n\x0cIngestActive\x18\x07 \x02(\x08\x12\x14\n\x0c\x43onfigTblPtr\x18\x08 \x02(\r\x12\x11\n\tSchPipeId\x18\t \x02(\t\x12\x1f\n\x06InData\x18\n \x02(\x0b\x32\x0f.CI_InData_t_pb\x12\x11\n\tCdsTblHdl\x18\x0b \x02(\r\x12\x17\n\x0fTimeoutTblMutex\x18\x0c \x02(\r\x12\x1c\n\x14SerialListenerTaskID\x18\r \x02(\r\x12\x12\n\nDataPipeId\x18\x0e \x02(\t\x12\x14\n\x0cIngestBuffer\x18\x0f \x03(\r\x12,\n\nTimeoutTbl\x18\x10 \x02(\x0b\x32\x18.CI_TimeoutTblEntry_t_pb\x12)\n\x08\x45ventTbl\x18\x11 \x03(\x0b\x32\x17.CFE_EVS_BinFilter_t_pb\x12\x16\n\x0eListenerTaskID\x18\x12 \x02(\r\x12\x13\n\x0buiRunStatus\x18\x13 \x02(\r\x12\x11\n\tCmdPipeId\x18\x14 \x02(\t\x12\x16\n\x0eIngestBehavior\x18\x15 \x02(\r\x12\x14\n\x0c\x43onfigTblHdl\x18\x16 \x02(\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CI_OUTDATA_T_PB = _descriptor.Descriptor(
  name='CI_OutData_t_pb',
  full_name='CI_OutData_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ucTlmHeader', full_name='CI_OutData_t_pb.ucTlmHeader', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uiCounter', full_name='CI_OutData_t_pb.uiCounter', index=1,
      number=2, type=13, cpp_type=3, label=2,
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
  serialized_start=26,
  serialized_end=83,
)


_CI_CDSTBL_T_PB = _descriptor.Descriptor(
  name='CI_CdsTbl_t_pb',
  full_name='CI_CdsTbl_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iParam', full_name='CI_CdsTbl_t_pb.iParam', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  serialized_start=85,
  serialized_end=117,
)


_CFE_EVS_BINFILTER_T_PB = _descriptor.Descriptor(
  name='CFE_EVS_BinFilter_t_pb',
  full_name='CFE_EVS_BinFilter_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='EventID', full_name='CFE_EVS_BinFilter_t_pb.EventID', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Mask', full_name='CFE_EVS_BinFilter_t_pb.Mask', index=1,
      number=2, type=13, cpp_type=3, label=2,
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
  serialized_start=119,
  serialized_end=174,
)


_CI_HKTLM_T_PB = _descriptor.Descriptor(
  name='CI_HkTlm_t_pb',
  full_name='CI_HkTlm_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='usCmdCnt', full_name='CI_HkTlm_t_pb.usCmdCnt', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='IngestMsgCount', full_name='CI_HkTlm_t_pb.IngestMsgCount', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='padding', full_name='CI_HkTlm_t_pb.padding', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TlmHeader', full_name='CI_HkTlm_t_pb.TlmHeader', index=3,
      number=4, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='usCmdErrCnt', full_name='CI_HkTlm_t_pb.usCmdErrCnt', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='IngestErrorCount', full_name='CI_HkTlm_t_pb.IngestErrorCount', index=5,
      number=6, type=13, cpp_type=3, label=2,
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
  serialized_start=177,
  serialized_end=317,
)


_CI_TIMEOUTTBLENTRY_T_PB = _descriptor.Descriptor(
  name='CI_TimeoutTblEntry_t_pb',
  full_name='CI_TimeoutTblEntry_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='TableID', full_name='CI_TimeoutTblEntry_t_pb.TableID', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='CI_TimeoutTblEntry_t_pb.time', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=319,
  serialized_end=375,
)


_CI_INDATA_T_PB = _descriptor.Descriptor(
  name='CI_InData_t_pb',
  full_name='CI_InData_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='TlmHeader', full_name='CI_InData_t_pb.TlmHeader', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='counter', full_name='CI_InData_t_pb.counter', index=1,
      number=2, type=13, cpp_type=3, label=2,
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
  serialized_start=377,
  serialized_end=429,
)


_CI_APPDATA_T_PB = _descriptor.Descriptor(
  name='CI_AppData_t_pb',
  full_name='CI_AppData_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='SerialIngestBuffer', full_name='CI_AppData_t_pb.SerialIngestBuffer', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CdsTbl', full_name='CI_AppData_t_pb.CdsTbl', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ConfigTblMutex', full_name='CI_AppData_t_pb.ConfigTblMutex', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='HkTlm', full_name='CI_AppData_t_pb.HkTlm', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OutData', full_name='CI_AppData_t_pb.OutData', index=4,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TimeoutTblHdl', full_name='CI_AppData_t_pb.TimeoutTblHdl', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='IngestActive', full_name='CI_AppData_t_pb.IngestActive', index=6,
      number=7, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ConfigTblPtr', full_name='CI_AppData_t_pb.ConfigTblPtr', index=7,
      number=8, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SchPipeId', full_name='CI_AppData_t_pb.SchPipeId', index=8,
      number=9, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='InData', full_name='CI_AppData_t_pb.InData', index=9,
      number=10, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CdsTblHdl', full_name='CI_AppData_t_pb.CdsTblHdl', index=10,
      number=11, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TimeoutTblMutex', full_name='CI_AppData_t_pb.TimeoutTblMutex', index=11,
      number=12, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SerialListenerTaskID', full_name='CI_AppData_t_pb.SerialListenerTaskID', index=12,
      number=13, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DataPipeId', full_name='CI_AppData_t_pb.DataPipeId', index=13,
      number=14, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='IngestBuffer', full_name='CI_AppData_t_pb.IngestBuffer', index=14,
      number=15, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TimeoutTbl', full_name='CI_AppData_t_pb.TimeoutTbl', index=15,
      number=16, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='EventTbl', full_name='CI_AppData_t_pb.EventTbl', index=16,
      number=17, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ListenerTaskID', full_name='CI_AppData_t_pb.ListenerTaskID', index=17,
      number=18, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uiRunStatus', full_name='CI_AppData_t_pb.uiRunStatus', index=18,
      number=19, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CmdPipeId', full_name='CI_AppData_t_pb.CmdPipeId', index=19,
      number=20, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='IngestBehavior', full_name='CI_AppData_t_pb.IngestBehavior', index=20,
      number=21, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ConfigTblHdl', full_name='CI_AppData_t_pb.ConfigTblHdl', index=21,
      number=22, type=5, cpp_type=1, label=2,
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
  serialized_start=432,
  serialized_end=1034,
)

_CI_APPDATA_T_PB.fields_by_name['CdsTbl'].message_type = _CI_CDSTBL_T_PB
_CI_APPDATA_T_PB.fields_by_name['HkTlm'].message_type = _CI_HKTLM_T_PB
_CI_APPDATA_T_PB.fields_by_name['OutData'].message_type = _CI_OUTDATA_T_PB
_CI_APPDATA_T_PB.fields_by_name['InData'].message_type = _CI_INDATA_T_PB
_CI_APPDATA_T_PB.fields_by_name['TimeoutTbl'].message_type = _CI_TIMEOUTTBLENTRY_T_PB
_CI_APPDATA_T_PB.fields_by_name['EventTbl'].message_type = _CFE_EVS_BINFILTER_T_PB
DESCRIPTOR.message_types_by_name['CI_OutData_t_pb'] = _CI_OUTDATA_T_PB
DESCRIPTOR.message_types_by_name['CI_CdsTbl_t_pb'] = _CI_CDSTBL_T_PB
DESCRIPTOR.message_types_by_name['CFE_EVS_BinFilter_t_pb'] = _CFE_EVS_BINFILTER_T_PB
DESCRIPTOR.message_types_by_name['CI_HkTlm_t_pb'] = _CI_HKTLM_T_PB
DESCRIPTOR.message_types_by_name['CI_TimeoutTblEntry_t_pb'] = _CI_TIMEOUTTBLENTRY_T_PB
DESCRIPTOR.message_types_by_name['CI_InData_t_pb'] = _CI_INDATA_T_PB
DESCRIPTOR.message_types_by_name['CI_AppData_t_pb'] = _CI_APPDATA_T_PB

CI_OutData_t_pb = _reflection.GeneratedProtocolMessageType('CI_OutData_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _CI_OUTDATA_T_PB,
  __module__ = '_py_CI_AppData_t_pb2'
  # @@protoc_insertion_point(class_scope:CI_OutData_t_pb)
  ))
_sym_db.RegisterMessage(CI_OutData_t_pb)

CI_CdsTbl_t_pb = _reflection.GeneratedProtocolMessageType('CI_CdsTbl_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _CI_CDSTBL_T_PB,
  __module__ = '_py_CI_AppData_t_pb2'
  # @@protoc_insertion_point(class_scope:CI_CdsTbl_t_pb)
  ))
_sym_db.RegisterMessage(CI_CdsTbl_t_pb)

CFE_EVS_BinFilter_t_pb = _reflection.GeneratedProtocolMessageType('CFE_EVS_BinFilter_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _CFE_EVS_BINFILTER_T_PB,
  __module__ = '_py_CI_AppData_t_pb2'
  # @@protoc_insertion_point(class_scope:CFE_EVS_BinFilter_t_pb)
  ))
_sym_db.RegisterMessage(CFE_EVS_BinFilter_t_pb)

CI_HkTlm_t_pb = _reflection.GeneratedProtocolMessageType('CI_HkTlm_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _CI_HKTLM_T_PB,
  __module__ = '_py_CI_AppData_t_pb2'
  # @@protoc_insertion_point(class_scope:CI_HkTlm_t_pb)
  ))
_sym_db.RegisterMessage(CI_HkTlm_t_pb)

CI_TimeoutTblEntry_t_pb = _reflection.GeneratedProtocolMessageType('CI_TimeoutTblEntry_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _CI_TIMEOUTTBLENTRY_T_PB,
  __module__ = '_py_CI_AppData_t_pb2'
  # @@protoc_insertion_point(class_scope:CI_TimeoutTblEntry_t_pb)
  ))
_sym_db.RegisterMessage(CI_TimeoutTblEntry_t_pb)

CI_InData_t_pb = _reflection.GeneratedProtocolMessageType('CI_InData_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _CI_INDATA_T_PB,
  __module__ = '_py_CI_AppData_t_pb2'
  # @@protoc_insertion_point(class_scope:CI_InData_t_pb)
  ))
_sym_db.RegisterMessage(CI_InData_t_pb)

CI_AppData_t_pb = _reflection.GeneratedProtocolMessageType('CI_AppData_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _CI_APPDATA_T_PB,
  __module__ = '_py_CI_AppData_t_pb2'
  # @@protoc_insertion_point(class_scope:CI_AppData_t_pb)
  ))
_sym_db.RegisterMessage(CI_AppData_t_pb)


# @@protoc_insertion_point(module_scope)
