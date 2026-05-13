// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from utils:msg/Semaphore.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/semaphore.h"


#ifndef UTILS__MSG__DETAIL__SEMAPHORE__STRUCT_H_
#define UTILS__MSG__DETAIL__SEMAPHORE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Struct defined in msg/Semaphore in the package utils.
typedef struct utils__msg__Semaphore
{
  uint8_t state;
  float pos_x;
  float pos_y;
} utils__msg__Semaphore;

// Struct for a sequence of utils__msg__Semaphore.
typedef struct utils__msg__Semaphore__Sequence
{
  utils__msg__Semaphore * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} utils__msg__Semaphore__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // UTILS__MSG__DETAIL__SEMAPHORE__STRUCT_H_
