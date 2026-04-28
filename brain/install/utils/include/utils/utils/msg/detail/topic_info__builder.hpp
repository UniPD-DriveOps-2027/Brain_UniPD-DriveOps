// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from utils:msg/TopicInfo.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "utils/msg/topic_info.hpp"


#ifndef UTILS__MSG__DETAIL__TOPIC_INFO__BUILDER_HPP_
#define UTILS__MSG__DETAIL__TOPIC_INFO__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "utils/msg/detail/topic_info__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace utils
{

namespace msg
{

namespace builder
{

class Init_TopicInfo_buffer_size
{
public:
  explicit Init_TopicInfo_buffer_size(::utils::msg::TopicInfo & msg)
  : msg_(msg)
  {}
  ::utils::msg::TopicInfo buffer_size(::utils::msg::TopicInfo::_buffer_size_type arg)
  {
    msg_.buffer_size = std::move(arg);
    return std::move(msg_);
  }

private:
  ::utils::msg::TopicInfo msg_;
};

class Init_TopicInfo_md5sum
{
public:
  explicit Init_TopicInfo_md5sum(::utils::msg::TopicInfo & msg)
  : msg_(msg)
  {}
  Init_TopicInfo_buffer_size md5sum(::utils::msg::TopicInfo::_md5sum_type arg)
  {
    msg_.md5sum = std::move(arg);
    return Init_TopicInfo_buffer_size(msg_);
  }

private:
  ::utils::msg::TopicInfo msg_;
};

class Init_TopicInfo_message_type
{
public:
  explicit Init_TopicInfo_message_type(::utils::msg::TopicInfo & msg)
  : msg_(msg)
  {}
  Init_TopicInfo_md5sum message_type(::utils::msg::TopicInfo::_message_type_type arg)
  {
    msg_.message_type = std::move(arg);
    return Init_TopicInfo_md5sum(msg_);
  }

private:
  ::utils::msg::TopicInfo msg_;
};

class Init_TopicInfo_topic_name
{
public:
  explicit Init_TopicInfo_topic_name(::utils::msg::TopicInfo & msg)
  : msg_(msg)
  {}
  Init_TopicInfo_message_type topic_name(::utils::msg::TopicInfo::_topic_name_type arg)
  {
    msg_.topic_name = std::move(arg);
    return Init_TopicInfo_message_type(msg_);
  }

private:
  ::utils::msg::TopicInfo msg_;
};

class Init_TopicInfo_topic_id
{
public:
  Init_TopicInfo_topic_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TopicInfo_topic_name topic_id(::utils::msg::TopicInfo::_topic_id_type arg)
  {
    msg_.topic_id = std::move(arg);
    return Init_TopicInfo_topic_name(msg_);
  }

private:
  ::utils::msg::TopicInfo msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::utils::msg::TopicInfo>()
{
  return utils::msg::builder::Init_TopicInfo_topic_id();
}

}  // namespace utils

#endif  // UTILS__MSG__DETAIL__TOPIC_INFO__BUILDER_HPP_
