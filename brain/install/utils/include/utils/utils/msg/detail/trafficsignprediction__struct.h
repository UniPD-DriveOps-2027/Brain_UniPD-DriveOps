// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from utils:msg/Trafficsignprediction.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/trafficsignprediction.h"


#ifndef UTILS__MSG__DETAIL__TRAFFICSIGNPREDICTION__STRUCT_H_
#define UTILS__MSG__DETAIL__TRAFFICSIGNPREDICTION__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

// Include directives for member types
// Member 'prediction'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/Trafficsignprediction in the package utils.
typedef struct utils__msg__Trafficsignprediction
{
  rosidl_runtime_c__String prediction;
  float conf;
} utils__msg__Trafficsignprediction;

// Struct for a sequence of utils__msg__Trafficsignprediction.
typedef struct utils__msg__Trafficsignprediction__Sequence
{
  utils__msg__Trafficsignprediction * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} utils__msg__Trafficsignprediction__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // UTILS__MSG__DETAIL__TRAFFICSIGNPREDICTION__STRUCT_H_
