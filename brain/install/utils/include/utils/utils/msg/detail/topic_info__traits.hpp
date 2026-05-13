// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from utils:msg/TopicInfo.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/topic_info.hpp"


#ifndef UTILS__MSG__DETAIL__TOPIC_INFO__TRAITS_HPP_
#define UTILS__MSG__DETAIL__TOPIC_INFO__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "utils/msg/detail/topic_info__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace utils
{

namespace msg
{

inline void to_flow_style_yaml(
  const TopicInfo & msg,
  std::ostream & out)
{
  out << "{";
  // member: topic_id
  {
    out << "topic_id: ";
    rosidl_generator_traits::value_to_yaml(msg.topic_id, out);
    out << ", ";
  }

  // member: topic_name
  {
    out << "topic_name: ";
    rosidl_generator_traits::value_to_yaml(msg.topic_name, out);
    out << ", ";
  }

  // member: message_type
  {
    out << "message_type: ";
    rosidl_generator_traits::value_to_yaml(msg.message_type, out);
    out << ", ";
  }

  // member: md5sum
  {
    out << "md5sum: ";
    rosidl_generator_traits::value_to_yaml(msg.md5sum, out);
    out << ", ";
  }

  // member: buffer_size
  {
    out << "buffer_size: ";
    rosidl_generator_traits::value_to_yaml(msg.buffer_size, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const TopicInfo & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: topic_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "topic_id: ";
    rosidl_generator_traits::value_to_yaml(msg.topic_id, out);
    out << "\n";
  }

  // member: topic_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "topic_name: ";
    rosidl_generator_traits::value_to_yaml(msg.topic_name, out);
    out << "\n";
  }

  // member: message_type
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "message_type: ";
    rosidl_generator_traits::value_to_yaml(msg.message_type, out);
    out << "\n";
  }

  // member: md5sum
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "md5sum: ";
    rosidl_generator_traits::value_to_yaml(msg.md5sum, out);
    out << "\n";
  }

  // member: buffer_size
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "buffer_size: ";
    rosidl_generator_traits::value_to_yaml(msg.buffer_size, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const TopicInfo & msg, bool use_flow_style = false)
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
  const utils::msg::TopicInfo & msg,
  std::ostream & out, size_t indentation = 0)
{
  utils::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use utils::msg::to_yaml() instead")]]
inline std::string to_yaml(const utils::msg::TopicInfo & msg)
{
  return utils::msg::to_yaml(msg);
}

template<>
inline const char * data_type<utils::msg::TopicInfo>()
{
  return "utils::msg::TopicInfo";
}

template<>
inline const char * name<utils::msg::TopicInfo>()
{
  return "utils/msg/TopicInfo";
}

template<>
struct has_fixed_size<utils::msg::TopicInfo>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<utils::msg::TopicInfo>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<utils::msg::TopicInfo>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // UTILS__MSG__DETAIL__TOPIC_INFO__TRAITS_HPP_
