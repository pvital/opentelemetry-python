# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: opentelemetry/proto/metrics/v1/metrics.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from opentelemetry.proto.common.v1 import common_pb2 as opentelemetry_dot_proto_dot_common_dot_v1_dot_common__pb2
from opentelemetry.proto.resource.v1 import resource_pb2 as opentelemetry_dot_proto_dot_resource_dot_v1_dot_resource__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,opentelemetry/proto/metrics/v1/metrics.proto\x12\x1eopentelemetry.proto.metrics.v1\x1a*opentelemetry/proto/common/v1/common.proto\x1a.opentelemetry/proto/resource/v1/resource.proto\"X\n\x0bMetricsData\x12I\n\x10resource_metrics\x18\x01 \x03(\x0b\x32/.opentelemetry.proto.metrics.v1.ResourceMetrics\"\xaf\x01\n\x0fResourceMetrics\x12;\n\x08resource\x18\x01 \x01(\x0b\x32).opentelemetry.proto.resource.v1.Resource\x12\x43\n\rscope_metrics\x18\x02 \x03(\x0b\x32,.opentelemetry.proto.metrics.v1.ScopeMetrics\x12\x12\n\nschema_url\x18\x03 \x01(\tJ\x06\x08\xe8\x07\x10\xe9\x07\"\x9f\x01\n\x0cScopeMetrics\x12\x42\n\x05scope\x18\x01 \x01(\x0b\x32\x33.opentelemetry.proto.common.v1.InstrumentationScope\x12\x37\n\x07metrics\x18\x02 \x03(\x0b\x32&.opentelemetry.proto.metrics.v1.Metric\x12\x12\n\nschema_url\x18\x03 \x01(\t\"\xcd\x03\n\x06Metric\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04unit\x18\x03 \x01(\t\x12\x36\n\x05gauge\x18\x05 \x01(\x0b\x32%.opentelemetry.proto.metrics.v1.GaugeH\x00\x12\x32\n\x03sum\x18\x07 \x01(\x0b\x32#.opentelemetry.proto.metrics.v1.SumH\x00\x12>\n\thistogram\x18\t \x01(\x0b\x32).opentelemetry.proto.metrics.v1.HistogramH\x00\x12U\n\x15\x65xponential_histogram\x18\n \x01(\x0b\x32\x34.opentelemetry.proto.metrics.v1.ExponentialHistogramH\x00\x12:\n\x07summary\x18\x0b \x01(\x0b\x32\'.opentelemetry.proto.metrics.v1.SummaryH\x00\x12\x39\n\x08metadata\x18\x0c \x03(\x0b\x32\'.opentelemetry.proto.common.v1.KeyValueB\x06\n\x04\x64\x61taJ\x04\x08\x04\x10\x05J\x04\x08\x06\x10\x07J\x04\x08\x08\x10\t\"M\n\x05Gauge\x12\x44\n\x0b\x64\x61ta_points\x18\x01 \x03(\x0b\x32/.opentelemetry.proto.metrics.v1.NumberDataPoint\"\xba\x01\n\x03Sum\x12\x44\n\x0b\x64\x61ta_points\x18\x01 \x03(\x0b\x32/.opentelemetry.proto.metrics.v1.NumberDataPoint\x12W\n\x17\x61ggregation_temporality\x18\x02 \x01(\x0e\x32\x36.opentelemetry.proto.metrics.v1.AggregationTemporality\x12\x14\n\x0cis_monotonic\x18\x03 \x01(\x08\"\xad\x01\n\tHistogram\x12G\n\x0b\x64\x61ta_points\x18\x01 \x03(\x0b\x32\x32.opentelemetry.proto.metrics.v1.HistogramDataPoint\x12W\n\x17\x61ggregation_temporality\x18\x02 \x01(\x0e\x32\x36.opentelemetry.proto.metrics.v1.AggregationTemporality\"\xc3\x01\n\x14\x45xponentialHistogram\x12R\n\x0b\x64\x61ta_points\x18\x01 \x03(\x0b\x32=.opentelemetry.proto.metrics.v1.ExponentialHistogramDataPoint\x12W\n\x17\x61ggregation_temporality\x18\x02 \x01(\x0e\x32\x36.opentelemetry.proto.metrics.v1.AggregationTemporality\"P\n\x07Summary\x12\x45\n\x0b\x64\x61ta_points\x18\x01 \x03(\x0b\x32\x30.opentelemetry.proto.metrics.v1.SummaryDataPoint\"\x86\x02\n\x0fNumberDataPoint\x12;\n\nattributes\x18\x07 \x03(\x0b\x32\'.opentelemetry.proto.common.v1.KeyValue\x12\x1c\n\x14start_time_unix_nano\x18\x02 \x01(\x06\x12\x16\n\x0etime_unix_nano\x18\x03 \x01(\x06\x12\x13\n\tas_double\x18\x04 \x01(\x01H\x00\x12\x10\n\x06\x61s_int\x18\x06 \x01(\x10H\x00\x12;\n\texemplars\x18\x05 \x03(\x0b\x32(.opentelemetry.proto.metrics.v1.Exemplar\x12\r\n\x05\x66lags\x18\x08 \x01(\rB\x07\n\x05valueJ\x04\x08\x01\x10\x02\"\xe6\x02\n\x12HistogramDataPoint\x12;\n\nattributes\x18\t \x03(\x0b\x32\'.opentelemetry.proto.common.v1.KeyValue\x12\x1c\n\x14start_time_unix_nano\x18\x02 \x01(\x06\x12\x16\n\x0etime_unix_nano\x18\x03 \x01(\x06\x12\r\n\x05\x63ount\x18\x04 \x01(\x06\x12\x10\n\x03sum\x18\x05 \x01(\x01H\x00\x88\x01\x01\x12\x15\n\rbucket_counts\x18\x06 \x03(\x06\x12\x17\n\x0f\x65xplicit_bounds\x18\x07 \x03(\x01\x12;\n\texemplars\x18\x08 \x03(\x0b\x32(.opentelemetry.proto.metrics.v1.Exemplar\x12\r\n\x05\x66lags\x18\n \x01(\r\x12\x10\n\x03min\x18\x0b \x01(\x01H\x01\x88\x01\x01\x12\x10\n\x03max\x18\x0c \x01(\x01H\x02\x88\x01\x01\x42\x06\n\x04_sumB\x06\n\x04_minB\x06\n\x04_maxJ\x04\x08\x01\x10\x02\"\xda\x04\n\x1d\x45xponentialHistogramDataPoint\x12;\n\nattributes\x18\x01 \x03(\x0b\x32\'.opentelemetry.proto.common.v1.KeyValue\x12\x1c\n\x14start_time_unix_nano\x18\x02 \x01(\x06\x12\x16\n\x0etime_unix_nano\x18\x03 \x01(\x06\x12\r\n\x05\x63ount\x18\x04 \x01(\x06\x12\x10\n\x03sum\x18\x05 \x01(\x01H\x00\x88\x01\x01\x12\r\n\x05scale\x18\x06 \x01(\x11\x12\x12\n\nzero_count\x18\x07 \x01(\x06\x12W\n\x08positive\x18\x08 \x01(\x0b\x32\x45.opentelemetry.proto.metrics.v1.ExponentialHistogramDataPoint.Buckets\x12W\n\x08negative\x18\t \x01(\x0b\x32\x45.opentelemetry.proto.metrics.v1.ExponentialHistogramDataPoint.Buckets\x12\r\n\x05\x66lags\x18\n \x01(\r\x12;\n\texemplars\x18\x0b \x03(\x0b\x32(.opentelemetry.proto.metrics.v1.Exemplar\x12\x10\n\x03min\x18\x0c \x01(\x01H\x01\x88\x01\x01\x12\x10\n\x03max\x18\r \x01(\x01H\x02\x88\x01\x01\x12\x16\n\x0ezero_threshold\x18\x0e \x01(\x01\x1a\x30\n\x07\x42uckets\x12\x0e\n\x06offset\x18\x01 \x01(\x11\x12\x15\n\rbucket_counts\x18\x02 \x03(\x04\x42\x06\n\x04_sumB\x06\n\x04_minB\x06\n\x04_max\"\xc5\x02\n\x10SummaryDataPoint\x12;\n\nattributes\x18\x07 \x03(\x0b\x32\'.opentelemetry.proto.common.v1.KeyValue\x12\x1c\n\x14start_time_unix_nano\x18\x02 \x01(\x06\x12\x16\n\x0etime_unix_nano\x18\x03 \x01(\x06\x12\r\n\x05\x63ount\x18\x04 \x01(\x06\x12\x0b\n\x03sum\x18\x05 \x01(\x01\x12Y\n\x0fquantile_values\x18\x06 \x03(\x0b\x32@.opentelemetry.proto.metrics.v1.SummaryDataPoint.ValueAtQuantile\x12\r\n\x05\x66lags\x18\x08 \x01(\r\x1a\x32\n\x0fValueAtQuantile\x12\x10\n\x08quantile\x18\x01 \x01(\x01\x12\r\n\x05value\x18\x02 \x01(\x01J\x04\x08\x01\x10\x02\"\xc1\x01\n\x08\x45xemplar\x12\x44\n\x13\x66iltered_attributes\x18\x07 \x03(\x0b\x32\'.opentelemetry.proto.common.v1.KeyValue\x12\x16\n\x0etime_unix_nano\x18\x02 \x01(\x06\x12\x13\n\tas_double\x18\x03 \x01(\x01H\x00\x12\x10\n\x06\x61s_int\x18\x06 \x01(\x10H\x00\x12\x0f\n\x07span_id\x18\x04 \x01(\x0c\x12\x10\n\x08trace_id\x18\x05 \x01(\x0c\x42\x07\n\x05valueJ\x04\x08\x01\x10\x02*\x8c\x01\n\x16\x41ggregationTemporality\x12\'\n#AGGREGATION_TEMPORALITY_UNSPECIFIED\x10\x00\x12!\n\x1d\x41GGREGATION_TEMPORALITY_DELTA\x10\x01\x12&\n\"AGGREGATION_TEMPORALITY_CUMULATIVE\x10\x02*^\n\x0e\x44\x61taPointFlags\x12\x1f\n\x1b\x44\x41TA_POINT_FLAGS_DO_NOT_USE\x10\x00\x12+\n\'DATA_POINT_FLAGS_NO_RECORDED_VALUE_MASK\x10\x01\x42\x7f\n!io.opentelemetry.proto.metrics.v1B\x0cMetricsProtoP\x01Z)go.opentelemetry.io/proto/otlp/metrics/v1\xaa\x02\x1eOpenTelemetry.Proto.Metrics.V1b\x06proto3')

