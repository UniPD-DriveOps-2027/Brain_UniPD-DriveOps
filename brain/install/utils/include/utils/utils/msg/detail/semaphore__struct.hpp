// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from utils:msg/Semaphore.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/semaphore.hpp"


#ifndef UTILS__MSG__DETAIL__SEMAPHORE__STRUCT_HPP_
#define UTILS__MSG__DETAIL__SEMAPHORE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__utils__msg__Semaphore __attribute__((deprecated))
#else
# define DEPRECATED__utils__msg__Semaphore __declspec(deprecated)
#endif

namespace utils
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Semaphore_
{
  using Type = Semaphore_<ContainerAllocator>;

  explicit Semaphore_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->state = 0;
      this->pos_x = 0.0f;
      this->pos_y = 0.0f;
    }
  }

  explicit Semaphore_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->state = 0;
      this->pos_x = 0.0f;
      this->pos_y = 0.0f;
    }
  }

  // field types and members
  using _state_type =
    uint8_t;
  _state_type state;
  using _pos_x_type =
    float;
  _pos_x_type pos_x;
  using _pos_y_type =
    float;
  _pos_y_type pos_y;

  // setters for named parameter idiom
  Type & set__state(
    const uint8_t & _arg)
  {
    this->state = _arg;
    return *this;
  }
  Type & set__pos_x(
    const float & _arg)
  {
    this->pos_x = _arg;
    return *this;
  }
  Type & set__pos_y(
    const float & _arg)
  {
    this->pos_y = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    utils::msg::Semaphore_<ContainerAllocator> *;
  using ConstRawPtr =
    const utils::msg::Semaphore_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<utils::msg::Semaphore_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<utils::msg::Semaphore_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      utils::msg::Semaphore_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<utils::msg::Semaphore_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      utils::msg::Semaphore_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<utils::msg::Semaphore_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<utils::msg::Semaphore_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<utils::msg::Semaphore_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__utils__msg__Semaphore
    std::shared_ptr<utils::msg::Semaphore_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__utils__msg__Semaphore
    std::shared_ptr<utils::msg::Semaphore_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Semaphore_ & other) const
  {
    if (this->state != other.state) {
      return false;
    }
    if (this->pos_x != other.pos_x) {
      return false;
    }
    if (this->pos_y != other.pos_y) {
      return false;
    }
    return true;
  }
  bool operator!=(const Semaphore_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Semaphore_

// alias to use template instance with default allocator
using Semaphore =
  utils::msg::Semaphore_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace utils

#endif  // UTILS__MSG__DETAIL__SEMAPHORE__STRUCT_HPP_
