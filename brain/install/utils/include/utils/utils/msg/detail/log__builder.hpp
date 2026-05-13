// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from utils:msg/Log.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/log.hpp"


#ifndef UTILS__MSG__DETAIL__LOG__BUILDER_HPP_
#define UTILS__MSG__DETAIL__LOG__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "utils/msg/detail/log__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace utils
{

namespace msg
{

namespace builder
{

class Init_Log_msg
{
public:
  explicit Init_Log_msg(::utils::msg::Log & msg)
  : msg_(msg)
  {}
  ::utils::msg::Log msg(::utils::msg::Log::_msg_type arg)
  {
    msg_.msg = std::move(arg);
    return std::move(msg_);
  }

private:
  ::utils::msg::Log msg_;
};

class Init_Log_level
{
public:
  Init_Log_level()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Log_msg level(::utils::msg::Log::_level_type arg)
  {
    msg_.level = std::move(arg);
    return Init_Log_msg(msg_);
  }

private:
  ::utils::msg::Log msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::utils::msg::Log>()
{
  return utils::msg::builder::Init_Log_level();
}

}  // namespace utils

#endif  // UTILS__MSG__DETAIL__LOG__BUILDER_HPP_
