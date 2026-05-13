// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from utils:msg/Conditions.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/conditions.h"


#ifndef UTILS__MSG__DETAIL__CONDITIONS__STRUCT_H_
#define UTILS__MSG__DETAIL__CONDITIONS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Struct defined in msg/Conditions in the package utils.
typedef struct utils__msg__Conditions
{
  bool can_overtake;
  bool highway;
  bool car_on_path;
  bool rerouting;
  bool tunnel;
} utils__msg__Conditions;

// Struct for a sequence of utils__msg__Conditions.
typedef struct utils__msg__Conditions__Sequence
{
  utils__msg__Conditions * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} utils__msg__Conditions__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // UTILS__MSG__DETAIL__CONDITIONS__STRUCT_H_
