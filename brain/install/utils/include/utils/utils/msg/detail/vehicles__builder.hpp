// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from utils:msg/Vehicles.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/vehicles.hpp"


#ifndef UTILS__MSG__DETAIL__VEHICLES__BUILDER_HPP_
#define UTILS__MSG__DETAIL__VEHICLES__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "utils/msg/detail/vehicles__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace utils
{

namespace msg
{

namespace builder
{

class Init_Vehicles_rot_b
{
public:
  explicit Init_Vehicles_rot_b(::utils::msg::Vehicles & msg)
  : msg_(msg)
  {}
  ::utils::msg::Vehicles rot_b(::utils::msg::Vehicles::_rot_b_type arg)
  {
    msg_.rot_b = std::move(arg);
    return std::move(msg_);
  }

private:
  ::utils::msg::Vehicles msg_;
};

class Init_Vehicles_rot_a
{
public:
  explicit Init_Vehicles_rot_a(::utils::msg::Vehicles & msg)
  : msg_(msg)
  {}
  Init_Vehicles_rot_b rot_a(::utils::msg::Vehicles::_rot_a_type arg)
  {
    msg_.rot_a = std::move(arg);
    return Init_Vehicles_rot_b(msg_);
  }

private:
  ::utils::msg::Vehicles msg_;
};

class Init_Vehicles_pos_b
{
public:
  explicit Init_Vehicles_pos_b(::utils::msg::Vehicles & msg)
  : msg_(msg)
  {}
  Init_Vehicles_rot_a pos_b(::utils::msg::Vehicles::_pos_b_type arg)
  {
    msg_.pos_b = std::move(arg);
    return Init_Vehicles_rot_a(msg_);
  }

private:
  ::utils::msg::Vehicles msg_;
};

class Init_Vehicles_pos_a
{
public:
  explicit Init_Vehicles_pos_a(::utils::msg::Vehicles & msg)
  : msg_(msg)
  {}
  Init_Vehicles_pos_b pos_a(::utils::msg::Vehicles::_pos_a_type arg)
  {
    msg_.pos_a = std::move(arg);
    return Init_Vehicles_pos_b(msg_);
  }

private:
  ::utils::msg::Vehicles msg_;
};

class Init_Vehicles_timestamp
{
public:
  explicit Init_Vehicles_timestamp(::utils::msg::Vehicles & msg)
  : msg_(msg)
  {}
  Init_Vehicles_pos_a timestamp(::utils::msg::Vehicles::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return Init_Vehicles_pos_a(msg_);
  }

private:
  ::utils::msg::Vehicles msg_;
};

class Init_Vehicles_id
{
public:
  Init_Vehicles_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Vehicles_timestamp id(::utils::msg::Vehicles::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_Vehicles_timestamp(msg_);
  }

private:
  ::utils::msg::Vehicles msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::utils::msg::Vehicles>()
{
  return utils::msg::builder::Init_Vehicles_id();
}

}  // namespace utils

#endif  // UTILS__MSG__DETAIL__VEHICLES__BUILDER_HPP_
