// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from utils:msg/Environmental.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "utils/msg/detail/environmental__functions.h"
#include "utils/msg/detail/environmental__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace utils
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void Environmental_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) utils::msg::Environmental(_init);
}

void Environmental_fini_function(void * message_memory)
{
  auto typed_message = static_cast<utils::msg::Environmental *>(message_memory);
  typed_message->~Environmental();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember Environmental_message_member_array[3] = {
  {
    "obstacle_id",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(utils::msg::Environmental, obstacle_id),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "x",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(utils::msg::Environmental, x),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "y",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(utils::msg::Environmental, y),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers Environmental_message_members = {
  "utils::msg",  // message namespace
  "Environmental",  // message name
  3,  // number of fields
  sizeof(utils::msg::Environmental),
  false,  // has_any_key_member_
  Environmental_message_member_array,  // message members
  Environmental_init_function,  // function to initialize message memory (memory has to be allocated)
  Environmental_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t Environmental_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &Environmental_message_members,
  get_message_typesupport_handle_function,
  &utils__msg__Environmental__get_type_hash,
  &utils__msg__Environmental__get_type_description,
  &utils__msg__Environmental__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace utils


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<utils::msg::Environmental>()
{
  return &::utils::msg::rosidl_typesupport_introspection_cpp::Environmental_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, utils, msg, Environmental)() {
  return &::utils::msg::rosidl_typesupport_introspection_cpp::Environmental_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
