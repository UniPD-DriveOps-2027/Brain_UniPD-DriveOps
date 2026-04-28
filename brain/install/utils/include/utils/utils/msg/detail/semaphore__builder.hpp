// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from utils:msg/Semaphore.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/semaphore.hpp"


#ifndef UTILS__MSG__DETAIL__SEMAPHORE__BUILDER_HPP_
#define UTILS__MSG__DETAIL__SEMAPHORE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "utils/msg/detail/semaphore__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace utils
{

namespace msg
{

namespace builder
{

class Init_Semaphore_pos_y
{
public:
  explicit Init_Semaphore_pos_y(::utils::msg::Semaphore & msg)
  : msg_(msg)
  {}
  ::utils::msg::Semaphore pos_y(::utils::msg::Semaphore::_pos_y_type arg)
  {
    msg_.pos_y = std::move(arg);
    return std::move(msg_);
  }

private:
  ::utils::msg::Semaphore msg_;
};

class Init_Semaphore_pos_x
{
public:
  explicit Init_Semaphore_pos_x(::utils::msg::Semaphore & msg)
  : msg_(msg)
  {}
  Init_Semaphore_pos_y pos_x(::utils::msg::Semaphore::_pos_x_type arg)
  {
    msg_.pos_x = std::move(arg);
    return Init_Semaphore_pos_y(msg_);
  }

private:
  ::utils::msg::Semaphore msg_;
};

class Init_Semaphore_state
{
public:
  Init_Semaphore_state()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Semaphore_pos_x state(::utils::msg::Semaphore::_state_type arg)
  {
    msg_.state = std::move(arg);
    return Init_Semaphore_pos_x(msg_);
  }

private:
  ::utils::msg::Semaphore msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::utils::msg::Semaphore>()
{
  return utils::msg::builder::Init_Semaphore_state();
}

}  // namespace utils

#endif  // UTILS__MSG__DETAIL__SEMAPHORE__BUILDER_HPP_
