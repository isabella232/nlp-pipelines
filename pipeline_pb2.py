# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pipeline.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pipeline.proto',
  package='pipelines',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0epipeline.proto\x12\tpipelines\"\n\n\x08To_lower\"5\n\nHash_ngram\x12\x13\n\x0bnum_buckets\x18\x01 \x01(\x05\x12\x12\n\nhash_sizes\x18\x02 \x03(\x05\"x\n\x0eTransformation\x12\'\n\x08to_lower\x18\x01 \x01(\x0b\x32\x13.pipelines.To_lowerH\x00\x12+\n\nhash_ngram\x18\x02 \x01(\x0b\x32\x15.pipelines.Hash_ngramH\x00\x42\x10\n\x0eRepresentation\"\x1a\n\x06Vector\x12\x10\n\x08\x65lements\x18\x01 \x03(\x02\"X\n\x0bNaive_bayes\x12\x0f\n\x07\x63lasses\x18\x01 \x03(\t\x12\"\n\x07vectors\x18\x02 \x03(\x0b\x32\x11.pipelines.Vector\x12\x14\n\x0c\x63lass_priors\x18\x03 \x03(\x02\"$\n\x11Linear_classifier\x12\x0f\n\x07\x63lasses\x18\x01 \x03(\t\"l\n\nClassifier\x12$\n\x02nb\x18\x01 \x01(\x0b\x32\x16.pipelines.Naive_bayesH\x00\x12*\n\x02lc\x18\x02 \x01(\x0b\x32\x1c.pipelines.Linear_classifierH\x00\x42\x0c\n\nclassifier\"\x8d\x01\n\x08Pipeline\x12\x10\n\x08language\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\t\x12\x31\n\x0erepresentation\x18\x03 \x03(\x0b\x32\x19.pipelines.Transformation\x12)\n\nclassifier\x18\x04 \x01(\x0b\x32\x15.pipelines.Classifierb\x06proto3')
)




_TO_LOWER = _descriptor.Descriptor(
  name='To_lower',
  full_name='pipelines.To_lower',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=39,
)


_HASH_NGRAM = _descriptor.Descriptor(
  name='Hash_ngram',
  full_name='pipelines.Hash_ngram',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_buckets', full_name='pipelines.Hash_ngram.num_buckets', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash_sizes', full_name='pipelines.Hash_ngram.hash_sizes', index=1,
      number=2, type=5, cpp_type=1, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=94,
)


_TRANSFORMATION = _descriptor.Descriptor(
  name='Transformation',
  full_name='pipelines.Transformation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='to_lower', full_name='pipelines.Transformation.to_lower', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash_ngram', full_name='pipelines.Transformation.hash_ngram', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Representation', full_name='pipelines.Transformation.Representation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=96,
  serialized_end=216,
)


_VECTOR = _descriptor.Descriptor(
  name='Vector',
  full_name='pipelines.Vector',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='elements', full_name='pipelines.Vector.elements', index=0,
      number=1, type=2, cpp_type=6, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=218,
  serialized_end=244,
)


_NAIVE_BAYES = _descriptor.Descriptor(
  name='Naive_bayes',
  full_name='pipelines.Naive_bayes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='classes', full_name='pipelines.Naive_bayes.classes', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vectors', full_name='pipelines.Naive_bayes.vectors', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='class_priors', full_name='pipelines.Naive_bayes.class_priors', index=2,
      number=3, type=2, cpp_type=6, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=246,
  serialized_end=334,
)


_LINEAR_CLASSIFIER = _descriptor.Descriptor(
  name='Linear_classifier',
  full_name='pipelines.Linear_classifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='classes', full_name='pipelines.Linear_classifier.classes', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=336,
  serialized_end=372,
)


_CLASSIFIER = _descriptor.Descriptor(
  name='Classifier',
  full_name='pipelines.Classifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nb', full_name='pipelines.Classifier.nb', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lc', full_name='pipelines.Classifier.lc', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='classifier', full_name='pipelines.Classifier.classifier',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=374,
  serialized_end=482,
)


_PIPELINE = _descriptor.Descriptor(
  name='Pipeline',
  full_name='pipelines.Pipeline',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='language', full_name='pipelines.Pipeline.language', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='pipelines.Pipeline.timestamp', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='representation', full_name='pipelines.Pipeline.representation', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classifier', full_name='pipelines.Pipeline.classifier', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=485,
  serialized_end=626,
)

_TRANSFORMATION.fields_by_name['to_lower'].message_type = _TO_LOWER
_TRANSFORMATION.fields_by_name['hash_ngram'].message_type = _HASH_NGRAM
_TRANSFORMATION.oneofs_by_name['Representation'].fields.append(
  _TRANSFORMATION.fields_by_name['to_lower'])
