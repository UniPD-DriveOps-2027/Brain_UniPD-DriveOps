// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from utils:msg/IMU.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/imu.hpp"


#ifndef UTILS__MSG__DETAIL__IMU__TRAITS_HPP_
#define UTILS__MSG__DETAIL__IMU__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "utils/msg/detail/imu__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace utils
{

namespace msg
{

inline void to_flow_style_yaml(
  const IMU & msg,
  std::ostream & out)
{
  out << "{";
  // member: roll
  {
    out << "roll: ";
    rosidl_generator_traits::value_to_yaml(msg.roll, out);
    out << ", ";
  }

  // member: pitch
  {
    out << "pitch: ";
    rosidl_generator_traits::value_to_yaml(msg.pitch, out);
    out << ", ";
  }

  // member: yaw
  {
    out << "yaw: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw, out);
    out << ", ";
  }

  // member: accelx
  {
    out << "accelx: ";
    rosidl_generator_traits::value_to_yaml(msg.accelx, out);
    out << ", ";
  }

  // member: accely
  {
    out << "accely: ";
    rosidl_generator_traits::value_to_yaml(msg.accely, out);
    out << ", ";
  }

  // member: accelz
  {
    out << "accelz: ";
    rosidl_generator_traits::value_to_yaml(msg.accelz, out);
    out << ", ";
  }

  // member: gyrox
  {
    out << "gyrox: ";
    rosidl_generator_traits::value_to_yaml(msg.gyrox, out);
    out << ", ";
  }

  // member: gyroy
  {
    out << "gyroy: ";
    rosidl_generator_traits::value_to_yaml(msg.gyroy, out);
    out << ", ";
  }

  // member: gyroz
  {
    out << "gyroz: ";
    rosidl_generator_traits::value_to_yaml(msg.gyroz, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const IMU & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: roll
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "roll: ";
    rosidl_generator_traits::value_to_yaml(msg.roll, out);
    out << "\n";
  }

  // member: pitch
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pitch: ";
    rosidl_generator_traits::value_to_yaml(msg.pitch, out);
    out << "\n";
  }

  // member: yaw
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "yaw: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw, out);
    out << "\n";
  }

  // member: accelx
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "accelx: ";
    rosidl_generator_traits::value_to_yaml(msg.accelx, out);
    out << "\n";
  }

  // member: accely
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "accely: ";
    rosidl_generator_traits::value_to_yaml(msg.accely, out);
    out << "\n";
  }

  // member: accelz
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "accelz: ";
    rosidl_generator_traits::value_to_yaml(msg.accelz, out);
    out << "\n";
  }

  // member: gyrox
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "gyrox: ";
    rosidl_generator_traits::value_to_yaml(msg.gyrox, out);
    out << "\n";
  }

  // member: gyroy
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "gyroy: ";
    rosidl_generator_traits::value_to_yaml(msg.gyroy, out);
    out << "\n";
  }

  // member: gyroz
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "gyroz: ";
    rosidl_generator_traits::value_to_yaml(msg.gyroz, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const IMU & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace utils

namespace rosidl_generator_traits
{

[[deprecated("use utils::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const utils::msg::IMU & msg,
  std::ostream & out, size_t indentation = 0)
{
  utils::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use utils::msg::to_yaml() instead")]]
inline std::string to_yaml(const utils::msg::IMU & msg)
{
  return utils::msg::to_yaml(msg);
}

template<>
inline const char * data_type<utils::msg::IMU>()
{
  return "utils::msg::IMU";
}

template<>
inline const char * name<utils::msg::IMU>()
{
  return "utils/msg/IMU";
}

template<>
struct has_fixed_size<utils::msg::IMU>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<utils::msg::IMU>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<utils::msg::IMU>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // UTILS__MSG__DETAIL__IMU__TRAITS_HPP_
