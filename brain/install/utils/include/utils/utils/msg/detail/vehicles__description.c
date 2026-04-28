// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from utils:msg/Vehicles.idl
// generated code does not contain a copyright notice

#include "utils/msg/detail/vehicles__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_utils
const rosidl_type_hash_t *
utils__msg__Vehicles__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x2d, 0xf9, 0x4b, 0xc1, 0x1b, 0xee, 0xc2, 0xde,
      0x5f, 0xc0, 0x62, 0xe4, 0xca, 0xee, 0x8e, 0xe4,
      0x52, 0x9c, 0x71, 0xe1, 0x2c, 0x37, 0xfd, 0xf1,
      0x4c, 0x06, 0x27, 0x7c, 0x4f, 0x28, 0x2f, 0xc2,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char utils__msg__Vehicles__TYPE_NAME[] = "utils/msg/Vehicles";

// Define type names, field names, and default values
static char utils__msg__Vehicles__FIELD_NAME__id[] = "id";
static char utils__msg__Vehicles__FIELD_NAME__timestamp[] = "timestamp";
static char utils__msg__Vehicles__FIELD_NAME__pos_a[] = "pos_a";
static char utils__msg__Vehicles__FIELD_NAME__pos_b[] = "pos_b";
static char utils__msg__Vehicles__FIELD_NAME__rot_a[] = "rot_a";
static char utils__msg__Vehicles__FIELD_NAME__rot_b[] = "rot_b";

static rosidl_runtime_c__type_description__Field utils__msg__Vehicles__FIELDS[] = {
  {
    {utils__msg__Vehicles__FIELD_NAME__id, 2, 2},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT8,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__Vehicles__FIELD_NAME__timestamp, 9, 9},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__Vehicles__FIELD_NAME__pos_a, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__Vehicles__FIELD_NAME__pos_b, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__Vehicles__FIELD_NAME__rot_a, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__Vehicles__FIELD_NAME__rot_b, 5, 5},
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
utils__msg__Vehicles__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {utils__msg__Vehicles__TYPE_NAME, 18, 18},
      {utils__msg__Vehicles__FIELDS, 6, 6},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "uint8 id\n"
  "float32 timestamp\n"
  "float32 pos_a\n"
  "float32 pos_b\n"
  "float32 rot_a\n"
  "float32 rot_b";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
utils__msg__Vehicles__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {utils__msg__Vehicles__TYPE_NAME, 18, 18},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 83, 83},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
utils__msg__Vehicles__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *utils__msg__Vehicles__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
