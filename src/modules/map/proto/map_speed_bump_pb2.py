# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/map/proto/map_speed_bump.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from modules.map.proto import map_id_pb2 as modules_dot_map_dot_proto_dot_map__id__pb2
from modules.map.proto import map_geometry_pb2 as modules_dot_map_dot_proto_dot_map__geometry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/map/proto/map_speed_bump.proto',
  package='apollo.hdmap',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n&modules/map/proto/map_speed_bump.proto\x12\x0c\x61pollo.hdmap\x1a\x1emodules/map/proto/map_id.proto\x1a$modules/map/proto/map_geometry.proto\"v\n\tSpeedBump\x12\x1c\n\x02id\x18\x01 \x01(\x0b\x32\x10.apollo.hdmap.Id\x12$\n\noverlap_id\x18\x02 \x03(\x0b\x32\x10.apollo.hdmap.Id\x12%\n\x08position\x18\x03 \x03(\x0b\x32\x13.apollo.hdmap.Curve')
  ,
  dependencies=[modules_dot_map_dot_proto_dot_map__id__pb2.DESCRIPTOR,modules_dot_map_dot_proto_dot_map__geometry__pb2.DESCRIPTOR,])




_SPEEDBUMP = _descriptor.Descriptor(
  name='SpeedBump',
  full_name='apollo.hdmap.SpeedBump',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='apollo.hdmap.SpeedBump.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='overlap_id', full_name='apollo.hdmap.SpeedBump.overlap_id', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position', full_name='apollo.hdmap.SpeedBump.position', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=244,
)

_SPEEDBUMP.fields_by_name['id'].message_type = modules_dot_map_dot_proto_dot_map__id__pb2._ID
_SPEEDBUMP.fields_by_name['overlap_id'].message_type = modules_dot_map_dot_proto_dot_map__id__pb2._ID
_SPEEDBUMP.fields_by_name['position'].message_type = modules_dot_map_dot_proto_dot_map__geometry__pb2._CURVE
DESCRIPTOR.message_types_by_name['SpeedBump'] = _SPEEDBUMP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SpeedBump = _reflection.GeneratedProtocolMessageType('SpeedBump', (_message.Message,), dict(
  DESCRIPTOR = _SPEEDBUMP,
  __module__ = 'modules.map.proto.map_speed_bump_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.SpeedBump)
  ))
_sym_db.RegisterMessage(SpeedBump)


# @@protoc_insertion_point(module_scope)