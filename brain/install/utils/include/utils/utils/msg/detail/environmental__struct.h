// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from utils:msg/Environmental.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/environmental.h"


#ifndef UTILS__MSG__DETAIL__ENVIRONMENTAL__STRUCT_H_
#define UTILS__MSG__DETAIL__ENVIRONMENTAL__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Struct defined in msg/Environmental in the package utils.
typedef struct utils__msg__Environmental
{
  uint8_t obstacle_id;
  float x;
  float y;
} utils__msg__Environmental;

// Struct for a sequence of utils__msg__Environmental.
typedef struct utils__msg__Environmental__Sequence
{
  utils__msg__Environmental * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} utils__msg__Environmental__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // UTILS__MSG__DETAIL__ENVIRONMENTAL__STRUCT_H_
