# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: myproto.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rmyproto.proto\x12\tmypackage\"+\n\x0fWeatherResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04temp\x18\x02 \x01(\t\"*\n\rCoinsResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05\x64olar\x18\x02 \x01(\t\"$\n\nUfResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\n\n\x02uf\x18\x02 \x01(\t\"\x07\n\x05\x45mpty2\xb8\x01\n\x04\x44\x61ta\x12>\n\x0eGetWeatherData\x12\x10.mypackage.Empty\x1a\x1a.mypackage.WeatherResponse\x12:\n\x0cGetCoinsData\x12\x10.mypackage.Empty\x1a\x18.mypackage.CoinsResponse\x12\x34\n\tGetUfData\x12\x10.mypackage.Empty\x1a\x15.mypackage.UfResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'myproto_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WEATHERRESPONSE._serialized_start=28
  _WEATHERRESPONSE._serialized_end=71
  _COINSRESPONSE._serialized_start=73
  _COINSRESPONSE._serialized_end=115
  _UFRESPONSE._serialized_start=117
  _UFRESPONSE._serialized_end=153
  _EMPTY._serialized_start=155
  _EMPTY._serialized_end=162
  _DATA._serialized_start=165
  _DATA._serialized_end=349
# @@protoc_insertion_point(module_scope)