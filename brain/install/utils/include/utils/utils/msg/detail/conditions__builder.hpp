// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from utils:msg/Conditions.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/conditions.hpp"


#ifndef UTILS__MSG__DETAIL__CONDITIONS__BUILDER_HPP_
#define UTILS__MSG__DETAIL__CONDITIONS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "utils/msg/detail/conditions__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace utils
{

namespace msg
{

namespace builder
{

class Init_Conditions_tunnel
{
public:
  explicit Init_Conditions_tunnel(::utils::msg::Conditions & msg)
  : msg_(msg)
  {}
  ::utils::msg::Conditions tunnel(::utils::msg::Conditions::_tunnel_type arg)
  {
    msg_.tunnel = std::move(arg);
    return std::move(msg_);
  }

private:
  ::utils::msg::Conditions msg_;
};

class Init_Conditions_rerouting
{
public:
  explicit Init_Conditions_rerouting(::utils::msg::Conditions & msg)
  : msg_(msg)
  {}
  Init_Conditions_tunnel rerouting(::utils::msg::Conditions::_rerouting_type arg)
  {
    msg_.rerouting = std::move(arg);
    return Init_Conditions_tunnel(msg_);
  }

private:
  ::utils::msg::Conditions msg_;
};

class Init_Conditions_car_on_path
{
public:
  explicit Init_Conditions_car_on_path(::utils::msg::Conditions & msg)
  : msg_(msg)
  {}
  Init_Conditions_rerouting car_on_path(::utils::msg::Conditions::_car_on_path_type arg)
  {
    msg_.car_on_path = std::move(arg);
    return Init_Conditions_rerouting(msg_);
  }

private:
  ::utils::msg::Conditions msg_;
};

class Init_Conditions_highway
{
public:
  explicit Init_Conditions_highway(::utils::msg::Conditions & msg)
  : msg_(msg)
  {}
  Init_Conditions_car_on_path highway(::utils::msg::Conditions::_highway_type arg)
  {
    msg_.highway = std::move(arg);
    return Init_Conditions_car_on_path(msg_);
  }

private:
  ::utils::msg::Conditions msg_;
};

class Init_Conditions_can_overtake
{
public:
  Init_Conditions_can_overtake()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Conditions_highway can_overtake(::utils::msg::Conditions::_can_overtake_type arg)
  {
    msg_.can_overtake = std::move(arg);
    return Init_Conditions_highway(msg_);
  }

private:
  ::utils::msg::Conditions msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::utils::msg::Conditions>()
{
  return utils::msg::builder::Init_Conditions_can_overtake();
}

}  // namespace utils

#endif  // UTILS__MSG__DETAIL__CONDITIONS__BUILDER_HPP_
