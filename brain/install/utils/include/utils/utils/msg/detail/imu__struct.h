// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from utils:msg/IMU.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/imu.h"


#ifndef UTILS__MSG__DETAIL__IMU__STRUCT_H_
#define UTILS__MSG__DETAIL__IMU__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Struct defined in msg/IMU in the package utils.
typedef struct utils__msg__IMU
{
  float roll;
  float pitch;
  float yaw;
  float accelx;
  float accely;
  float accelz;
  float gyrox;
  float gyroy;
  float gyroz;
} utils__msg__IMU;

// Struct for a sequence of utils__msg__IMU.
typedef struct utils__msg__IMU__Sequence
{
  utils__msg__IMU * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} utils__msg__IMU__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // UTILS__MSG__DETAIL__IMU__STRUCT_H_
