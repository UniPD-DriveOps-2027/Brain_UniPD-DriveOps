// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from utils:msg/Conditions.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/conditions.hpp"


#ifndef UTILS__MSG__DETAIL__CONDITIONS__TRAITS_HPP_
#define UTILS__MSG__DETAIL__CONDITIONS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "utils/msg/detail/conditions__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace utils
{

namespace msg
{

inline void to_flow_style_yaml(
  const Conditions & msg,
  std::ostream & out)
{
  out << "{";
  // member: can_overtake
  {
    out << "can_overtake: ";
    rosidl_generator_traits::value_to_yaml(msg.can_overtake, out);
    out << ", ";
  }

  // member: highway
  {
    out << "highway: ";
    rosidl_generator_traits::value_to_yaml(msg.highway, out);
    out << ", ";
  }

  // member: car_on_path
  {
    out << "car_on_path: ";
    rosidl_generator_traits::value_to_yaml(msg.car_on_path, out);
    out << ", ";
  }

  // member: rerouting
  {
    out << "rerouting: ";
    rosidl_generator_traits::value_to_yaml(msg.rerouting, out);
    out << ", ";
  }

  // member: tunnel
  {
    out << "tunnel: ";
    rosidl_generator_traits::value_to_yaml(msg.tunnel, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Conditions & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: can_overtake
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "can_overtake: ";
    rosidl_generator_traits::value_to_yaml(msg.can_overtake, out);
    out << "\n";
  }

  // member: highway
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "highway: ";
    rosidl_generator_traits::value_to_yaml(msg.highway, out);
    out << "\n";
  }

  // member: car_on_path
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "car_on_path: ";
    rosidl_generator_traits::value_to_yaml(msg.car_on_path, out);
    out << "\n";
  }

  // member: rerouting
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "rerouting: ";
    rosidl_generator_traits::value_to_yaml(msg.rerouting, out);
    out << "\n";
  }

  // member: tunnel
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "tunnel: ";
    rosidl_generator_traits::value_to_yaml(msg.tunnel, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Conditions & msg, bool use_flow_style = false)
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
  const utils::msg::Conditions & msg,
  std::ostream & out, size_t indentation = 0)
{
  utils::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use utils::msg::to_yaml() instead")]]
inline std::string to_yaml(const utils::msg::Conditions & msg)
{
  return utils::msg::to_yaml(msg);
}

template<>
inline const char * data_type<utils::msg::Conditions>()
{
  return "utils::msg::Conditions";
}

template<>
inline const char * name<utils::msg::Conditions>()
{
  return "utils/msg/Conditions";
}

template<>
struct has_fixed_size<utils::msg::Conditions>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<utils::msg::Conditions>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<utils::msg::Conditions>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // UTILS__MSG__DETAIL__CONDITIONS__TRAITS_HPP_
