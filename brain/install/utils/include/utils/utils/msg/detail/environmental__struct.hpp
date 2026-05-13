// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from utils:msg/Environmental.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/environmental.hpp"


#ifndef UTILS__MSG__DETAIL__ENVIRONMENTAL__STRUCT_HPP_
#define UTILS__MSG__DETAIL__ENVIRONMENTAL__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__utils__msg__Environmental __attribute__((deprecated))
#else
# define DEPRECATED__utils__msg__Environmental __declspec(deprecated)
#endif

namespace utils
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Environmental_
{
  using Type = Environmental_<ContainerAllocator>;

  explicit Environmental_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->obstacle_id = 0;
      this->x = 0.0f;
      this->y = 0.0f;
    }
  }

  explicit Environmental_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->obstacle_id = 0;
      this->x = 0.0f;
      this->y = 0.0f;
    }
  }

  // field types and members
  using _obstacle_id_type =
    uint8_t;
  _obstacle_id_type obstacle_id;
  using _x_type =
    float;
  _x_type x;
  using _y_type =
    float;
  _y_type y;

  // setters for named parameter idiom
  Type & set__obstacle_id(
    const uint8_t & _arg)
  {
    this->obstacle_id = _arg;
    return *this;
  }
  Type & set__x(
    const float & _arg)
  {
    this->x = _arg;
    return *this;
  }
  Type & set__y(
    const float & _arg)
  {
    this->y = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    utils::msg::Environmental_<ContainerAllocator> *;
  using ConstRawPtr =
    const utils::msg::Environmental_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<utils::msg::Environmental_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<utils::msg::Environmental_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      utils::msg::Environmental_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<utils::msg::Environmental_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      utils::msg::Environmental_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<utils::msg::Environmental_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<utils::msg::Environmental_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<utils::msg::Environmental_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__utils__msg__Environmental
    std::shared_ptr<utils::msg::Environmental_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__utils__msg__Environmental
    std::shared_ptr<utils::msg::Environmental_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Environmental_ & other) const
  {
    if (this->obstacle_id != other.obstacle_id) {
      return false;
    }
    if (this->x != other.x) {
      return false;
    }
    if (this->y != other.y) {
      return false;
    }
    return true;
  }
  bool operator!=(const Environmental_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Environmental_

// alias to use template instance with default allocator
using Environmental =
  utils::msg::Environmental_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace utils

#endif  // UTILS__MSG__DETAIL__ENVIRONMENTAL__STRUCT_HPP_
