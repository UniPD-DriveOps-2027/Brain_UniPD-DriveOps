// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from utils:msg/TopicInfo.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/topic_info.h"


#ifndef UTILS__MSG__DETAIL__TOPIC_INFO__STRUCT_H_
#define UTILS__MSG__DETAIL__TOPIC_INFO__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Constant 'ID_PUBLISHER'.
enum
{
  utils__msg__TopicInfo__ID_PUBLISHER = 0
};

/// Constant 'ID_SUBSCRIBER'.
enum
{
  utils__msg__TopicInfo__ID_SUBSCRIBER = 1
};

/// Constant 'ID_SERVICE_SERVER'.
enum
{
  utils__msg__TopicInfo__ID_SERVICE_SERVER = 2
};

/// Constant 'ID_SERVICE_CLIENT'.
enum
{
  utils__msg__TopicInfo__ID_SERVICE_CLIENT = 4
};

/// Constant 'ID_PARAMETER_REQUEST'.
enum
{
  utils__msg__TopicInfo__ID_PARAMETER_REQUEST = 6
};

/// Constant 'ID_LOG'.
enum
{
  utils__msg__TopicInfo__ID_LOG = 7
};

/// Constant 'ID_TIME'.
enum
{
  utils__msg__TopicInfo__ID_TIME = 10
};

/// Constant 'ID_TX_STOP'.
enum
{
  utils__msg__TopicInfo__ID_TX_STOP = 11
};

// Include directives for member types
// Member 'topic_name'
// Member 'message_type'
// Member 'md5sum'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/TopicInfo in the package utils.
/**
  * special topic_ids
 */
typedef struct utils__msg__TopicInfo
{
  /// The endpoint ID for this topic
  uint16_t topic_id;
  rosidl_runtime_c__String topic_name;
  rosidl_runtime_c__String message_type;
  /// MD5 checksum for this message type
  rosidl_runtime_c__String md5sum;
  /// size of the buffer message must fit in
  int32_t buffer_size;
} utils__msg__TopicInfo;

// Struct for a sequence of utils__msg__TopicInfo.
typedef struct utils__msg__TopicInfo__Sequence
{
  utils__msg__TopicInfo * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} utils__msg__TopicInfo__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // UTILS__MSG__DETAIL__TOPIC_INFO__STRUCT_H_
