// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from utils:msg/Vehicles.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "utils/msg/detail/vehicles__rosidl_typesupport_introspection_c.h"
#include "utils/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "utils/msg/detail/vehicles__functions.h"
#include "utils/msg/detail/vehicles__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void utils__msg__Vehicles__rosidl_typesupport_introspection_c__Vehicles_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  utils__msg__Vehicles__init(message_memory);
}

void utils__msg__Vehicles__rosidl_typesupport_introspection_c__Vehicles_fini_function(void * message_memory)
{
  utils__msg__Vehicles__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember utils__msg__Vehicles__rosidl_typesupport_introspection_c__Vehicles_message_member_array[6] = {
  {
    "id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(utils__msg__Vehicles, id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "timestamp",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(utils__msg__Vehicles, timestamp),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "pos_a",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(utils__msg__Vehicles, pos_a),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "pos_b",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(utils__msg__Vehicles, pos_b),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "rot_a",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(utils__msg__Vehicles, rot_a),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "rot_b",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(utils__msg__Vehicles, rot_b),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers utils__msg__Vehicles__rosidl_typesupport_introspection_c__Vehicles_message_members = {
  "utils__msg",  // message namespace
  "Vehicles",  // message name
  6,  // number of fields
  sizeof(utils__msg__Vehicles),
  false,  // has_any_key_member_
  utils__msg__Vehicles__rosidl_typesupport_introspection_c__Vehicles_message_member_array,  // message members
  utils__msg__Vehicles__rosidl_typesupport_introspection_c__Vehicles_init_function,  // function to initialize message memory (memory has to be allocated)
  utils__msg__Vehicles__rosidl_typesupport_introspection_c__Vehicles_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t utils__msg__Vehicles__rosidl_typesupport_introspection_c__Vehicles_message_type_support_handle = {
  0,
  &utils__msg__Vehicles__rosidl_typesupport_introspection_c__Vehicles_message_members,
  get_message_typesupport_handle_function,
  &utils__msg__Vehicles__get_type_hash,
  &utils__msg__Vehicles__get_type_description,
  &utils__msg__Vehicles__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_utils
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, utils, msg, Vehicles)() {
  if (!utils__msg__Vehicles__rosidl_typesupport_introspection_c__Vehicles_message_type_support_handle.typesupport_identifier) {
    utils__msg__Vehicles__rosidl_typesupport_introspection_c__Vehicles_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &utils__msg__Vehicles__rosidl_typesupport_introspection_c__Vehicles_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
