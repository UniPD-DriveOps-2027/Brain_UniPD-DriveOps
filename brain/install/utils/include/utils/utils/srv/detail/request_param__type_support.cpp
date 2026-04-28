// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from utils:srv/RequestParam.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "utils/srv/detail/request_param__functions.h"
#include "utils/srv/detail/request_param__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace utils
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

void RequestParam_Request_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) utils::srv::RequestParam_Request(_init);
}

void RequestParam_Request_fini_function(void * message_memory)
{
  auto typed_message = static_cast<utils::srv::RequestParam_Request *>(message_memory);
  typed_message->~RequestParam_Request();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember RequestParam_Request_message_member_array[1] = {
  {
    "name",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(utils::srv::RequestParam_Request, name),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers RequestParam_Request_message_members = {
  "utils::srv",  // message namespace
  "RequestParam_Request",  // message name
  1,  // number of fields
  sizeof(utils::srv::RequestParam_Request),
  false,  // has_any_key_member_
  RequestParam_Request_message_member_array,  // message members
  RequestParam_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  RequestParam_Request_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t RequestParam_Request_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &RequestParam_Request_message_members,
  get_message_typesupport_handle_function,
  &utils__srv__RequestParam_Request__get_type_hash,
  &utils__srv__RequestParam_Request__get_type_description,
  &utils__srv__RequestParam_Request__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace utils


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<utils::srv::RequestParam_Request>()
{
  return &::utils::srv::rosidl_typesupport_introspection_cpp::RequestParam_Request_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, utils, srv, RequestParam_Request)() {
  return &::utils::srv::rosidl_typesupport_introspection_cpp::RequestParam_Request_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "array"
// already included above
// #include "cstddef"
// already included above
// #include "string"
// already included above
// #include "vector"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
// already included above
// #include "utils/srv/detail/request_param__functions.h"
// already included above
// #include "utils/srv/detail/request_param__struct.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/field_types.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace utils
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

void RequestParam_Response_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) utils::srv::RequestParam_Response(_init);
}

void RequestParam_Response_fini_function(void * message_memory)
{
  auto typed_message = static_cast<utils::srv::RequestParam_Response *>(message_memory);
  typed_message->~RequestParam_Response();
}

size_t size_function__RequestParam_Response__ints(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return member->size();
}

const void * get_const_function__RequestParam_Response__ints(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void * get_function__RequestParam_Response__ints(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void fetch_function__RequestParam_Response__ints(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const int32_t *>(
    get_const_function__RequestParam_Response__ints(untyped_member, index));
  auto & value = *reinterpret_cast<int32_t *>(untyped_value);
  value = item;
}

void assign_function__RequestParam_Response__ints(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<int32_t *>(
    get_function__RequestParam_Response__ints(untyped_member, index));
  const auto & value = *reinterpret_cast<const int32_t *>(untyped_value);
  item = value;
}

void resize_function__RequestParam_Response__ints(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  member->resize(size);
}

size_t size_function__RequestParam_Response__floats(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<float> *>(untyped_member);
  return member->size();
}

const void * get_const_function__RequestParam_Response__floats(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<float> *>(untyped_member);
  return &member[index];
}

void * get_function__RequestParam_Response__floats(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<float> *>(untyped_member);
  return &member[index];
}

void fetch_function__RequestParam_Response__floats(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const float *>(
    get_const_function__RequestParam_Response__floats(untyped_member, index));
  auto & value = *reinterpret_cast<float *>(untyped_value);
  value = item;
}

void assign_function__RequestParam_Response__floats(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<float *>(
    get_function__RequestParam_Response__floats(untyped_member, index));
  const auto & value = *reinterpret_cast<const float *>(untyped_value);
  item = value;
}

void resize_function__RequestParam_Response__floats(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<float> *>(untyped_member);
  member->resize(size);
}

size_t size_function__RequestParam_Response__strings(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return member->size();
}

const void * get_const_function__RequestParam_Response__strings(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void * get_function__RequestParam_Response__strings(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void fetch_function__RequestParam_Response__strings(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const std::string *>(
    get_const_function__RequestParam_Response__strings(untyped_member, index));
  auto & value = *reinterpret_cast<std::string *>(untyped_value);
  value = item;
}

void assign_function__RequestParam_Response__strings(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<std::string *>(
    get_function__RequestParam_Response__strings(untyped_member, index));
  const auto & value = *reinterpret_cast<const std::string *>(untyped_value);
  item = value;
}

void resize_function__RequestParam_Response__strings(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<std::string> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember RequestParam_Response_message_member_array[3] = {
  {
    "ints",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(utils::srv::RequestParam_Response, ints),  // bytes offset in struct
    nullptr,  // default value
    size_function__RequestParam_Response__ints,  // size() function pointer
    get_const_function__RequestParam_Response__ints,  // get_const(index) function pointer
    get_function__RequestParam_Response__ints,  // get(index) function pointer
    fetch_function__RequestParam_Response__ints,  // fetch(index, &value) function pointer
    assign_function__RequestParam_Response__ints,  // assign(index, value) function pointer
    resize_function__RequestParam_Response__ints  // resize(index) function pointer
  },
  {
    "floats",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(utils::srv::RequestParam_Response, floats),  // bytes offset in struct
    nullptr,  // default value
    size_function__RequestParam_Response__floats,  // size() function pointer
    get_const_function__RequestParam_Response__floats,  // get_const(index) function pointer
    get_function__RequestParam_Response__floats,  // get(index) function pointer
    fetch_function__RequestParam_Response__floats,  // fetch(index, &value) function pointer
    assign_function__RequestParam_Response__floats,  // assign(index, value) function pointer
    resize_function__RequestParam_Response__floats  // resize(index) function pointer
  },
  {
    "strings",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(utils::srv::RequestParam_Response, strings),  // bytes offset in struct
    nullptr,  // default value
    size_function__RequestParam_Response__strings,  // size() function pointer
    get_const_function__RequestParam_Response__strings,  // get_const(index) function pointer
    get_function__RequestParam_Response__strings,  // get(index) function pointer
    fetch_function__RequestParam_Response__strings,  // fetch(index, &value) function pointer
    assign_function__RequestParam_Response__strings,  // assign(index, value) function pointer
    resize_function__RequestParam_Response__strings  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers RequestParam_Response_message_members = {
  "utils::srv",  // message namespace
  "RequestParam_Response",  // message name
  3,  // number of fields
  sizeof(utils::srv::RequestParam_Response),
  false,  // has_any_key_member_
  RequestParam_Response_message_member_array,  // message members
  RequestParam_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  RequestParam_Response_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t RequestParam_Response_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &RequestParam_Response_message_members,
  get_message_typesupport_handle_function,
  &utils__srv__RequestParam_Response__get_type_hash,
  &utils__srv__RequestParam_Response__get_type_description,
  &utils__srv__RequestParam_Response__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace utils


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<utils::srv::RequestParam_Response>()
{
  return &::utils::srv::rosidl_typesupport_introspection_cpp::RequestParam_Response_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, utils, srv, RequestParam_Response)() {
  return &::utils::srv::rosidl_typesupport_introspection_cpp::RequestParam_Response_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "array"
// already included above
// #include "cstddef"
// already included above
// #include "string"
// already included above
// #include "vector"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
// already included above
// #include "utils/srv/detail/request_param__functions.h"
// already included above
// #include "utils/srv/detail/request_param__struct.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/field_types.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace utils
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

void RequestParam_Event_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) utils::srv::RequestParam_Event(_init);
}

void RequestParam_Event_fini_function(void * message_memory)
{
  auto typed_message = static_cast<utils::srv::RequestParam_Event *>(message_memory);
  typed_message->~RequestParam_Event();
}

size_t size_function__RequestParam_Event__request(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<utils::srv::RequestParam_Request> *>(untyped_member);
  return member->size();
}

const void * get_const_function__RequestParam_Event__request(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<utils::srv::RequestParam_Request> *>(untyped_member);
  return &member[index];
}

void * get_function__RequestParam_Event__request(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<utils::srv::RequestParam_Request> *>(untyped_member);
  return &member[index];
}

void fetch_function__RequestParam_Event__request(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const utils::srv::RequestParam_Request *>(
    get_const_function__RequestParam_Event__request(untyped_member, index));
  auto & value = *reinterpret_cast<utils::srv::RequestParam_Request *>(untyped_value);
  value = item;
}

void assign_function__RequestParam_Event__request(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<utils::srv::RequestParam_Request *>(
    get_function__RequestParam_Event__request(untyped_member, index));
  const auto & value = *reinterpret_cast<const utils::srv::RequestParam_Request *>(untyped_value);
  item = value;
}

void resize_function__RequestParam_Event__request(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<utils::srv::RequestParam_Request> *>(untyped_member);
  member->resize(size);
}

size_t size_function__RequestParam_Event__response(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<utils::srv::RequestParam_Response> *>(untyped_member);
  return member->size();
}

const void * get_const_function__RequestParam_Event__response(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<utils::srv::RequestParam_Response> *>(untyped_member);
  return &member[index];
}

void * get_function__RequestParam_Event__response(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<utils::srv::RequestParam_Response> *>(untyped_member);
  return &member[index];
}

void fetch_function__RequestParam_Event__response(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const utils::srv::RequestParam_Response *>(
    get_const_function__RequestParam_Event__response(untyped_member, index));
  auto & value = *reinterpret_cast<utils::srv::RequestParam_Response *>(untyped_value);
  value = item;
}

void assign_function__RequestParam_Event__response(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<utils::srv::RequestParam_Response *>(
    get_function__RequestParam_Event__response(untyped_member, index));
  const auto & value = *reinterpret_cast<const utils::srv::RequestParam_Response *>(untyped_value);
  item = value;
}

void resize_function__RequestParam_Event__response(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<utils::srv::RequestParam_Response> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember RequestParam_Event_message_member_array[3] = {
  {
    "info",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<service_msgs::msg::ServiceEventInfo>(),  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(utils::srv::RequestParam_Event, info),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "request",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<utils::srv::RequestParam_Request>(),  // members of sub message
    false,  // is key
    true,  // is array
    1,  // array size
    true,  // is upper bound
    offsetof(utils::srv::RequestParam_Event, request),  // bytes offset in struct
    nullptr,  // default value
    size_function__RequestParam_Event__request,  // size() function pointer
    get_const_function__RequestParam_Event__request,  // get_const(index) function pointer
    get_function__RequestParam_Event__request,  // get(index) function pointer
    fetch_function__RequestParam_Event__request,  // fetch(index, &value) function pointer
    assign_function__RequestParam_Event__request,  // assign(index, value) function pointer
    resize_function__RequestParam_Event__request  // resize(index) function pointer
  },
  {
    "response",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<utils::srv::RequestParam_Response>(),  // members of sub message
    false,  // is key
    true,  // is array
    1,  // array size
    true,  // is upper bound
    offsetof(utils::srv::RequestParam_Event, response),  // bytes offset in struct
    nullptr,  // default value
    size_function__RequestParam_Event__response,  // size() function pointer
    get_const_function__RequestParam_Event__response,  // get_const(index) function pointer
    get_function__RequestParam_Event__response,  // get(index) function pointer
    fetch_function__RequestParam_Event__response,  // fetch(index, &value) function pointer
    assign_function__RequestParam_Event__response,  // assign(index, value) function pointer
    resize_function__RequestParam_Event__response  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers RequestParam_Event_message_members = {
  "utils::srv",  // message namespace
  "RequestParam_Event",  // message name
  3,  // number of fields
  sizeof(utils::srv::RequestParam_Event),
  false,  // has_any_key_member_
  RequestParam_Event_message_member_array,  // message members
  RequestParam_Event_init_function,  // function to initialize message memory (memory has to be allocated)
  RequestParam_Event_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t RequestParam_Event_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &RequestParam_Event_message_members,
  get_message_typesupport_handle_function,
  &utils__srv__RequestParam_Event__get_type_hash,
  &utils__srv__RequestParam_Event__get_type_description,
  &utils__srv__RequestParam_Event__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace utils


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<utils::srv::RequestParam_Event>()
{
  return &::utils::srv::rosidl_typesupport_introspection_cpp::RequestParam_Event_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, utils, srv, RequestParam_Event)() {
  return &::utils::srv::rosidl_typesupport_introspection_cpp::RequestParam_Event_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
// already included above
// #include "rosidl_typesupport_introspection_cpp/visibility_control.h"
// already included above
// #include "utils/srv/detail/request_param__functions.h"
// already included above
// #include "utils/srv/detail/request_param__struct.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/service_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/service_type_support_decl.hpp"

namespace utils
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

// this is intentionally not const to allow initialization later to prevent an initialization race
static ::rosidl_typesupport_introspection_cpp::ServiceMembers RequestParam_service_members = {
  "utils::srv",  // service namespace
  "RequestParam",  // service name
  // the following fields are initialized below on first access
  // see get_service_type_support_handle<utils::srv::RequestParam>()
  nullptr,  // request message
  nullptr,  // response message
  nullptr,  // event message
};

static const rosidl_service_type_support_t RequestParam_service_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &RequestParam_service_members,
  get_service_typesupport_handle_function,
  ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<utils::srv::RequestParam_Request>(),
  ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<utils::srv::RequestParam_Response>(),
  ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<utils::srv::RequestParam_Event>(),
  &::rosidl_typesupport_cpp::service_create_event_message<utils::srv::RequestParam>,
  &::rosidl_typesupport_cpp::service_destroy_event_message<utils::srv::RequestParam>,
  &utils__srv__RequestParam__get_type_hash,
  &utils__srv__RequestParam__get_type_description,
  &utils__srv__RequestParam__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace utils


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<utils::srv::RequestParam>()
{
  // get a handle to the value to be returned
  auto service_type_support =
    &::utils::srv::rosidl_typesupport_introspection_cpp::RequestParam_service_type_support_handle;
  // get a non-const and properly typed version of the data void *
  auto service_members = const_cast<::rosidl_typesupport_introspection_cpp::ServiceMembers *>(
    static_cast<const ::rosidl_typesupport_introspection_cpp::ServiceMembers *>(
      service_type_support->data));
  // make sure all of the service_members are initialized
  // if they are not, initialize them
  if (
    service_members->request_members_ == nullptr ||
    service_members->response_members_ == nullptr ||
    service_members->event_members_ == nullptr)
  {
    // initialize the request_members_ with the static function from the external library
    service_members->request_members_ = static_cast<
      const ::rosidl_typesupport_introspection_cpp::MessageMembers *
      >(
      ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<
        ::utils::srv::RequestParam_Request
      >()->data
      );
    // initialize the response_members_ with the static function from the external library
    service_members->response_members_ = static_cast<
      const ::rosidl_typesupport_introspection_cpp::MessageMembers *
      >(
      ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<
        ::utils::srv::RequestParam_Response
      >()->data
      );
    // initialize the event_members_ with the static function from the external library
    service_members->event_members_ = static_cast<
      const ::rosidl_typesupport_introspection_cpp::MessageMembers *
      >(
      ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<
        ::utils::srv::RequestParam_Event
      >()->data
      );
  }
  // finally return the properly initialized service_type_support handle
  return service_type_support;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, utils, srv, RequestParam)() {
  return ::rosidl_typesupport_introspection_cpp::get_service_type_support_handle<utils::srv::RequestParam>();
}

#ifdef __cplusplus
}
#endif
