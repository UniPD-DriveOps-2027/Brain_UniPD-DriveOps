// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from utils:srv/Subscribing.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/srv/subscribing.hpp"


#ifndef UTILS__SRV__DETAIL__SUBSCRIBING__BUILDER_HPP_
#define UTILS__SRV__DETAIL__SUBSCRIBING__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "utils/srv/detail/subscribing__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace utils
{

namespace srv
{

namespace builder
{

class Init_Subscribing_Request_topic
{
public:
  explicit Init_Subscribing_Request_topic(::utils::srv::Subscribing_Request & msg)
  : msg_(msg)
  {}
  ::utils::srv::Subscribing_Request topic(::utils::srv::Subscribing_Request::_topic_type arg)
  {
    msg_.topic = std::move(arg);
    return std::move(msg_);
  }

private:
  ::utils::srv::Subscribing_Request msg_;
};

class Init_Subscribing_Request_code
{
public:
  explicit Init_Subscribing_Request_code(::utils::srv::Subscribing_Request & msg)
  : msg_(msg)
  {}
  Init_Subscribing_Request_topic code(::utils::srv::Subscribing_Request::_code_type arg)
  {
    msg_.code = std::move(arg);
    return Init_Subscribing_Request_topic(msg_);
  }

private:
  ::utils::srv::Subscribing_Request msg_;
};

class Init_Subscribing_Request_subscribing
{
public:
  Init_Subscribing_Request_subscribing()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Subscribing_Request_code subscribing(::utils::srv::Subscribing_Request::_subscribing_type arg)
  {
    msg_.subscribing = std::move(arg);
    return Init_Subscribing_Request_code(msg_);
  }

private:
  ::utils::srv::Subscribing_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::utils::srv::Subscribing_Request>()
{
  return utils::srv::builder::Init_Subscribing_Request_subscribing();
}

}  // namespace utils


namespace utils
{

namespace srv
{

namespace builder
{

class Init_Subscribing_Response_topic
{
public:
  Init_Subscribing_Response_topic()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::utils::srv::Subscribing_Response topic(::utils::srv::Subscribing_Response::_topic_type arg)
  {
    msg_.topic = std::move(arg);
    return std::move(msg_);
  }

private:
  ::utils::srv::Subscribing_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::utils::srv::Subscribing_Response>()
{
  return utils::srv::builder::Init_Subscribing_Response_topic();
}

}  // namespace utils


namespace utils
{

namespace srv
{

namespace builder
{

class Init_Subscribing_Event_response
{
public:
  explicit Init_Subscribing_Event_response(::utils::srv::Subscribing_Event & msg)
  : msg_(msg)
  {}
  ::utils::srv::Subscribing_Event response(::utils::srv::Subscribing_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::utils::srv::Subscribing_Event msg_;
};

class Init_Subscribing_Event_request
{
public:
  explicit Init_Subscribing_Event_request(::utils::srv::Subscribing_Event & msg)
  : msg_(msg)
  {}
  Init_Subscribing_Event_response request(::utils::srv::Subscribing_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_Subscribing_Event_response(msg_);
  }

private:
  ::utils::srv::Subscribing_Event msg_;
};

class Init_Subscribing_Event_info
{
public:
  Init_Subscribing_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Subscribing_Event_request info(::utils::srv::Subscribing_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_Subscribing_Event_request(msg_);
  }

private:
  ::utils::srv::Subscribing_Event msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::utils::srv::Subscribing_Event>()
{
  return utils::srv::builder::Init_Subscribing_Event_info();
}

}  // namespace utils

#endif  // UTILS__SRV__DETAIL__SUBSCRIBING__BUILDER_HPP_
