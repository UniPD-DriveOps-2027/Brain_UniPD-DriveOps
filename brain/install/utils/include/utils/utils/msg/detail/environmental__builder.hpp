// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from utils:msg/Environmental.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/environmental.hpp"


#ifndef UTILS__MSG__DETAIL__ENVIRONMENTAL__BUILDER_HPP_
#define UTILS__MSG__DETAIL__ENVIRONMENTAL__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "utils/msg/detail/environmental__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace utils
{

namespace msg
{

namespace builder
{

class Init_Environmental_y
{
public:
  explicit Init_Environmental_y(::utils::msg::Environmental & msg)
  : msg_(msg)
  {}
  ::utils::msg::Environmental y(::utils::msg::Environmental::_y_type arg)
  {
    msg_.y = std::move(arg);
    return std::move(msg_);
  }

private:
  ::utils::msg::Environmental msg_;
};

class Init_Environmental_x
{
public:
  explicit Init_Environmental_x(::utils::msg::Environmental & msg)
  : msg_(msg)
  {}
  Init_Environmental_y x(::utils::msg::Environmental::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_Environmental_y(msg_);
  }

private:
  ::utils::msg::Environmental msg_;
};

class Init_Environmental_obstacle_id
{
public:
  Init_Environmental_obstacle_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Environmental_x obstacle_id(::utils::msg::Environmental::_obstacle_id_type arg)
  {
    msg_.obstacle_id = std::move(arg);
    return Init_Environmental_x(msg_);
  }

private:
  ::utils::msg::Environmental msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::utils::msg::Environmental>()
{
  return utils::msg::builder::Init_Environmental_obstacle_id();
}

}  // namespace utils

#endif  // UTILS__MSG__DETAIL__ENVIRONMENTAL__BUILDER_HPP_
