// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from utils:msg/Semaphore.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/semaphore.hpp"


#ifndef UTILS__MSG__DETAIL__SEMAPHORE__TRAITS_HPP_
#define UTILS__MSG__DETAIL__SEMAPHORE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "utils/msg/detail/semaphore__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace utils
{

namespace msg
{

inline void to_flow_style_yaml(
  const Semaphore & msg,
  std::ostream & out)
{
  out << "{";
  // member: state
  {
    out << "state: ";
    rosidl_generator_traits::value_to_yaml(msg.state, out);
    out << ", ";
  }

  // member: pos_x
  {
    out << "pos_x: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_x, out);
    out << ", ";
  }

  // member: pos_y
  {
    out << "pos_y: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_y, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Semaphore & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "state: ";
    rosidl_generator_traits::value_to_yaml(msg.state, out);
    out << "\n";
  }

  // member: pos_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pos_x: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_x, out);
    out << "\n";
  }

  // member: pos_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pos_y: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_y, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Semaphore & msg, bool use_flow_style = false)
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
  const utils::msg::Semaphore & msg,
  std::ostream & out, size_t indentation = 0)
{
  utils::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use utils::msg::to_yaml() instead")]]
inline std::string to_yaml(const utils::msg::Semaphore & msg)
{
  return utils::msg::to_yaml(msg);
}

template<>
inline const char * data_type<utils::msg::Semaphore>()
{
  return "utils::msg::Semaphore";
}

template<>
inline const char * name<utils::msg::Semaphore>()
{
  return "utils/msg/Semaphore";
}

template<>
struct has_fixed_size<utils::msg::Semaphore>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<utils::msg::Semaphore>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<utils::msg::Semaphore>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // UTILS__MSG__DETAIL__SEMAPHORE__TRAITS_HPP_
