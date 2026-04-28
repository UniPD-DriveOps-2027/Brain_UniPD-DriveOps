// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from utils:msg/Conditions.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/conditions.hpp"


#ifndef UTILS__MSG__DETAIL__CONDITIONS__STRUCT_HPP_
#define UTILS__MSG__DETAIL__CONDITIONS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__utils__msg__Conditions __attribute__((deprecated))
#else
# define DEPRECATED__utils__msg__Conditions __declspec(deprecated)
#endif

namespace utils
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Conditions_
{
  using Type = Conditions_<ContainerAllocator>;

  explicit Conditions_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->can_overtake = false;
      this->highway = false;
      this->car_on_path = false;
      this->rerouting = false;
      this->tunnel = false;
    }
  }

  explicit Conditions_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->can_overtake = false;
      this->highway = false;
      this->car_on_path = false;
      this->rerouting = false;
      this->tunnel = false;
    }
  }

  // field types and members
  using _can_overtake_type =
    bool;
  _can_overtake_type can_overtake;
  using _highway_type =
    bool;
  _highway_type highway;
  using _car_on_path_type =
    bool;
  _car_on_path_type car_on_path;
  using _rerouting_type =
    bool;
  _rerouting_type rerouting;
  using _tunnel_type =
    bool;
  _tunnel_type tunnel;

  // setters for named parameter idiom
  Type & set__can_overtake(
    const bool & _arg)
  {
    this->can_overtake = _arg;
    return *this;
  }
  Type & set__highway(
    const bool & _arg)
  {
    this->highway = _arg;
    return *this;
  }
  Type & set__car_on_path(
    const bool & _arg)
  {
    this->car_on_path = _arg;
    return *this;
  }
  Type & set__rerouting(
    const bool & _arg)
  {
    this->rerouting = _arg;
    return *this;
  }
  Type & set__tunnel(
    const bool & _arg)
  {
    this->tunnel = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    utils::msg::Conditions_<ContainerAllocator> *;
  using ConstRawPtr =
    const utils::msg::Conditions_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<utils::msg::Conditions_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<utils::msg::Conditions_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      utils::msg::Conditions_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<utils::msg::Conditions_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      utils::msg::Conditions_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<utils::msg::Conditions_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<utils::msg::Conditions_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<utils::msg::Conditions_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__utils__msg__Conditions
    std::shared_ptr<utils::msg::Conditions_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__utils__msg__Conditions
    std::shared_ptr<utils::msg::Conditions_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Conditions_ & other) const
  {
    if (this->can_overtake != other.can_overtake) {
      return false;
    }
    if (this->highway != other.highway) {
      return false;
    }
    if (this->car_on_path != other.car_on_path) {
      return false;
    }
    if (this->rerouting != other.rerouting) {
      return false;
    }
    if (this->tunnel != other.tunnel) {
      return false;
    }
    return true;
  }
  bool operator!=(const Conditions_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Conditions_

// alias to use template instance with default allocator
using Conditions =
  utils::msg::Conditions_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace utils

#endif  // UTILS__MSG__DETAIL__CONDITIONS__STRUCT_HPP_
