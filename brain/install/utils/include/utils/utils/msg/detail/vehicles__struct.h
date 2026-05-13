// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from utils:msg/Vehicles.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/vehicles.h"


#ifndef UTILS__MSG__DETAIL__VEHICLES__STRUCT_H_
#define UTILS__MSG__DETAIL__VEHICLES__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Struct defined in msg/Vehicles in the package utils.
typedef struct utils__msg__Vehicles
{
  uint8_t id;
  float timestamp;
  float pos_a;
  float pos_b;
  float rot_a;
  float rot_b;
} utils__msg__Vehicles;

// Struct for a sequence of utils__msg__Vehicles.
typedef struct utils__msg__Vehicles__Sequence
{
  utils__msg__Vehicles * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} utils__msg__Vehicles__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // UTILS__MSG__DETAIL__VEHICLES__STRUCT_H_
