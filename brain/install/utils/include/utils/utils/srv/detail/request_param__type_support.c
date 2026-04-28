// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from utils:srv/RequestParam.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "utils/srv/detail/request_param__rosidl_typesupport_introspection_c.h"
#include "utils/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "utils/srv/detail/request_param__functions.h"
#include "utils/srv/detail/request_param__struct.h"


// Include directives for member types
// Member `name`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void utils__srv__RequestParam_Request__rosidl_typesupport_introspection_c__RequestParam_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  utils__srv__RequestParam_Request__init(message_memory);
}

void utils__srv__RequestParam_Request__rosidl_typesupport_introspection_c__RequestParam_Request_fini_function(void * message_memory)
{
  utils__srv__RequestParam_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember utils__srv__RequestParam_Request__rosidl_typesupport_introspection_c__RequestParam_Request_message_member_array[1] = {
  {
    "name",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(utils__srv__RequestParam_Request, name),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers utils__srv__RequestParam_Request__rosidl_typesupport_introspection_c__RequestParam_Request_message_members = {
  "utils__srv",  // message namespace
  "RequestParam_Request",  // message name
  1,  // number of fields
  sizeof(utils__srv__RequestParam_Request),
  false,  // has_any_key_member_
  utils__srv__RequestParam_Request__rosidl_typesupport_introspection_c__RequestParam_Request_message_member_array,  // message members
  utils__srv__RequestParam_Request__rosidl_typesupport_introspection_c__RequestParam_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  utils__srv__RequestParam_Request__rosidl_typesupport_introspection_c__RequestParam_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t utils__srv__RequestParam_Request__rosidl_typesupport_introspection_c__RequestParam_Request_message_type_support_handle = {
  0,
  &utils__srv__RequestParam_Request__rosidl_typesupport_introspection_c__RequestParam_Request_message_members,
  get_message_typesupport_handle_function,
  &utils__srv__RequestParam_Request__get_type_hash,
  &utils__srv__RequestParam_Request__get_type_description,
  &utils__srv__RequestParam_Request__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_utils
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, utils, srv, RequestParam_Request)() {
  if (!utils__srv__RequestParam_Request__rosidl_typesupport_introspection_c__RequestParam_Request_message_type_support_handle.typesupport_identifier) {
    utils__srv__RequestParam_Request__rosidl_typesupport_introspection_c__RequestParam_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &utils__srv__RequestParam_Request__rosidl_typesupport_introspection_c__RequestParam_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "utils/srv/detail/request_param__rosidl_typesupport_introspection_c.h"
// already included above
// #include "utils/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "utils/srv/detail/request_param__functions.h"
// already included above
// #include "utils/srv/detail/request_param__struct.h"


// Include directives for member types
// Member `ints`
// Member `floats`
#include "rosidl_runtime_c/primitives_sequence_functions.h"
// Member `strings`
// already included above
// #include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__RequestParam_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  utils__srv__RequestParam_Response__init(message_memory);
}

void utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__RequestParam_Response_fini_function(void * message_memory)
{
  utils__srv__RequestParam_Response__fini(message_memory);
}

size_t utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__size_function__RequestParam_Response__ints(
  const void * untyped_member)
{
  const rosidl_runtime_c__int32__Sequence * member =
    (const rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return member->size;
}

const void * utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__get_const_function__RequestParam_Response__ints(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__int32__Sequence * member =
    (const rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return &member->data[index];
}

void * utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__get_function__RequestParam_Response__ints(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__int32__Sequence * member =
    (rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return &member->data[index];
}

void utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__fetch_function__RequestParam_Response__ints(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const int32_t * item =
    ((const int32_t *)
    utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__get_const_function__RequestParam_Response__ints(untyped_member, index));
  int32_t * value =
    (int32_t *)(untyped_value);
  *value = *item;
}

void utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__assign_function__RequestParam_Response__ints(
  void * untyped_member, size_t index, const void * untyped_value)
{
  int32_t * item =
    ((int32_t *)
    utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__get_function__RequestParam_Response__ints(untyped_member, index));
  const int32_t * value =
    (const int32_t *)(untyped_value);
  *item = *value;
}

bool utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__resize_function__RequestParam_Response__ints(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__int32__Sequence * member =
    (rosidl_runtime_c__int32__Sequence *)(untyped_member);
  rosidl_runtime_c__int32__Sequence__fini(member);
  return rosidl_runtime_c__int32__Sequence__init(member, size);
}

size_t utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__size_function__RequestParam_Response__floats(
  const void * untyped_member)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return member->size;
}

const void * utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__get_const_function__RequestParam_Response__floats(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void * utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__get_function__RequestParam_Response__floats(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__fetch_function__RequestParam_Response__floats(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const float * item =
    ((const float *)
    utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__get_const_function__RequestParam_Response__floats(untyped_member, index));
  float * value =
    (float *)(untyped_value);
  *value = *item;
}

void utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__assign_function__RequestParam_Response__floats(
  void * untyped_member, size_t index, const void * untyped_value)
{
  float * item =
    ((float *)
    utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__get_function__RequestParam_Response__floats(untyped_member, index));
  const float * value =
    (const float *)(untyped_value);
  *item = *value;
}

bool utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__resize_function__RequestParam_Response__floats(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  rosidl_runtime_c__float__Sequence__fini(member);
  return rosidl_runtime_c__float__Sequence__init(member, size);
}

size_t utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__size_function__RequestParam_Response__strings(
  const void * untyped_member)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return member->size;
}

const void * utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__get_const_function__RequestParam_Response__strings(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void * utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__get_function__RequestParam_Response__strings(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__fetch_function__RequestParam_Response__strings(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const rosidl_runtime_c__String * item =
    ((const rosidl_runtime_c__String *)
    utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__get_const_function__RequestParam_Response__strings(untyped_member, index));
  rosidl_runtime_c__String * value =
    (rosidl_runtime_c__String *)(untyped_value);
  *value = *item;
}

void utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__assign_function__RequestParam_Response__strings(
  void * untyped_member, size_t index, const void * untyped_value)
{
  rosidl_runtime_c__String * item =
    ((rosidl_runtime_c__String *)
    utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__get_function__RequestParam_Response__strings(untyped_member, index));
  const rosidl_runtime_c__String * value =
    (const rosidl_runtime_c__String *)(untyped_value);
  *item = *value;
}

bool utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__resize_function__RequestParam_Response__strings(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  rosidl_runtime_c__String__Sequence__fini(member);
  return rosidl_runtime_c__String__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__RequestParam_Response_message_member_array[3] = {
  {
    "ints",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(utils__srv__RequestParam_Response, ints),  // bytes offset in struct
    NULL,  // default value
    utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__size_function__RequestParam_Response__ints,  // size() function pointer
    utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__get_const_function__RequestParam_Response__ints,  // get_const(index) function pointer
    utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__get_function__RequestParam_Response__ints,  // get(index) function pointer
    utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__fetch_function__RequestParam_Response__ints,  // fetch(index, &value) function pointer
    utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__assign_function__RequestParam_Response__ints,  // assign(index, value) function pointer
    utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__resize_function__RequestParam_Response__ints  // resize(index) function pointer
  },
  {
    "floats",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(utils__srv__RequestParam_Response, floats),  // bytes offset in struct
    NULL,  // default value
    utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__size_function__RequestParam_Response__floats,  // size() function pointer
    utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__get_const_function__RequestParam_Response__floats,  // get_const(index) function pointer
    utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__get_function__RequestParam_Response__floats,  // get(index) function pointer
    utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__fetch_function__RequestParam_Response__floats,  // fetch(index, &value) function pointer
    utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__assign_function__RequestParam_Response__floats,  // assign(index, value) function pointer
    utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__resize_function__RequestParam_Response__floats  // resize(index) function pointer
  },
  {
    "strings",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(utils__srv__RequestParam_Response, strings),  // bytes offset in struct
    NULL,  // default value
    utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__size_function__RequestParam_Response__strings,  // size() function pointer
    utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__get_const_function__RequestParam_Response__strings,  // get_const(index) function pointer
    utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__get_function__RequestParam_Response__strings,  // get(index) function pointer
    utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__fetch_function__RequestParam_Response__strings,  // fetch(index, &value) function pointer
    utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__assign_function__RequestParam_Response__strings,  // assign(index, value) function pointer
    utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__resize_function__RequestParam_Response__strings  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__RequestParam_Response_message_members = {
  "utils__srv",  // message namespace
  "RequestParam_Response",  // message name
  3,  // number of fields
  sizeof(utils__srv__RequestParam_Response),
  false,  // has_any_key_member_
  utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__RequestParam_Response_message_member_array,  // message members
  utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__RequestParam_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__RequestParam_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__RequestParam_Response_message_type_support_handle = {
  0,
  &utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__RequestParam_Response_message_members,
  get_message_typesupport_handle_function,
  &utils__srv__RequestParam_Response__get_type_hash,
  &utils__srv__RequestParam_Response__get_type_description,
  &utils__srv__RequestParam_Response__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_utils
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, utils, srv, RequestParam_Response)() {
  if (!utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__RequestParam_Response_message_type_support_handle.typesupport_identifier) {
    utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__RequestParam_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__RequestParam_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "utils/srv/detail/request_param__rosidl_typesupport_introspection_c.h"
// already included above
// #include "utils/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "utils/srv/detail/request_param__functions.h"
// already included above
// #include "utils/srv/detail/request_param__struct.h"


// Include directives for member types
// Member `info`
#include "service_msgs/msg/service_event_info.h"
// Member `info`
#include "service_msgs/msg/detail/service_event_info__rosidl_typesupport_introspection_c.h"
// Member `request`
// Member `response`
#include "utils/srv/request_param.h"
// Member `request`
// Member `response`
// already included above
// #include "utils/srv/detail/request_param__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__RequestParam_Event_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  utils__srv__RequestParam_Event__init(message_memory);
}

void utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__RequestParam_Event_fini_function(void * message_memory)
{
  utils__srv__RequestParam_Event__fini(message_memory);
}

size_t utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__size_function__RequestParam_Event__request(
  const void * untyped_member)
{
  const utils__srv__RequestParam_Request__Sequence * member =
    (const utils__srv__RequestParam_Request__Sequence *)(untyped_member);
  return member->size;
}

const void * utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__get_const_function__RequestParam_Event__request(
  const void * untyped_member, size_t index)
{
  const utils__srv__RequestParam_Request__Sequence * member =
    (const utils__srv__RequestParam_Request__Sequence *)(untyped_member);
  return &member->data[index];
}

void * utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__get_function__RequestParam_Event__request(
  void * untyped_member, size_t index)
{
  utils__srv__RequestParam_Request__Sequence * member =
    (utils__srv__RequestParam_Request__Sequence *)(untyped_member);
  return &member->data[index];
}

void utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__fetch_function__RequestParam_Event__request(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const utils__srv__RequestParam_Request * item =
    ((const utils__srv__RequestParam_Request *)
    utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__get_const_function__RequestParam_Event__request(untyped_member, index));
  utils__srv__RequestParam_Request * value =
    (utils__srv__RequestParam_Request *)(untyped_value);
  *value = *item;
}

void utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__assign_function__RequestParam_Event__request(
  void * untyped_member, size_t index, const void * untyped_value)
{
  utils__srv__RequestParam_Request * item =
    ((utils__srv__RequestParam_Request *)
    utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__get_function__RequestParam_Event__request(untyped_member, index));
  const utils__srv__RequestParam_Request * value =
    (const utils__srv__RequestParam_Request *)(untyped_value);
  *item = *value;
}

bool utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__resize_function__RequestParam_Event__request(
  void * untyped_member, size_t size)
{
  utils__srv__RequestParam_Request__Sequence * member =
    (utils__srv__RequestParam_Request__Sequence *)(untyped_member);
  utils__srv__RequestParam_Request__Sequence__fini(member);
  return utils__srv__RequestParam_Request__Sequence__init(member, size);
}

size_t utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__size_function__RequestParam_Event__response(
  const void * untyped_member)
{
  const utils__srv__RequestParam_Response__Sequence * member =
    (const utils__srv__RequestParam_Response__Sequence *)(untyped_member);
  return member->size;
}

const void * utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__get_const_function__RequestParam_Event__response(
  const void * untyped_member, size_t index)
{
  const utils__srv__RequestParam_Response__Sequence * member =
    (const utils__srv__RequestParam_Response__Sequence *)(untyped_member);
  return &member->data[index];
}

void * utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__get_function__RequestParam_Event__response(
  void * untyped_member, size_t index)
{
  utils__srv__RequestParam_Response__Sequence * member =
    (utils__srv__RequestParam_Response__Sequence *)(untyped_member);
  return &member->data[index];
}

void utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__fetch_function__RequestParam_Event__response(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const utils__srv__RequestParam_Response * item =
    ((const utils__srv__RequestParam_Response *)
    utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__get_const_function__RequestParam_Event__response(untyped_member, index));
  utils__srv__RequestParam_Response * value =
    (utils__srv__RequestParam_Response *)(untyped_value);
  *value = *item;
}

void utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__assign_function__RequestParam_Event__response(
  void * untyped_member, size_t index, const void * untyped_value)
{
  utils__srv__RequestParam_Response * item =
    ((utils__srv__RequestParam_Response *)
    utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__get_function__RequestParam_Event__response(untyped_member, index));
  const utils__srv__RequestParam_Response * value =
    (const utils__srv__RequestParam_Response *)(untyped_value);
  *item = *value;
}

bool utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__resize_function__RequestParam_Event__response(
  void * untyped_member, size_t size)
{
  utils__srv__RequestParam_Response__Sequence * member =
    (utils__srv__RequestParam_Response__Sequence *)(untyped_member);
  utils__srv__RequestParam_Response__Sequence__fini(member);
  return utils__srv__RequestParam_Response__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__RequestParam_Event_message_member_array[3] = {
  {
    "info",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(utils__srv__RequestParam_Event, info),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "request",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    true,  // is array
    1,  // array size
    true,  // is upper bound
    offsetof(utils__srv__RequestParam_Event, request),  // bytes offset in struct
    NULL,  // default value
    utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__size_function__RequestParam_Event__request,  // size() function pointer
    utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__get_const_function__RequestParam_Event__request,  // get_const(index) function pointer
    utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__get_function__RequestParam_Event__request,  // get(index) function pointer
    utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__fetch_function__RequestParam_Event__request,  // fetch(index, &value) function pointer
    utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__assign_function__RequestParam_Event__request,  // assign(index, value) function pointer
    utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__resize_function__RequestParam_Event__request  // resize(index) function pointer
  },
  {
    "response",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    true,  // is array
    1,  // array size
    true,  // is upper bound
    offsetof(utils__srv__RequestParam_Event, response),  // bytes offset in struct
    NULL,  // default value
    utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__size_function__RequestParam_Event__response,  // size() function pointer
    utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__get_const_function__RequestParam_Event__response,  // get_const(index) function pointer
    utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__get_function__RequestParam_Event__response,  // get(index) function pointer
    utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__fetch_function__RequestParam_Event__response,  // fetch(index, &value) function pointer
    utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__assign_function__RequestParam_Event__response,  // assign(index, value) function pointer
    utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__resize_function__RequestParam_Event__response  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__RequestParam_Event_message_members = {
  "utils__srv",  // message namespace
  "RequestParam_Event",  // message name
  3,  // number of fields
  sizeof(utils__srv__RequestParam_Event),
  false,  // has_any_key_member_
  utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__RequestParam_Event_message_member_array,  // message members
  utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__RequestParam_Event_init_function,  // function to initialize message memory (memory has to be allocated)
  utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__RequestParam_Event_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__RequestParam_Event_message_type_support_handle = {
  0,
  &utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__RequestParam_Event_message_members,
  get_message_typesupport_handle_function,
  &utils__srv__RequestParam_Event__get_type_hash,
  &utils__srv__RequestParam_Event__get_type_description,
  &utils__srv__RequestParam_Event__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_utils
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, utils, srv, RequestParam_Event)() {
  utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__RequestParam_Event_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_msgs, msg, ServiceEventInfo)();
  utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__RequestParam_Event_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, utils, srv, RequestParam_Request)();
  utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__RequestParam_Event_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, utils, srv, RequestParam_Response)();
  if (!utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__RequestParam_Event_message_type_support_handle.typesupport_identifier) {
    utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__RequestParam_Event_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__RequestParam_Event_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "utils/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "utils/srv/detail/request_param__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers utils__srv__detail__request_param__rosidl_typesupport_introspection_c__RequestParam_service_members = {
  "utils__srv",  // service namespace
  "RequestParam",  // service name
  // the following fields are initialized below on first access
  NULL,  // request message
  // utils__srv__detail__request_param__rosidl_typesupport_introspection_c__RequestParam_Request_message_type_support_handle,
  NULL,  // response message
  // utils__srv__detail__request_param__rosidl_typesupport_introspection_c__RequestParam_Response_message_type_support_handle
  NULL  // event_message
  // utils__srv__detail__request_param__rosidl_typesupport_introspection_c__RequestParam_Response_message_type_support_handle
};


static rosidl_service_type_support_t utils__srv__detail__request_param__rosidl_typesupport_introspection_c__RequestParam_service_type_support_handle = {
  0,
  &utils__srv__detail__request_param__rosidl_typesupport_introspection_c__RequestParam_service_members,
  get_service_typesupport_handle_function,
  &utils__srv__RequestParam_Request__rosidl_typesupport_introspection_c__RequestParam_Request_message_type_support_handle,
  &utils__srv__RequestParam_Response__rosidl_typesupport_introspection_c__RequestParam_Response_message_type_support_handle,
  &utils__srv__RequestParam_Event__rosidl_typesupport_introspection_c__RequestParam_Event_message_type_support_handle,
  ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_CREATE_EVENT_MESSAGE_SYMBOL_NAME(
    rosidl_typesupport_c,
    utils,
    srv,
    RequestParam
  ),
  ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_DESTROY_EVENT_MESSAGE_SYMBOL_NAME(
    rosidl_typesupport_c,
    utils,
    srv,
    RequestParam
  ),
  &utils__srv__RequestParam__get_type_hash,
  &utils__srv__RequestParam__get_type_description,
  &utils__srv__RequestParam__get_type_description_sources,
};

// Forward declaration of message type support functions for service members
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, utils, srv, RequestParam_Request)(void);

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, utils, srv, RequestParam_Response)(void);

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, utils, srv, RequestParam_Event)(void);

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_utils
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, utils, srv, RequestParam)(void) {
  if (!utils__srv__detail__request_param__rosidl_typesupport_introspection_c__RequestParam_service_type_support_handle.typesupport_identifier) {
    utils__srv__detail__request_param__rosidl_typesupport_introspection_c__RequestParam_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)utils__srv__detail__request_param__rosidl_typesupport_introspection_c__RequestParam_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, utils, srv, RequestParam_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, utils, srv, RequestParam_Response)()->data;
  }
  if (!service_members->event_members_) {
    service_members->event_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, utils, srv, RequestParam_Event)()->data;
  }

  return &utils__srv__detail__request_param__rosidl_typesupport_introspection_c__RequestParam_service_type_support_handle;
}
