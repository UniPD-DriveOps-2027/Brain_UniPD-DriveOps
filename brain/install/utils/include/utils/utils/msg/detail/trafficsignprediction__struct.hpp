// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from utils:msg/Trafficsignprediction.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/trafficsignprediction.hpp"


#ifndef UTILS__MSG__DETAIL__TRAFFICSIGNPREDICTION__STRUCT_HPP_
#define UTILS__MSG__DETAIL__TRAFFICSIGNPREDICTION__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__utils__msg__Trafficsignprediction __attribute__((deprecated))
#else
# define DEPRECATED__utils__msg__Trafficsignprediction __declspec(deprecated)
#endif

namespace utils
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Trafficsignprediction_
{
  using Type = Trafficsignprediction_<ContainerAllocator>;

  explicit Trafficsignprediction_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->prediction = "";
      this->conf = 0.0f;
    }
  }

  explicit Trafficsignprediction_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : prediction(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->prediction = "";
      this->conf = 0.0f;
    }
  }

  // field types and members
  using _prediction_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _prediction_type prediction;
  using _conf_type =
    float;
  _conf_type conf;

  // setters for named parameter idiom
  Type & set__prediction(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->prediction = _arg;
    return *this;
  }
  Type & set__conf(
    const float & _arg)
  {
    this->conf = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    utils::msg::Trafficsignprediction_<ContainerAllocator> *;
  using ConstRawPtr =
    const utils::msg::Trafficsignprediction_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<utils::msg::Trafficsignprediction_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<utils::msg::Trafficsignprediction_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      utils::msg::Trafficsignprediction_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<utils::msg::Trafficsignprediction_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      utils::msg::Trafficsignprediction_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<utils::msg::Trafficsignprediction_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<utils::msg::Trafficsignprediction_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<utils::msg::Trafficsignprediction_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__utils__msg__Trafficsignprediction
    std::shared_ptr<utils::msg::Trafficsignprediction_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__utils__msg__Trafficsignprediction
    std::shared_ptr<utils::msg::Trafficsignprediction_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Trafficsignprediction_ & other) const
  {
    if (this->prediction != other.prediction) {
      return false;
    }
    if (this->conf != other.conf) {
      return false;
    }
    return true;
  }
  bool operator!=(const Trafficsignprediction_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Trafficsignprediction_

// alias to use template instance with default allocator
using Trafficsignprediction =
  utils::msg::Trafficsignprediction_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace utils

#endif  // UTILS__MSG__DETAIL__TRAFFICSIGNPREDICTION__STRUCT_HPP_
