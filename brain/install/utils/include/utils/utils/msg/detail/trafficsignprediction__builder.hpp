// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from utils:msg/Trafficsignprediction.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/trafficsignprediction.hpp"


#ifndef UTILS__MSG__DETAIL__TRAFFICSIGNPREDICTION__BUILDER_HPP_
#define UTILS__MSG__DETAIL__TRAFFICSIGNPREDICTION__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "utils/msg/detail/trafficsignprediction__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace utils
{

namespace msg
{

namespace builder
{

class Init_Trafficsignprediction_conf
{
public:
  explicit Init_Trafficsignprediction_conf(::utils::msg::Trafficsignprediction & msg)
  : msg_(msg)
  {}
  ::utils::msg::Trafficsignprediction conf(::utils::msg::Trafficsignprediction::_conf_type arg)
  {
    msg_.conf = std::move(arg);
    return std::move(msg_);
  }

private:
  ::utils::msg::Trafficsignprediction msg_;
};

class Init_Trafficsignprediction_prediction
{
public:
  Init_Trafficsignprediction_prediction()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Trafficsignprediction_conf prediction(::utils::msg::Trafficsignprediction::_prediction_type arg)
  {
    msg_.prediction = std::move(arg);
    return Init_Trafficsignprediction_conf(msg_);
  }

private:
  ::utils::msg::Trafficsignprediction msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::utils::msg::Trafficsignprediction>()
{
  return utils::msg::builder::Init_Trafficsignprediction_prediction();
}

}  // namespace utils

#endif  // UTILS__MSG__DETAIL__TRAFFICSIGNPREDICTION__BUILDER_HPP_
