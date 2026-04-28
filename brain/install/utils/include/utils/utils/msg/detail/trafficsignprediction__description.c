// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from utils:msg/Trafficsignprediction.idl
// generated code does not contain a copyright notice

#include "utils/msg/detail/trafficsignprediction__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_utils
const rosidl_type_hash_t *
utils__msg__Trafficsignprediction__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x34, 0xda, 0x56, 0x76, 0x3d, 0x81, 0x2d, 0xfd,
      0x96, 0x62, 0xf7, 0x6b, 0x79, 0xe1, 0xdb, 0x50,
      0xa7, 0xc9, 0x6a, 0xe1, 0x45, 0xb4, 0xbf, 0x19,
      0x82, 0x61, 0xce, 0x17, 0x7d, 0xf9, 0x7a, 0x41,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char utils__msg__Trafficsignprediction__TYPE_NAME[] = "utils/msg/Trafficsignprediction";

// Define type names, field names, and default values
static char utils__msg__Trafficsignprediction__FIELD_NAME__prediction[] = "prediction";
static char utils__msg__Trafficsignprediction__FIELD_NAME__conf[] = "conf";

static rosidl_runtime_c__type_description__Field utils__msg__Trafficsignprediction__FIELDS[] = {
  {
    {utils__msg__Trafficsignprediction__FIELD_NAME__prediction, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__Trafficsignprediction__FIELD_NAME__conf, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
utils__msg__Trafficsignprediction__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {utils__msg__Trafficsignprediction__TYPE_NAME, 31, 31},
      {utils__msg__Trafficsignprediction__FIELDS, 2, 2},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "string prediction\n"
  "float32 conf";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
utils__msg__Trafficsignprediction__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {utils__msg__Trafficsignprediction__TYPE_NAME, 31, 31},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 30, 30},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
utils__msg__Trafficsignprediction__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *utils__msg__Trafficsignprediction__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
