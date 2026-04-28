// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from utils:msg/Vehicles.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/vehicles.hpp"


#ifndef UTILS__MSG__DETAIL__VEHICLES__STRUCT_HPP_
#define UTILS__MSG__DETAIL__VEHICLES__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__utils__msg__Vehicles __attribute__((deprecated))
#else
# define DEPRECATED__utils__msg__Vehicles __declspec(deprecated)
#endif

namespace utils
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Vehicles_
{
  using Type = Vehicles_<ContainerAllocator>;

  explicit Vehicles_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0;
      this->timestamp = 0.0f;
      this->pos_a = 0.0f;
      this->pos_b = 0.0f;
      this->rot_a = 0.0f;
      this->rot_b = 0.0f;
    }
  }

  explicit Vehicles_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0;
      this->timestamp = 0.0f;
      this->pos_a = 0.0f;
      this->pos_b = 0.0f;
      this->rot_a = 0.0f;
      this->rot_b = 0.0f;
    }
  }

  // field types and members
  using _id_type =
    uint8_t;
  _id_type id;
  using _timestamp_type =
    float;
  _timestamp_type timestamp;
  using _pos_a_type =
    float;
  _pos_a_type pos_a;
  using _pos_b_type =
    float;
  _pos_b_type pos_b;
  using _rot_a_type =
    float;
  _rot_a_type rot_a;
  using _rot_b_type =
    float;
  _rot_b_type rot_b;

  // setters for named parameter idiom
  Type & set__id(
    const uint8_t & _arg)
  {
    this->id = _arg;
    return *this;
  }
  Type & set__timestamp(
    const float & _arg)
  {
    this->timestamp = _arg;
    return *this;
  }
  Type & set__pos_a(
    const float & _arg)
  {
    this->pos_a = _arg;
    return *this;
  }
  Type & set__pos_b(
    const float & _arg)
  {
    this->pos_b = _arg;
    return *this;
  }
  Type & set__rot_a(
    const float & _arg)
  {
    this->rot_a = _arg;
    return *this;
  }
  Type & set__rot_b(
    const float & _arg)
  {
    this->rot_b = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    utils::msg::Vehicles_<ContainerAllocator> *;
  using ConstRawPtr =
    const utils::msg::Vehicles_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<utils::msg::Vehicles_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<utils::msg::Vehicles_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      utils::msg::Vehicles_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<utils::msg::Vehicles_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      utils::msg::Vehicles_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<utils::msg::Vehicles_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<utils::msg::Vehicles_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<utils::msg::Vehicles_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__utils__msg__Vehicles
    std::shared_ptr<utils::msg::Vehicles_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__utils__msg__Vehicles
    std::shared_ptr<utils::msg::Vehicles_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Vehicles_ & other) const
  {
    if (this->id != other.id) {
      return false;
    }
    if (this->timestamp != other.timestamp) {
      return false;
    }
    if (this->pos_a != other.pos_a) {
      return false;
    }
    if (this->pos_b != other.pos_b) {
      return false;
    }
    if (this->rot_a != other.rot_a) {
      return false;
    }
    if (this->rot_b != other.rot_b) {
      return false;
    }
    return true;
  }
  bool operator!=(const Vehicles_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Vehicles_

// alias to use template instance with default allocator
using Vehicles =
  utils::msg::Vehicles_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace utils

#endif  // UTILS__MSG__DETAIL__VEHICLES__STRUCT_HPP_
