// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from utils:msg/IMU.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/imu.hpp"


#ifndef UTILS__MSG__DETAIL__IMU__BUILDER_HPP_
#define UTILS__MSG__DETAIL__IMU__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "utils/msg/detail/imu__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace utils
{

namespace msg
{

namespace builder
{

class Init_IMU_gyroz
{
public:
  explicit Init_IMU_gyroz(::utils::msg::IMU & msg)
  : msg_(msg)
  {}
  ::utils::msg::IMU gyroz(::utils::msg::IMU::_gyroz_type arg)
  {
    msg_.gyroz = std::move(arg);
    return std::move(msg_);
  }

private:
  ::utils::msg::IMU msg_;
};

class Init_IMU_gyroy
{
public:
  explicit Init_IMU_gyroy(::utils::msg::IMU & msg)
  : msg_(msg)
  {}
  Init_IMU_gyroz gyroy(::utils::msg::IMU::_gyroy_type arg)
  {
    msg_.gyroy = std::move(arg);
    return Init_IMU_gyroz(msg_);
  }

private:
  ::utils::msg::IMU msg_;
};

class Init_IMU_gyrox
{
public:
  explicit Init_IMU_gyrox(::utils::msg::IMU & msg)
  : msg_(msg)
  {}
  Init_IMU_gyroy gyrox(::utils::msg::IMU::_gyrox_type arg)
  {
    msg_.gyrox = std::move(arg);
    return Init_IMU_gyroy(msg_);
  }

private:
  ::utils::msg::IMU msg_;
};

class Init_IMU_accelz
{
public:
  explicit Init_IMU_accelz(::utils::msg::IMU & msg)
  : msg_(msg)
  {}
  Init_IMU_gyrox accelz(::utils::msg::IMU::_accelz_type arg)
  {
    msg_.accelz = std::move(arg);
    return Init_IMU_gyrox(msg_);
  }

private:
  ::utils::msg::IMU msg_;
};

class Init_IMU_accely
{
public:
  explicit Init_IMU_accely(::utils::msg::IMU & msg)
  : msg_(msg)
  {}
  Init_IMU_accelz accely(::utils::msg::IMU::_accely_type arg)
  {
    msg_.accely = std::move(arg);
    return Init_IMU_accelz(msg_);
  }

private:
  ::utils::msg::IMU msg_;
};

class Init_IMU_accelx
{
public:
  explicit Init_IMU_accelx(::utils::msg::IMU & msg)
  : msg_(msg)
  {}
  Init_IMU_accely accelx(::utils::msg::IMU::_accelx_type arg)
  {
    msg_.accelx = std::move(arg);
    return Init_IMU_accely(msg_);
  }

private:
  ::utils::msg::IMU msg_;
};

class Init_IMU_yaw
{
public:
  explicit Init_IMU_yaw(::utils::msg::IMU & msg)
  : msg_(msg)
  {}
  Init_IMU_accelx yaw(::utils::msg::IMU::_yaw_type arg)
  {
    msg_.yaw = std::move(arg);
    return Init_IMU_accelx(msg_);
  }

private:
  ::utils::msg::IMU msg_;
};

class Init_IMU_pitch
{
public:
  explicit Init_IMU_pitch(::utils::msg::IMU & msg)
  : msg_(msg)
  {}
  Init_IMU_yaw pitch(::utils::msg::IMU::_pitch_type arg)
  {
    msg_.pitch = std::move(arg);
    return Init_IMU_yaw(msg_);
  }

private:
  ::utils::msg::IMU msg_;
};

class Init_IMU_roll
{
public:
  Init_IMU_roll()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_IMU_pitch roll(::utils::msg::IMU::_roll_type arg)
  {
    msg_.roll = std::move(arg);
    return Init_IMU_pitch(msg_);
  }

private:
  ::utils::msg::IMU msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::utils::msg::IMU>()
{
  return utils::msg::builder::Init_IMU_roll();
}

}  // namespace utils

#endif  // UTILS__MSG__DETAIL__IMU__BUILDER_HPP_
