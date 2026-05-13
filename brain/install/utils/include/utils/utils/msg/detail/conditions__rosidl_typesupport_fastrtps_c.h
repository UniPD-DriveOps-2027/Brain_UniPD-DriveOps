// generated from rosidl_typesupport_fastrtps_c/resource/idl__rosidl_typesupport_fastrtps_c.h.em
// with input from utils:msg/Conditions.idl
// generated code does not contain a copyright notice
#ifndef UTILS__MSG__DETAIL__CONDITIONS__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
#define UTILS__MSG__DETAIL__CONDITIONS__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_


#include <stddef.h>
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "utils/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "utils/msg/detail/conditions__struct.h"
#include "fastcdr/Cdr.h"

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_utils
bool cdr_serialize_utils__msg__Conditions(
  const utils__msg__Conditions * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_utils
bool cdr_deserialize_utils__msg__Conditions(
  eprosima::fastcdr::Cdr &,
  utils__msg__Conditions * ros_message);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_utils
size_t get_serialized_size_utils__msg__Conditions(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_utils
size_t max_serialized_size_utils__msg__Conditions(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_utils
bool cdr_serialize_key_utils__msg__Conditions(
  const utils__msg__Conditions * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_utils
size_t get_serialized_size_key_utils__msg__Conditions(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_utils
size_t max_serialized_size_key_utils__msg__Conditions(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_utils
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, utils, msg, Conditions)();

#ifdef __cplusplus
}
#endif

#endif  // UTILS__MSG__DETAIL__CONDITIONS__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
