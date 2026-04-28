// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from utils:msg/Semaphore.idl
// generated code does not contain a copyright notice

#include "utils/msg/detail/semaphore__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_utils
const rosidl_type_hash_t *
utils__msg__Semaphore__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xb2, 0xf9, 0xd6, 0x92, 0x85, 0x9f, 0x6c, 0x8b,
      0xab, 0x2d, 0xb8, 0x50, 0xc6, 0x1d, 0x30, 0xa8,
      0x97, 0xbf, 0xd3, 0xfa, 0x0e, 0x5d, 0x34, 0x7f,
      0x5e, 0x3c, 0xa0, 0xa5, 0xc4, 0xb5, 0x78, 0xaa,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char utils__msg__Semaphore__TYPE_NAME[] = "utils/msg/Semaphore";

// Define type names, field names, and default values
static char utils__msg__Semaphore__FIELD_NAME__state[] = "state";
static char utils__msg__Semaphore__FIELD_NAME__pos_x[] = "pos_x";
static char utils__msg__Semaphore__FIELD_NAME__pos_y[] = "pos_y";

static rosidl_runtime_c__type_description__Field utils__msg__Semaphore__FIELDS[] = {
  {
    {utils__msg__Semaphore__FIELD_NAME__state, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT8,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__Semaphore__FIELD_NAME__pos_x, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__Semaphore__FIELD_NAME__pos_y, 5, 5},
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
utils__msg__Semaphore__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {utils__msg__Semaphore__TYPE_NAME, 19, 19},
      {utils__msg__Semaphore__FIELDS, 3, 3},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "uint8 state\n"
  "float32 pos_x\n"
  "float32 pos_y";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
utils__msg__Semaphore__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {utils__msg__Semaphore__TYPE_NAME, 19, 19},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 39, 39},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
utils__msg__Semaphore__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *utils__msg__Semaphore__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
