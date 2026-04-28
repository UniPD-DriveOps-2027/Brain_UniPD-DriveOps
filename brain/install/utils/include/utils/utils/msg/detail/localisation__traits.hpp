// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from utils:msg/Localisation.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/localisation.hpp"


#ifndef UTILS__MSG__DETAIL__LOCALISATION__TRAITS_HPP_
#define UTILS__MSG__DETAIL__LOCALISATION__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "utils/msg/detail/localisation__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace utils
{

namespace msg
{

inline void to_flow_style_yaml(
  const Localisation & msg,
  std::ostream & out)
{
  out << "{";
  // member: timestamp
  {
    out << "timestamp: ";
    rosidl_generator_traits::value_to_yaml(msg.timestamp, out);
    out << ", ";
  }

  // member: pos_a
  {
    out << "pos_a: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_a, out);
    out << ", ";
  }

  // member: pos_b
  {
    out << "pos_b: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_b, out);
    out << ", ";
  }

  // member: rot_a
  {
    out << "rot_a: ";
    rosidl_generator_traits::value_to_yaml(msg.rot_a, out);
    out << ", ";
  }

  // member: rot_b
  {
    out << "rot_b: ";
    rosidl_generator_traits::value_to_yaml(msg.rot_b, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Localisation & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: timestamp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "timestamp: ";
    rosidl_generator_traits::value_to_yaml(msg.timestamp, out);
    out << "\n";
  }

  // member: pos_a
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pos_a: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_a, out);
    out << "\n";
  }

  // member: pos_b
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pos_b: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_b, out);
    out << "\n";
  }

  // member: rot_a
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "rot_a: ";
    rosidl_generator_traits::value_to_yaml(msg.rot_a, out);
    out << "\n";
  }

  // member: rot_b
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "rot_b: ";
    rosidl_generator_traits::value_to_yaml(msg.rot_b, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Localisation & msg, bool use_flow_style = false)
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
  const utils::msg::Localisation & msg,
  std::ostream & out, size_t indentation = 0)
{
  utils::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use utils::msg::to_yaml() instead")]]
inline std::string to_yaml(const utils::msg::Localisation & msg)
{
  return utils::msg::to_yaml(msg);
}

template<>
inline const char * data_type<utils::msg::Localisation>()
{
  return "utils::msg::Localisation";
}

template<>
inline const char * name<utils::msg::Localisation>()
{
  return "utils/msg/Localisation";
}

template<>
struct has_fixed_size<utils::msg::Localisation>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<utils::msg::Localisation>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<utils::msg::Localisation>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // UTILS__MSG__DETAIL__LOCALISATION__TRAITS_HPP_
