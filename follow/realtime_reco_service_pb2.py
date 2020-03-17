# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: realtime_reco_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import follow.realtime_reco_pb2 as realtime__reco__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='realtime_reco_service.proto',
  package='kuaishou.newsmodel',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1brealtime_reco_service.proto\x12\x12kuaishou.newsmodel\x1a\x13realtime_reco.proto2k\n\x13RealTimeRecoService\x12T\n\x15GetRealTimeRecoResult\x12\x1c.ks.reco.RealTimeRecoRequest\x1a\x1d.ks.reco.RealTimeRecoResponse')
  ,
  dependencies=[realtime__reco__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_REALTIMERECOSERVICE = _descriptor.ServiceDescriptor(
  name='RealTimeRecoService',
  full_name='kuaishou.newsmodel.RealTimeRecoService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=72,
  serialized_end=179,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetRealTimeRecoResult',
    full_name='kuaishou.newsmodel.RealTimeRecoService.GetRealTimeRecoResult',
    index=0,
    containing_service=None,
    input_type=realtime__reco__pb2._REALTIMERECOREQUEST,
    output_type=realtime__reco__pb2._REALTIMERECORESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_REALTIMERECOSERVICE)

DESCRIPTOR.services_by_name['RealTimeRecoService'] = _REALTIMERECOSERVICE

# @@protoc_insertion_point(module_scope)