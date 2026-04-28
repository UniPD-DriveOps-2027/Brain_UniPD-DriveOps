// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from utils:msg/Localisation.idl
// generated code does not contain a copyright notice

#include "utils/msg/detail/localisation__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_utils
const rosidl_type_hash_t *
utils__msg__Localisation__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xf4, 0x0a, 0x18, 0x4f, 0x2c, 0xae, 0x1c, 0x99,
      0xf9, 0x33, 0xe4, 0xd8, 0x94, 0x36, 0x0b, 0x5e,
      0x1e, 0x12, 0x41, 0x8e, 0xdb, 0x04, 0x82, 0xe6,
      0x65, 0x1f, 0x52, 0xd1, 0xa1, 0x8e, 0x36, 0xad,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char utils__msg__Localisation__TYPE_NAME[] = "utils/msg/Localisation";

// Define type names, field names, and default values
static char utils__msg__Localisation__FIELD_NAME__timestamp[] = "timestamp";
static char utils__msg__Localisation__FIELD_NAME__pos_a[] = "pos_a";
static char utils__msg__Localisation__FIELD_NAME__pos_b[] = "pos_b";
static char utils__msg__Localisation__FIELD_NAME__rot_a[] = "rot_a";
static char utils__msg__Localisation__FIELD_NAME__rot_b[] = "rot_b";

static rosidl_runtime_c__type_description__Field utils__msg__Localisation__FIELDS[] = {
  {
    {utils__msg__Localisation__FIELD_NAME__timestamp, 9, 9},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__Localisation__FIELD_NAME__pos_a, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__Localisation__FIELD_NAME__pos_b, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__Localisation__FIELD_NAME__rot_a, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__Localisation__FIELD_NAME__rot_b, 5, 5},
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
utils__msg__Localisation__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {utils__msg__Localisation__TYPE_NAME, 22, 22},
      {utils__msg__Localisation__FIELDS, 5, 5},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "float64 timestamp\n"
  "float32 pos_a\n"
  "float32 pos_b\n"
  "float32 rot_a\n"
  "float32 rot_b";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
utils__msg__Localisation__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {utils__msg__Localisation__TYPE_NAME, 22, 22},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 74, 74},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
utils__msg__Localisation__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *utils__msg__Localisation__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