_AGGREGATIONTEMPORALITY = DESCRIPTOR.enum_types_by_name['AggregationTemporality']
AggregationTemporality = enum_type_wrapper.EnumTypeWrapper(_AGGREGATIONTEMPORALITY)
_DATAPOINTFLAGS = DESCRIPTOR.enum_types_by_name['DataPointFlags']
DataPointFlags = enum_type_wrapper.EnumTypeWrapper(_DATAPOINTFLAGS)
AGGREGATION_TEMPORALITY_UNSPECIFIED = 0
AGGREGATION_TEMPORALITY_DELTA = 1
AGGREGATION_TEMPORALITY_CUMULATIVE = 2
DATA_POINT_FLAGS_DO_NOT_USE = 0
DATA_POINT_FLAGS_NO_RECORDED_VALUE_MASK = 1


_METRICSDATA = DESCRIPTOR.message_types_by_name['MetricsData']
_RESOURCEMETRICS = DESCRIPTOR.message_types_by_name['ResourceMetrics']
_SCOPEMETRICS = DESCRIPTOR.message_types_by_name['ScopeMetrics']
_METRIC = DESCRIPTOR.message_types_by_name['Metric']
_GAUGE = DESCRIPTOR.message_types_by_name['Gauge']
_SUM = DESCRIPTOR.message_types_by_name['Sum']
_HISTOGRAM = DESCRIPTOR.message_types_by_name['Histogram']
_EXPONENTIALHISTOGRAM = DESCRIPTOR.message_types_by_name['ExponentialHistogram']
_SUMMARY = DESCRIPTOR.message_types_by_name['Summary']
_NUMBERDATAPOINT = DESCRIPTOR.message_types_by_name['NumberDataPoint']
_HISTOGRAMDATAPOINT = DESCRIPTOR.message_types_by_name['HistogramDataPoint']
_EXPONENTIALHISTOGRAMDATAPOINT = DESCRIPTOR.message_types_by_name['ExponentialHistogramDataPoint']
_EXPONENTIALHISTOGRAMDATAPOINT_BUCKETS = _EXPONENTIALHISTOGRAMDATAPOINT.nested_types_by_name['Buckets']
_SUMMARYDATAPOINT = DESCRIPTOR.message_types_by_name['SummaryDataPoint']
_SUMMARYDATAPOINT_VALUEATQUANTILE = _SUMMARYDATAPOINT.nested_types_by_name['ValueAtQuantile']
_EXEMPLAR = DESCRIPTOR.message_types_by_name['Exemplar']
MetricsData = _reflection.GeneratedProtocolMessageType('MetricsData', (_message.Message,), {
  'DESCRIPTOR' : _METRICSDATA,
  '__module__' : 'opentelemetry.proto.metrics.v1.metrics_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.metrics.v1.MetricsData)
  })
