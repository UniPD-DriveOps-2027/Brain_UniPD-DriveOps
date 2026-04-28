// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from utils:srv/RequestParam.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/srv/request_param.hpp"


#ifndef UTILS__SRV__DETAIL__REQUEST_PARAM__BUILDER_HPP_
#define UTILS__SRV__DETAIL__REQUEST_PARAM__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "utils/srv/detail/request_param__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace utils
{

namespace srv
{

namespace builder
{

class Init_RequestParam_Request_name
{
public:
  Init_RequestParam_Request_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::utils::srv::RequestParam_Request name(::utils::srv::RequestParam_Request::_name_type arg)
  {
    msg_.name = std::move(arg);
    return std::move(msg_);
  }

private:
  ::utils::srv::RequestParam_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::utils::srv::RequestParam_Request>()
{
  return utils::srv::builder::Init_RequestParam_Request_name();
}

}  // namespace utils


namespace utils
{

namespace srv
{

namespace builder
{

class Init_RequestParam_Response_strings
{
public:
  explicit Init_RequestParam_Response_strings(::utils::srv::RequestParam_Response & msg)
  : msg_(msg)
  {}
  ::utils::srv::RequestParam_Response strings(::utils::srv::RequestParam_Response::_strings_type arg)
  {
    msg_.strings = std::move(arg);
    return std::move(msg_);
  }

private:
  ::utils::srv::RequestParam_Response msg_;
};

class Init_RequestParam_Response_floats
{
public:
  explicit Init_RequestParam_Response_floats(::utils::srv::RequestParam_Response & msg)
  : msg_(msg)
  {}
  Init_RequestParam_Response_strings floats(::utils::srv::RequestParam_Response::_floats_type arg)
  {
    msg_.floats = std::move(arg);
    return Init_RequestParam_Response_strings(msg_);
  }

private:
  ::utils::srv::RequestParam_Response msg_;
};

class Init_RequestParam_Response_ints
{
public:
  Init_RequestParam_Response_ints()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RequestParam_Response_floats ints(::utils::srv::RequestParam_Response::_ints_type arg)
  {
    msg_.ints = std::move(arg);
    return Init_RequestParam_Response_floats(msg_);
  }

private:
  ::utils::srv::RequestParam_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::utils::srv::RequestParam_Response>()
{
  return utils::srv::builder::Init_RequestParam_Response_ints();
}

}  // namespace utils


namespace utils
{

namespace srv
{

namespace builder
{

class Init_RequestParam_Event_response
{
public:
  explicit Init_RequestParam_Event_response(::utils::srv::RequestParam_Event & msg)
  : msg_(msg)
  {}
  ::utils::srv::RequestParam_Event response(::utils::srv::RequestParam_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::utils::srv::RequestParam_Event msg_;
};

class Init_RequestParam_Event_request
{
public:
  explicit Init_RequestParam_Event_request(::utils::srv::RequestParam_Event & msg)
  : msg_(msg)
  {}
  Init_RequestParam_Event_response request(::utils::srv::RequestParam_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_RequestParam_Event_response(msg_);
  }

private:
  ::utils::srv::RequestParam_Event msg_;
};

class Init_RequestParam_Event_info
{
public:
  Init_RequestParam_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RequestParam_Event_request info(::utils::srv::RequestParam_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_RequestParam_Event_request(msg_);
  }

private:
  ::utils::srv::RequestParam_Event msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::utils::srv::RequestParam_Event>()
{
  return utils::srv::builder::Init_RequestParam_Event_info();
}

}  // namespace utils

#endif  // UTILS__SRV__DETAIL__REQUEST_PARAM__BUILDER_HPP_
