// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from utils:msg/Log.idl
// generated code does not contain a copyright notice

#include "utils/msg/detail/log__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_utils
const rosidl_type_hash_t *
utils__msg__Log__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xba, 0x3c, 0x03, 0xaf, 0xe7, 0xd9, 0x72, 0x09,
      0xc8, 0x94, 0x72, 0x7b, 0xe8, 0xf5, 0x28, 0x82,
      0xab, 0x45, 0x0c, 0xd3, 0xe6, 0x9c, 0xe2, 0x17,
      0xe0, 0xfa, 0xd4, 0xe4, 0x71, 0xe9, 0x0f, 0xb1,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char utils__msg__Log__TYPE_NAME[] = "utils/msg/Log";

// Define type names, field names, and default values
static char utils__msg__Log__FIELD_NAME__level[] = "level";
static char utils__msg__Log__FIELD_NAME__msg[] = "msg";

static rosidl_runtime_c__type_description__Field utils__msg__Log__FIELDS[] = {
  {
    {utils__msg__Log__FIELD_NAME__level, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT8,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__Log__FIELD_NAME__msg, 3, 3},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
utils__msg__Log__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {utils__msg__Log__TYPE_NAME, 13, 13},
      {utils__msg__Log__FIELDS, 2, 2},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "\n"
  "#ROS Logging Levels\n"
  "uint8 ROSDEBUG=0\n"
  "uint8 INFO=1\n"
  "uint8 WARN=2\n"
  "uint8 ERROR=3\n"
  "uint8 FATAL=4\n"
  "\n"
  "uint8 level\n"
  "string msg";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
utils__msg__Log__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {utils__msg__Log__TYPE_NAME, 13, 13},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 116, 116},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
utils__msg__Log__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *utils__msg__Log__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
