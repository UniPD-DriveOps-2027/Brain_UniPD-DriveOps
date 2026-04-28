// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from utils:msg/TopicInfo.idl
// generated code does not contain a copyright notice

#include "utils/msg/detail/topic_info__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_utils
const rosidl_type_hash_t *
utils__msg__TopicInfo__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xe6, 0x5f, 0x05, 0xe2, 0x22, 0xae, 0x3c, 0x22,
      0x2f, 0x5b, 0x22, 0xd8, 0x3a, 0x14, 0xd0, 0xc2,
      0xe5, 0xb6, 0xda, 0xbf, 0x17, 0xf6, 0x05, 0x8c,
      0xb9, 0xb9, 0x40, 0xf6, 0x92, 0xd6, 0x86, 0x70,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char utils__msg__TopicInfo__TYPE_NAME[] = "utils/msg/TopicInfo";

// Define type names, field names, and default values
static char utils__msg__TopicInfo__FIELD_NAME__topic_id[] = "topic_id";
static char utils__msg__TopicInfo__FIELD_NAME__topic_name[] = "topic_name";
static char utils__msg__TopicInfo__FIELD_NAME__message_type[] = "message_type";
static char utils__msg__TopicInfo__FIELD_NAME__md5sum[] = "md5sum";
static char utils__msg__TopicInfo__FIELD_NAME__buffer_size[] = "buffer_size";

static rosidl_runtime_c__type_description__Field utils__msg__TopicInfo__FIELDS[] = {
  {
    {utils__msg__TopicInfo__FIELD_NAME__topic_id, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_UINT16,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__TopicInfo__FIELD_NAME__topic_name, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__TopicInfo__FIELD_NAME__message_type, 12, 12},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__TopicInfo__FIELD_NAME__md5sum, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__TopicInfo__FIELD_NAME__buffer_size, 11, 11},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
utils__msg__TopicInfo__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {utils__msg__TopicInfo__TYPE_NAME, 19, 19},
      {utils__msg__TopicInfo__FIELDS, 5, 5},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "# special topic_ids\n"
  "uint16 ID_PUBLISHER=0\n"
  "uint16 ID_SUBSCRIBER=1\n"
  "uint16 ID_SERVICE_SERVER=2\n"
  "uint16 ID_SERVICE_CLIENT=4\n"
  "uint16 ID_PARAMETER_REQUEST=6\n"
  "uint16 ID_LOG=7\n"
  "uint16 ID_TIME=10\n"
  "uint16 ID_TX_STOP=11\n"
  "\n"
  "# The endpoint ID for this topic\n"
  "uint16 topic_id\n"
  "\n"
  "string topic_name\n"
  "string message_type\n"
  "\n"
  "# MD5 checksum for this message type\n"
  "string md5sum\n"
  "\n"
  "# size of the buffer message must fit in\n"
  "int32 buffer_size";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
utils__msg__TopicInfo__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {utils__msg__TopicInfo__TYPE_NAME, 19, 19},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 405, 405},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
utils__msg__TopicInfo__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *utils__msg__TopicInfo__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
