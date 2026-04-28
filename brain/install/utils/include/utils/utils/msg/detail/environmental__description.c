// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from utils:msg/Environmental.idl
// generated code does not contain a copyright notice

#include "utils/msg/detail/environmental__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_utils
const rosidl_type_hash_t *
utils__msg__Environmental__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x17, 0x8a, 0x23, 0x55, 0x94, 0x16, 0x16, 0x89,
      0x50, 0x6a, 0x33, 0xdf, 0xac, 0x91, 0x10, 0x95,
      0x84, 0xce, 0x94, 0x3c, 0x70, 0xc9, 0xab, 0x26,
      0xa7, 0x28, 0xb6, 0xfc, 0xb4, 0x5c, 0x3c, 0x6d,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char utils__msg__Environmental__TYPE_NAME[] = "utils/msg/Environmental";

// Define type names, field names, and default values
static char utils__msg__Environmental__FIELD_NAME__obstacle_id[] = "obstacle_id";
static char utils__msg__Environmental__FIELD_NAME__x[] = "x";
static char utils__msg__Environmental__FIELD_NAME__y[] = "y";

static rosidl_runtime_c__type_description__Field utils__msg__Environmental__FIELDS[] = {
  {
    {utils__msg__Environmental__FIELD_NAME__obstacle_id, 11, 11},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT8,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__Environmental__FIELD_NAME__x, 1, 1},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__Environmental__FIELD_NAME__y, 1, 1},
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
utils__msg__Environmental__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {utils__msg__Environmental__TYPE_NAME, 23, 23},
      {utils__msg__Environmental__FIELDS, 3, 3},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "uint8 obstacle_id\n"
  "float32 x\n"
  "float32 y";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
utils__msg__Environmental__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {utils__msg__Environmental__TYPE_NAME, 23, 23},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 37, 37},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
utils__msg__Environmental__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *utils__msg__Environmental__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
