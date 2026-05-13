// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from utils:msg/Localisation.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/localisation.hpp"


#ifndef UTILS__MSG__DETAIL__LOCALISATION__BUILDER_HPP_
#define UTILS__MSG__DETAIL__LOCALISATION__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "utils/msg/detail/localisation__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace utils
{

namespace msg
{

namespace builder
{

class Init_Localisation_rot_b
{
public:
  explicit Init_Localisation_rot_b(::utils::msg::Localisation & msg)
  : msg_(msg)
  {}
  ::utils::msg::Localisation rot_b(::utils::msg::Localisation::_rot_b_type arg)
  {
    msg_.rot_b = std::move(arg);
    return std::move(msg_);
  }

private:
  ::utils::msg::Localisation msg_;
};

class Init_Localisation_rot_a
{
public:
  explicit Init_Localisation_rot_a(::utils::msg::Localisation & msg)
  : msg_(msg)
  {}
  Init_Localisation_rot_b rot_a(::utils::msg::Localisation::_rot_a_type arg)
  {
    msg_.rot_a = std::move(arg);
    return Init_Localisation_rot_b(msg_);
  }

private:
  ::utils::msg::Localisation msg_;
};

class Init_Localisation_pos_b
{
public:
  explicit Init_Localisation_pos_b(::utils::msg::Localisation & msg)
  : msg_(msg)
  {}
  Init_Localisation_rot_a pos_b(::utils::msg::Localisation::_pos_b_type arg)
  {
    msg_.pos_b = std::move(arg);
    return Init_Localisation_rot_a(msg_);
  }

private:
  ::utils::msg::Localisation msg_;
};

class Init_Localisation_pos_a
{
public:
  explicit Init_Localisation_pos_a(::utils::msg::Localisation & msg)
  : msg_(msg)
  {}
  Init_Localisation_pos_b pos_a(::utils::msg::Localisation::_pos_a_type arg)
  {
    msg_.pos_a = std::move(arg);
    return Init_Localisation_pos_b(msg_);
  }

private:
  ::utils::msg::Localisation msg_;
};

class Init_Localisation_timestamp
{
public:
  Init_Localisation_timestamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Localisation_pos_a timestamp(::utils::msg::Localisation::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return Init_Localisation_pos_a(msg_);
  }

private:
  ::utils::msg::Localisation msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::utils::msg::Localisation>()
{
  return utils::msg::builder::Init_Localisation_timestamp();
}

}  // namespace utils

#endif  // UTILS__MSG__DETAIL__LOCALISATION__BUILDER_HPP_