_sym_db.RegisterMessage(MetricsData)

ResourceMetrics = _reflection.GeneratedProtocolMessageType('ResourceMetrics', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCEMETRICS,
  '__module__' : 'opentelemetry.proto.metrics.v1.metrics_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.metrics.v1.ResourceMetrics)
  })
_sym_db.RegisterMessage(ResourceMetrics)

ScopeMetrics = _reflection.GeneratedProtocolMessageType('ScopeMetrics', (_message.Message,), {
  'DESCRIPTOR' : _SCOPEMETRICS,
  '__module__' : 'opentelemetry.proto.metrics.v1.metrics_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.metrics.v1.ScopeMetrics)
  })
_sym_db.RegisterMessage(ScopeMetrics)

Metric = _reflection.GeneratedProtocolMessageType('Metric', (_message.Message,), {
  'DESCRIPTOR' : _METRIC,
  '__module__' : 'opentelemetry.proto.metrics.v1.metrics_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.metrics.v1.Metric)
  })
_sym_db.RegisterMessage(Metric)

Gauge = _reflection.GeneratedProtocolMessageType('Gauge', (_message.Message,), {
  'DESCRIPTOR' : _GAUGE,
  '__module__' : 'opentelemetry.proto.metrics.v1.metrics_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.metrics.v1.Gauge)
  })
