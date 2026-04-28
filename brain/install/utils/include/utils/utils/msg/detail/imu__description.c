// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from utils:msg/IMU.idl
// generated code does not contain a copyright notice

#include "utils/msg/detail/imu__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_utils
const rosidl_type_hash_t *
utils__msg__IMU__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xc8, 0xd1, 0x89, 0xf2, 0x7c, 0x89, 0xf1, 0x45,
      0x51, 0x30, 0x5e, 0xd1, 0x73, 0x28, 0x98, 0x41,
      0xf6, 0x31, 0xff, 0xd0, 0xef, 0x8c, 0xfe, 0xf3,
      0x5b, 0x00, 0xe9, 0x4f, 0x7d, 0x75, 0x80, 0x3a,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char utils__msg__IMU__TYPE_NAME[] = "utils/msg/IMU";

// Define type names, field names, and default values
static char utils__msg__IMU__FIELD_NAME__roll[] = "roll";
static char utils__msg__IMU__FIELD_NAME__pitch[] = "pitch";
static char utils__msg__IMU__FIELD_NAME__yaw[] = "yaw";
static char utils__msg__IMU__FIELD_NAME__accelx[] = "accelx";
static char utils__msg__IMU__FIELD_NAME__accely[] = "accely";
static char utils__msg__IMU__FIELD_NAME__accelz[] = "accelz";
static char utils__msg__IMU__FIELD_NAME__gyrox[] = "gyrox";
static char utils__msg__IMU__FIELD_NAME__gyroy[] = "gyroy";
static char utils__msg__IMU__FIELD_NAME__gyroz[] = "gyroz";

static rosidl_runtime_c__type_description__Field utils__msg__IMU__FIELDS[] = {
  {
    {utils__msg__IMU__FIELD_NAME__roll, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__IMU__FIELD_NAME__pitch, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__IMU__FIELD_NAME__yaw, 3, 3},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__IMU__FIELD_NAME__accelx, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__IMU__FIELD_NAME__accely, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__IMU__FIELD_NAME__accelz, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__IMU__FIELD_NAME__gyrox, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__IMU__FIELD_NAME__gyroy, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {utils__msg__IMU__FIELD_NAME__gyroz, 5, 5},
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
utils__msg__IMU__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {utils__msg__IMU__TYPE_NAME, 13, 13},
      {utils__msg__IMU__FIELDS, 9, 9},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "float32 roll\n"
  "float32 pitch\n"
  "float32 yaw\n"
  "float32 accelx\n"
  "float32 accely\n"
  "float32 accelz\n"
  "float32 gyrox\n"
  "float32 gyroy\n"
  "float32 gyroz";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
utils__msg__IMU__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {utils__msg__IMU__TYPE_NAME, 13, 13},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 126, 126},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
utils__msg__IMU__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *utils__msg__IMU__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
