// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from utils:msg/Trafficsignprediction.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/trafficsignprediction.hpp"


#ifndef UTILS__MSG__DETAIL__TRAFFICSIGNPREDICTION__TRAITS_HPP_
#define UTILS__MSG__DETAIL__TRAFFICSIGNPREDICTION__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "utils/msg/detail/trafficsignprediction__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace utils
{

namespace msg
{

inline void to_flow_style_yaml(
  const Trafficsignprediction & msg,
  std::ostream & out)
{
  out << "{";
  // member: prediction
  {
    out << "prediction: ";
    rosidl_generator_traits::value_to_yaml(msg.prediction, out);
    out << ", ";
  }

  // member: conf
  {
    out << "conf: ";
    rosidl_generator_traits::value_to_yaml(msg.conf, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Trafficsignprediction & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: prediction
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "prediction: ";
    rosidl_generator_traits::value_to_yaml(msg.prediction, out);
    out << "\n";
  }

  // member: conf
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "conf: ";
    rosidl_generator_traits::value_to_yaml(msg.conf, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Trafficsignprediction & msg, bool use_flow_style = false)
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
  const utils::msg::Trafficsignprediction & msg,
  std::ostream & out, size_t indentation = 0)
{
  utils::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use utils::msg::to_yaml() instead")]]
inline std::string to_yaml(const utils::msg::Trafficsignprediction & msg)
{
  return utils::msg::to_yaml(msg);
}

template<>
inline const char * data_type<utils::msg::Trafficsignprediction>()
{
  return "utils::msg::Trafficsignprediction";
}

template<>
inline const char * name<utils::msg::Trafficsignprediction>()
{
  return "utils/msg/Trafficsignprediction";
}

template<>
struct has_fixed_size<utils::msg::Trafficsignprediction>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<utils::msg::Trafficsignprediction>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<utils::msg::Trafficsignprediction>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // UTILS__MSG__DETAIL__TRAFFICSIGNPREDICTION__TRAITS_HPP_
