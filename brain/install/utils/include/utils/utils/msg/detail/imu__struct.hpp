// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from utils:msg/IMU.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/imu.hpp"


#ifndef UTILS__MSG__DETAIL__IMU__STRUCT_HPP_
#define UTILS__MSG__DETAIL__IMU__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__utils__msg__IMU __attribute__((deprecated))
#else
# define DEPRECATED__utils__msg__IMU __declspec(deprecated)
#endif

namespace utils
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct IMU_
{
  using Type = IMU_<ContainerAllocator>;

  explicit IMU_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->roll = 0.0f;
      this->pitch = 0.0f;
      this->yaw = 0.0f;
      this->accelx = 0.0f;
      this->accely = 0.0f;
      this->accelz = 0.0f;
      this->gyrox = 0.0f;
      this->gyroy = 0.0f;
      this->gyroz = 0.0f;
    }
  }

  explicit IMU_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->roll = 0.0f;
      this->pitch = 0.0f;
      this->yaw = 0.0f;
      this->accelx = 0.0f;
      this->accely = 0.0f;
      this->accelz = 0.0f;
      this->gyrox = 0.0f;
      this->gyroy = 0.0f;
      this->gyroz = 0.0f;
    }
  }

  // field types and members
  using _roll_type =
    float;
  _roll_type roll;
  using _pitch_type =
    float;
  _pitch_type pitch;
  using _yaw_type =
    float;
  _yaw_type yaw;
  using _accelx_type =
    float;
  _accelx_type accelx;
  using _accely_type =
    float;
  _accely_type accely;
  using _accelz_type =
    float;
  _accelz_type accelz;
  using _gyrox_type =
    float;
  _gyrox_type gyrox;
  using _gyroy_type =
    float;
  _gyroy_type gyroy;
  using _gyroz_type =
    float;
  _gyroz_type gyroz;

  // setters for named parameter idiom
  Type & set__roll(
    const float & _arg)
  {
    this->roll = _arg;
    return *this;
  }
  Type & set__pitch(
    const float & _arg)
  {
    this->pitch = _arg;
    return *this;
  }
  Type & set__yaw(
    const float & _arg)
  {
    this->yaw = _arg;
    return *this;
  }
  Type & set__accelx(
    const float & _arg)
  {
    this->accelx = _arg;
    return *this;
  }
  Type & set__accely(
    const float & _arg)
  {
    this->accely = _arg;
    return *this;
  }
  Type & set__accelz(
    const float & _arg)
  {
    this->accelz = _arg;
    return *this;
  }
  Type & set__gyrox(
    const float & _arg)
  {
    this->gyrox = _arg;
    return *this;
  }
  Type & set__gyroy(
    const float & _arg)
  {
    this->gyroy = _arg;
    return *this;
  }
  Type & set__gyroz(
    const float & _arg)
  {
    this->gyroz = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    utils::msg::IMU_<ContainerAllocator> *;
  using ConstRawPtr =
    const utils::msg::IMU_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<utils::msg::IMU_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<utils::msg::IMU_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      utils::msg::IMU_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<utils::msg::IMU_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      utils::msg::IMU_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<utils::msg::IMU_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<utils::msg::IMU_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<utils::msg::IMU_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__utils__msg__IMU
    std::shared_ptr<utils::msg::IMU_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__utils__msg__IMU
    std::shared_ptr<utils::msg::IMU_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const IMU_ & other) const
  {
    if (this->roll != other.roll) {
      return false;
    }
    if (this->pitch != other.pitch) {
      return false;
    }
    if (this->yaw != other.yaw) {
      return false;
    }
    if (this->accelx != other.accelx) {
      return false;
    }
    if (this->accely != other.accely) {
      return false;
    }
    if (this->accelz != other.accelz) {
      return false;
    }
    if (this->gyrox != other.gyrox) {
      return false;
    }
    if (this->gyroy != other.gyroy) {
      return false;
    }
    if (this->gyroz != other.gyroz) {
      return false;
    }
    return true;
  }
  bool operator!=(const IMU_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct IMU_

// alias to use template instance with default allocator
using IMU =
  utils::msg::IMU_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace utils

#endif  // UTILS__MSG__DETAIL__IMU__STRUCT_HPP_
