// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from utils:msg/TopicInfo.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/topic_info.hpp"


#ifndef UTILS__MSG__DETAIL__TOPIC_INFO__STRUCT_HPP_
#define UTILS__MSG__DETAIL__TOPIC_INFO__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__utils__msg__TopicInfo __attribute__((deprecated))
#else
# define DEPRECATED__utils__msg__TopicInfo __declspec(deprecated)
#endif

namespace utils
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TopicInfo_
{
  using Type = TopicInfo_<ContainerAllocator>;

  explicit TopicInfo_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->topic_id = 0;
      this->topic_name = "";
      this->message_type = "";
      this->md5sum = "";
      this->buffer_size = 0l;
    }
  }

  explicit TopicInfo_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : topic_name(_alloc),
    message_type(_alloc),
    md5sum(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->topic_id = 0;
      this->topic_name = "";
      this->message_type = "";
      this->md5sum = "";
      this->buffer_size = 0l;
    }
  }

  // field types and members
  using _topic_id_type =
    uint16_t;
  _topic_id_type topic_id;
  using _topic_name_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _topic_name_type topic_name;
  using _message_type_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _message_type_type message_type;
  using _md5sum_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _md5sum_type md5sum;
  using _buffer_size_type =
    int32_t;
  _buffer_size_type buffer_size;

  // setters for named parameter idiom
  Type & set__topic_id(
    const uint16_t & _arg)
  {
    this->topic_id = _arg;
    return *this;
  }
  Type & set__topic_name(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->topic_name = _arg;
    return *this;
  }
  Type & set__message_type(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->message_type = _arg;
    return *this;
  }
  Type & set__md5sum(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->md5sum = _arg;
    return *this;
  }
  Type & set__buffer_size(
    const int32_t & _arg)
  {
    this->buffer_size = _arg;
    return *this;
  }

  // constant declarations
  static constexpr uint16_t ID_PUBLISHER =
    0u;
  static constexpr uint16_t ID_SUBSCRIBER =
    1u;
  static constexpr uint16_t ID_SERVICE_SERVER =
    2u;
  static constexpr uint16_t ID_SERVICE_CLIENT =
    4u;
  static constexpr uint16_t ID_PARAMETER_REQUEST =
    6u;
  static constexpr uint16_t ID_LOG =
    7u;
  static constexpr uint16_t ID_TIME =
    10u;
  static constexpr uint16_t ID_TX_STOP =
    11u;

  // pointer types
  using RawPtr =
    utils::msg::TopicInfo_<ContainerAllocator> *;
  using ConstRawPtr =
    const utils::msg::TopicInfo_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<utils::msg::TopicInfo_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<utils::msg::TopicInfo_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      utils::msg::TopicInfo_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<utils::msg::TopicInfo_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      utils::msg::TopicInfo_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<utils::msg::TopicInfo_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<utils::msg::TopicInfo_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<utils::msg::TopicInfo_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__utils__msg__TopicInfo
    std::shared_ptr<utils::msg::TopicInfo_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__utils__msg__TopicInfo
    std::shared_ptr<utils::msg::TopicInfo_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TopicInfo_ & other) const
  {
    if (this->topic_id != other.topic_id) {
      return false;
    }
    if (this->topic_name != other.topic_name) {
      return false;
    }
    if (this->message_type != other.message_type) {
      return false;
    }
    if (this->md5sum != other.md5sum) {
      return false;
    }
    if (this->buffer_size != other.buffer_size) {
      return false;
    }
    return true;
  }
  bool operator!=(const TopicInfo_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TopicInfo_

// alias to use template instance with default allocator
using TopicInfo =
  utils::msg::TopicInfo_<std::allocator<void>>;

// constant definitions
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint16_t TopicInfo_<ContainerAllocator>::ID_PUBLISHER;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint16_t TopicInfo_<ContainerAllocator>::ID_SUBSCRIBER;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint16_t TopicInfo_<ContainerAllocator>::ID_SERVICE_SERVER;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint16_t TopicInfo_<ContainerAllocator>::ID_SERVICE_CLIENT;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint16_t TopicInfo_<ContainerAllocator>::ID_PARAMETER_REQUEST;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint16_t TopicInfo_<ContainerAllocator>::ID_LOG;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint16_t TopicInfo_<ContainerAllocator>::ID_TIME;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint16_t TopicInfo_<ContainerAllocator>::ID_TX_STOP;
#endif  // __cplusplus < 201703L

}  // namespace msg

}  // namespace utils

#endif  // UTILS__MSG__DETAIL__TOPIC_INFO__STRUCT_HPP_
