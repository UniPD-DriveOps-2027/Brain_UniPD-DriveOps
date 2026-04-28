// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from utils:msg/Environmental.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/environmental.hpp"


#ifndef UTILS__MSG__DETAIL__ENVIRONMENTAL__TRAITS_HPP_
#define UTILS__MSG__DETAIL__ENVIRONMENTAL__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "utils/msg/detail/environmental__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace utils
{

namespace msg
{

inline void to_flow_style_yaml(
  const Environmental & msg,
  std::ostream & out)
{
  out << "{";
  // member: obstacle_id
  {
    out << "obstacle_id: ";
    rosidl_generator_traits::value_to_yaml(msg.obstacle_id, out);
    out << ", ";
  }

  // member: x
  {
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << ", ";
  }

  // member: y
  {
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Environmental & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: obstacle_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "obstacle_id: ";
    rosidl_generator_traits::value_to_yaml(msg.obstacle_id, out);
    out << "\n";
  }

  // member: x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << "\n";
  }

  // member: y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Environmental & msg, bool use_flow_style = false)
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
  const utils::msg::Environmental & msg,
  std::ostream & out, size_t indentation = 0)
{
  utils::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use utils::msg::to_yaml() instead")]]
inline std::string to_yaml(const utils::msg::Environmental & msg)
{
  return utils::msg::to_yaml(msg);
}

template<>
inline const char * data_type<utils::msg::Environmental>()
{
  return "utils::msg::Environmental";
}

template<>
inline const char * name<utils::msg::Environmental>()
{
  return "utils/msg/Environmental";
}

template<>
struct has_fixed_size<utils::msg::Environmental>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<utils::msg::Environmental>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<utils::msg::Environmental>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // UTILS__MSG__DETAIL__ENVIRONMENTAL__TRAITS_HPP_