_TRANSFORMATION.fields_by_name['to_lower'].containing_oneof = _TRANSFORMATION.oneofs_by_name['Representation']
_TRANSFORMATION.oneofs_by_name['Representation'].fields.append(
  _TRANSFORMATION.fields_by_name['hash_ngram'])
_TRANSFORMATION.fields_by_name['hash_ngram'].containing_oneof = _TRANSFORMATION.oneofs_by_name['Representation']
_NAIVE_BAYES.fields_by_name['vectors'].message_type = _VECTOR
_CLASSIFIER.fields_by_name['nb'].message_type = _NAIVE_BAYES
_CLASSIFIER.fields_by_name['lc'].message_type = _LINEAR_CLASSIFIER
_CLASSIFIER.oneofs_by_name['classifier'].fields.append(
  _CLASSIFIER.fields_by_name['nb'])
_CLASSIFIER.fields_by_name['nb'].containing_oneof = _CLASSIFIER.oneofs_by_name['classifier']
_CLASSIFIER.oneofs_by_name['classifier'].fields.append(
  _CLASSIFIER.fields_by_name['lc'])
_CLASSIFIER.fields_by_name['lc'].containing_oneof = _CLASSIFIER.oneofs_by_name['classifier']
_PIPELINE.fields_by_name['representation'].message_type = _TRANSFORMATION
_PIPELINE.fields_by_name['classifier'].message_type = _CLASSIFIER
DESCRIPTOR.message_types_by_name['To_lower'] = _TO_LOWER
DESCRIPTOR.message_types_by_name['Hash_ngram'] = _HASH_NGRAM
DESCRIPTOR.message_types_by_name['Transformation'] = _TRANSFORMATION
DESCRIPTOR.message_types_by_name['Vector'] = _VECTOR
DESCRIPTOR.message_types_by_name['Naive_bayes'] = _NAIVE_BAYES
DESCRIPTOR.message_types_by_name['Linear_classifier'] = _LINEAR_CLASSIFIER
DESCRIPTOR.message_types_by_name['Classifier'] = _CLASSIFIER
DESCRIPTOR.message_types_by_name['Pipeline'] = _PIPELINE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

To_lower = _reflection.GeneratedProtocolMessageType('To_lower', (_message.Message,), dict(
  DESCRIPTOR = _TO_LOWER,
  __module__ = 'pipeline_pb2'
  # @@protoc_insertion_point(class_scope:pipelines.To_lower)
  ))
_sym_db.RegisterMessage(To_lower)

Hash_ngram = _reflection.GeneratedProtocolMessageType('Hash_ngram', (_message.Message,), dict(
  DESCRIPTOR = _HASH_NGRAM,
  __module__ = 'pipeline_pb2'
  # @@protoc_insertion_point(class_scope:pipelines.Hash_ngram)
  ))
_sym_db.RegisterMessage(Hash_ngram)

Transformation = _reflection.GeneratedProtocolMessageType('Transformation', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFORMATION,
  __module__ = 'pipeline_pb2'
  # @@protoc_insertion_point(class_scope:pipelines.Transformation)
  ))
_sym_db.RegisterMessage(Transformation)

Vector = _reflection.GeneratedProtocolMessageType('Vector', (_message.Message,), dict(
  DESCRIPTOR = _VECTOR,
  __module__ = 'pipeline_pb2'
  # @@protoc_insertion_point(class_scope:pipelines.Vector)
  ))
_sym_db.RegisterMessage(Vector)

Naive_bayes = _reflection.GeneratedProtocolMessageType('Naive_bayes', (_message.Message,), dict(
  DESCRIPTOR = _NAIVE_BAYES,
  __module__ = 'pipeline_pb2'
  # @@protoc_insertion_point(class_scope:pipelines.Naive_bayes)
  ))
_sym_db.RegisterMessage(Naive_bayes)

Linear_classifier = _reflection.GeneratedProtocolMessageType('Linear_classifier', (_message.Message,), dict(
  DESCRIPTOR = _LINEAR_CLASSIFIER,
  __module__ = 'pipeline_pb2'
  # @@protoc_insertion_point(class_scope:pipelines.Linear_classifier)
  ))
_sym_db.RegisterMessage(Linear_classifier)

Classifier = _reflection.GeneratedProtocolMessageType('Classifier', (_message.Message,), dict(
  DESCRIPTOR = _CLASSIFIER,
  __module__ = 'pipeline_pb2'
  # @@protoc_insertion_point(class_scope:pipelines.Classifier)
  ))
_sym_db.RegisterMessage(Classifier)

Pipeline = _reflection.GeneratedProtocolMessageType('Pipeline', (_message.Message,), dict(
  DESCRIPTOR = _PIPELINE,
  __module__ = 'pipeline_pb2'
  # @@protoc_insertion_point(class_scope:pipelines.Pipeline)
  ))
_sym_db.RegisterMessage(Pipeline)


# @@protoc_insertion_point(module_scope)