_sym_db.RegisterMessage(Gauge)

Sum = _reflection.GeneratedProtocolMessageType('Sum', (_message.Message,), {
  'DESCRIPTOR' : _SUM,
  '__module__' : 'opentelemetry.proto.metrics.v1.metrics_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.metrics.v1.Sum)
  })
_sym_db.RegisterMessage(Sum)

Histogram = _reflection.GeneratedProtocolMessageType('Histogram', (_message.Message,), {
  'DESCRIPTOR' : _HISTOGRAM,
  '__module__' : 'opentelemetry.proto.metrics.v1.metrics_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.metrics.v1.Histogram)
  })
_sym_db.RegisterMessage(Histogram)

ExponentialHistogram = _reflection.GeneratedProtocolMessageType('ExponentialHistogram', (_message.Message,), {
  'DESCRIPTOR' : _EXPONENTIALHISTOGRAM,
  '__module__' : 'opentelemetry.proto.metrics.v1.metrics_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.metrics.v1.ExponentialHistogram)
  })
_sym_db.RegisterMessage(ExponentialHistogram)

Summary = _reflection.GeneratedProtocolMessageType('Summary', (_message.Message,), {
  'DESCRIPTOR' : _SUMMARY,
  '__module__' : 'opentelemetry.proto.metrics.v1.metrics_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.metrics.v1.Summary)
  })
_sym_db.RegisterMessage(Summary)

NumberDataPoint = _reflection.GeneratedProtocolMessageType('NumberDataPoint', (_message.Message,), {
  'DESCRIPTOR' : _NUMBERDATAPOINT,
  '__module__' : 'opentelemetry.proto.metrics.v1.metrics_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.metrics.v1.NumberDataPoint)
  })
_sym_db.RegisterMessage(NumberDataPoint)

HistogramDataPoint = _reflection.GeneratedProtocolMessageType('HistogramDataPoint', (_message.Message,), {
  'DESCRIPTOR' : _HISTOGRAMDATAPOINT,
  '__module__' : 'opentelemetry.proto.metrics.v1.metrics_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.metrics.v1.HistogramDataPoint)
  })
_sym_db.RegisterMessage(HistogramDataPoint)

