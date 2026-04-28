// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from utils:msg/Conditions.idl
// generated code does not contain a copyright notice

#include "utils/msg/detail/conditions__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_utils
const rosidl_type_hash_t *
utils__msg__Conditions__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x4c, 0xb0, 0xd6, 0xb4, 0xc4, 0x6a, 0xed, 0xd1,
      0x2c, 0xdb, 0x0a, 0x6b, 0xf6, 0x10, 0x0c, 0xe8,
      0x8b, 0x6b, 0x4f, 0xe4, 0x44, 0x8f, 0x69, 0x16,
      0xb4, 0xc7, 0xfa, 0x97, 0xc6, 0x2a, 0x05, 0x78,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char utils__msg__Conditions__TYPE_NAME[] = "utils/msg/Conditions";

// Define type names, field names, and default values
static char utils__msg__Conditions__FIELD_NAME__can_overtake[] = "can_overtake";
static char utils__msg__Conditions__FIELD_NAME__highway[] = "highway";
static char utils__msg__Conditions__FIELD_NAME__car_on_path[] = "car_on_path";
static char utils__msg__Conditions__FIELD_NAME__rerouting[] = "rerouting";
static char utils__msg__Conditions__FIELD_NAME__tunnel[] = "tunnel";

static rosidl_runtime_c__type_description__Field utils__msg__Conditions__FIELDS[] = {
  {
    {utils__msg__Conditions__FIELD_NAME__can_overtake, 12, 12},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__Conditions__FIELD_NAME__highway, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__Conditions__FIELD_NAME__car_on_path, 11, 11},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__Conditions__FIELD_NAME__rerouting, 9, 9},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__Conditions__FIELD_NAME__tunnel, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
utils__msg__Conditions__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {utils__msg__Conditions__TYPE_NAME, 20, 20},
      {utils__msg__Conditions__FIELDS, 5, 5},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "bool can_overtake\n"
  "bool highway\n"
  "bool car_on_path\n"
  "bool rerouting\n"
  "bool tunnel";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
utils__msg__Conditions__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {utils__msg__Conditions__TYPE_NAME, 20, 20},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 74, 74},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
utils__msg__Conditions__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *utils__msg__Conditions__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
