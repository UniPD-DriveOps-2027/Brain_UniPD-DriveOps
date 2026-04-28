// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from utils:msg/Log.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/log.h"


#ifndef UTILS__MSG__DETAIL__LOG__STRUCT_H_
#define UTILS__MSG__DETAIL__LOG__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Constant 'ROSDEBUG'.
/**
  * ROS Logging Levels
 */
enum
{
  utils__msg__Log__ROSDEBUG = 0
};

/// Constant 'INFO'.
enum
{
  utils__msg__Log__INFO = 1
};

/// Constant 'WARN'.
enum
{
  utils__msg__Log__WARN = 2
};

/// Constant 'ERROR'.
enum
{
  utils__msg__Log__ERROR = 3
};

/// Constant 'FATAL'.
enum
{
  utils__msg__Log__FATAL = 4
};

// Include directives for member types
// Member 'msg'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/Log in the package utils.
typedef struct utils__msg__Log
{
  uint8_t level;
  rosidl_runtime_c__String msg;
} utils__msg__Log;

// Struct for a sequence of utils__msg__Log.
typedef struct utils__msg__Log__Sequence
{
  utils__msg__Log * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} utils__msg__Log__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // UTILS__MSG__DETAIL__LOG__STRUCT_H_