ExponentialHistogramDataPoint = _reflection.GeneratedProtocolMessageType('ExponentialHistogramDataPoint', (_message.Message,), {

  'Buckets' : _reflection.GeneratedProtocolMessageType('Buckets', (_message.Message,), {
    'DESCRIPTOR' : _EXPONENTIALHISTOGRAMDATAPOINT_BUCKETS,
    '__module__' : 'opentelemetry.proto.metrics.v1.metrics_pb2'
    # @@protoc_insertion_point(class_scope:opentelemetry.proto.metrics.v1.ExponentialHistogramDataPoint.Buckets)
    })
  ,
  'DESCRIPTOR' : _EXPONENTIALHISTOGRAMDATAPOINT,
  '__module__' : 'opentelemetry.proto.metrics.v1.metrics_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.metrics.v1.ExponentialHistogramDataPoint)
  })
_sym_db.RegisterMessage(ExponentialHistogramDataPoint)
_sym_db.RegisterMessage(ExponentialHistogramDataPoint.Buckets)

SummaryDataPoint = _reflection.GeneratedProtocolMessageType('SummaryDataPoint', (_message.Message,), {

  'ValueAtQuantile' : _reflection.GeneratedProtocolMessageType('ValueAtQuantile', (_message.Message,), {
    'DESCRIPTOR' : _SUMMARYDATAPOINT_VALUEATQUANTILE,
    '__module__' : 'opentelemetry.proto.metrics.v1.metrics_pb2'
    # @@protoc_insertion_point(class_scope:opentelemetry.proto.metrics.v1.SummaryDataPoint.ValueAtQuantile)
    })
  ,
  'DESCRIPTOR' : _SUMMARYDATAPOINT,
  '__module__' : 'opentelemetry.proto.metrics.v1.metrics_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.metrics.v1.SummaryDataPoint)
  })
_sym_db.RegisterMessage(SummaryDataPoint)
_sym_db.RegisterMessage(SummaryDataPoint.ValueAtQuantile)

Exemplar = _reflection.GeneratedProtocolMessageType('Exemplar', (_message.Message,), {
  'DESCRIPTOR' : _EXEMPLAR,
  '__module__' : 'opentelemetry.proto.metrics.v1.metrics_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.metrics.v1.Exemplar)
  })
_sym_db.RegisterMessage(Exemplar)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!io.opentelemetry.proto.metrics.v1B\014MetricsProtoP\001Z)go.opentelemetry.io/proto/otlp/metrics/v1\252\002\036OpenTelemetry.Proto.Metrics.V1'
  _AGGREGATIONTEMPORALITY._serialized_start=3546
  _AGGREGATIONTEMPORALITY._serialized_end=3686
  _DATAPOINTFLAGS._serialized_start=3688
  _DATAPOINTFLAGS._serialized_end=3782
  _METRICSDATA._serialized_start=172
  _METRICSDATA._serialized_end=260
  _RESOURCEMETRICS._serialized_start=263
  _RESOURCEMETRICS._serialized_end=438
  _SCOPEMETRICS._serialized_start=441
  _SCOPEMETRICS._serialized_end=600
  _METRIC._serialized_start=603
  _METRIC._serialized_end=1064
  _GAUGE._serialized_start=1066
  _GAUGE._serialized_end=1143
  _SUM._serialized_start=1146
  _SUM._serialized_end=1332
  _HISTOGRAM._serialized_start=1335
  _HISTOGRAM._serialized_end=1508
  _EXPONENTIALHISTOGRAM._serialized_start=1511
  _EXPONENTIALHISTOGRAM._serialized_end=1706
  _SUMMARY._serialized_start=1708
  _SUMMARY._serialized_end=1788
  _NUMBERDATAPOINT._serialized_start=1791
  _NUMBERDATAPOINT._serialized_end=2053
  _HISTOGRAMDATAPOINT._serialized_start=2056
  _HISTOGRAMDATAPOINT._serialized_end=2414
  _EXPONENTIALHISTOGRAMDATAPOINT._serialized_start=2417
  _EXPONENTIALHISTOGRAMDATAPOINT._serialized_end=3019
  _EXPONENTIALHISTOGRAMDATAPOINT_BUCKETS._serialized_start=2947
  _EXPONENTIALHISTOGRAMDATAPOINT_BUCKETS._serialized_end=2995
  _SUMMARYDATAPOINT._serialized_start=3022
  _SUMMARYDATAPOINT._serialized_end=3347
  _SUMMARYDATAPOINT_VALUEATQUANTILE._serialized_start=3291
  _SUMMARYDATAPOINT_VALUEATQUANTILE._serialized_end=3341
  _EXEMPLAR._serialized_start=3350
  _EXEMPLAR._serialized_end=3543
# @@protoc_insertion_point(module_scope)
