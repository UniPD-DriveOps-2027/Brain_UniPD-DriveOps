// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from utils:srv/RequestParam.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/srv/request_param.hpp"


#ifndef UTILS__SRV__DETAIL__REQUEST_PARAM__TRAITS_HPP_
#define UTILS__SRV__DETAIL__REQUEST_PARAM__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "utils/srv/detail/request_param__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace utils
{

namespace srv
{

inline void to_flow_style_yaml(
  const RequestParam_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: name
  {
    out << "name: ";
    rosidl_generator_traits::value_to_yaml(msg.name, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RequestParam_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "name: ";
    rosidl_generator_traits::value_to_yaml(msg.name, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RequestParam_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace utils

namespace rosidl_generator_traits
{

[[deprecated("use utils::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const utils::srv::RequestParam_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  utils::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use utils::srv::to_yaml() instead")]]
inline std::string to_yaml(const utils::srv::RequestParam_Request & msg)
{
  return utils::srv::to_yaml(msg);
}

template<>
inline const char * data_type<utils::srv::RequestParam_Request>()
{
  return "utils::srv::RequestParam_Request";
}

template<>
inline const char * name<utils::srv::RequestParam_Request>()
{
  return "utils/srv/RequestParam_Request";
}

template<>
struct has_fixed_size<utils::srv::RequestParam_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<utils::srv::RequestParam_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<utils::srv::RequestParam_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace utils
{

namespace srv
{

inline void to_flow_style_yaml(
  const RequestParam_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: ints
  {
    if (msg.ints.size() == 0) {
      out << "ints: []";
    } else {
      out << "ints: [";
      size_t pending_items = msg.ints.size();
      for (auto item : msg.ints) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: floats
  {
    if (msg.floats.size() == 0) {
      out << "floats: []";
    } else {
      out << "floats: [";
      size_t pending_items = msg.floats.size();
      for (auto item : msg.floats) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: strings
  {
    if (msg.strings.size() == 0) {
      out << "strings: []";
    } else {
      out << "strings: [";
      size_t pending_items = msg.strings.size();
      for (auto item : msg.strings) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RequestParam_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: ints
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.ints.size() == 0) {
      out << "ints: []\n";
    } else {
      out << "ints:\n";
      for (auto item : msg.ints) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: floats
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.floats.size() == 0) {
      out << "floats: []\n";
    } else {
      out << "floats:\n";
      for (auto item : msg.floats) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: strings
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.strings.size() == 0) {
      out << "strings: []\n";
    } else {
      out << "strings:\n";
      for (auto item : msg.strings) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RequestParam_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace utils

namespace rosidl_generator_traits
{

[[deprecated("use utils::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const utils::srv::RequestParam_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  utils::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use utils::srv::to_yaml() instead")]]
inline std::string to_yaml(const utils::srv::RequestParam_Response & msg)
{
  return utils::srv::to_yaml(msg);
}

template<>
inline const char * data_type<utils::srv::RequestParam_Response>()
{
  return "utils::srv::RequestParam_Response";
}

template<>
inline const char * name<utils::srv::RequestParam_Response>()
{
  return "utils/srv/RequestParam_Response";
}

template<>
struct has_fixed_size<utils::srv::RequestParam_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<utils::srv::RequestParam_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<utils::srv::RequestParam_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__traits.hpp"

namespace utils
{

namespace srv
{

inline void to_flow_style_yaml(
  const RequestParam_Event & msg,
  std::ostream & out)
{
  out << "{";
  // member: info
  {
    out << "info: ";
    to_flow_style_yaml(msg.info, out);
    out << ", ";
  }

  // member: request
  {
    if (msg.request.size() == 0) {
      out << "request: []";
    } else {
      out << "request: [";
      size_t pending_items = msg.request.size();
      for (auto item : msg.request) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: response
  {
    if (msg.response.size() == 0) {
      out << "response: []";
    } else {
      out << "response: [";
      size_t pending_items = msg.response.size();
      for (auto item : msg.response) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RequestParam_Event & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: info
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "info:\n";
    to_block_style_yaml(msg.info, out, indentation + 2);
  }

  // member: request
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.request.size() == 0) {
      out << "request: []\n";
    } else {
      out << "request:\n";
      for (auto item : msg.request) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }

  // member: response
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.response.size() == 0) {
      out << "response: []\n";
    } else {
      out << "response:\n";
      for (auto item : msg.response) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RequestParam_Event & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace utils

namespace rosidl_generator_traits
{

[[deprecated("use utils::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const utils::srv::RequestParam_Event & msg,
  std::ostream & out, size_t indentation = 0)
{
  utils::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use utils::srv::to_yaml() instead")]]
inline std::string to_yaml(const utils::srv::RequestParam_Event & msg)
{
  return utils::srv::to_yaml(msg);
}

template<>
inline const char * data_type<utils::srv::RequestParam_Event>()
{
  return "utils::srv::RequestParam_Event";
}

template<>
inline const char * name<utils::srv::RequestParam_Event>()
{
  return "utils/srv/RequestParam_Event";
}

template<>
struct has_fixed_size<utils::srv::RequestParam_Event>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<utils::srv::RequestParam_Event>
  : std::integral_constant<bool, has_bounded_size<service_msgs::msg::ServiceEventInfo>::value && has_bounded_size<utils::srv::RequestParam_Request>::value && has_bounded_size<utils::srv::RequestParam_Response>::value> {};

template<>
struct is_message<utils::srv::RequestParam_Event>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<utils::srv::RequestParam>()
{
  return "utils::srv::RequestParam";
}

template<>
inline const char * name<utils::srv::RequestParam>()
{
  return "utils/srv/RequestParam";
}

template<>
struct has_fixed_size<utils::srv::RequestParam>
  : std::integral_constant<
    bool,
    has_fixed_size<utils::srv::RequestParam_Request>::value &&
    has_fixed_size<utils::srv::RequestParam_Response>::value
  >
{
};

template<>
struct has_bounded_size<utils::srv::RequestParam>
  : std::integral_constant<
    bool,
    has_bounded_size<utils::srv::RequestParam_Request>::value &&
    has_bounded_size<utils::srv::RequestParam_Response>::value
  >
{
};

template<>
struct is_service<utils::srv::RequestParam>
  : std::true_type
{
};

template<>
struct is_service_request<utils::srv::RequestParam_Request>
  : std::true_type
{
};

template<>
struct is_service_response<utils::srv::RequestParam_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // UTILS__SRV__DETAIL__REQUEST_PARAM__TRAITS_HPP_
