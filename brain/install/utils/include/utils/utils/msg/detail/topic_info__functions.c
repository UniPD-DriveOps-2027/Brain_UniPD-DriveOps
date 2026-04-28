// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from utils:msg/TopicInfo.idl
// generated code does not contain a copyright notice
#include "utils/msg/detail/topic_info__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `topic_name`
// Member `message_type`
// Member `md5sum`
#include "rosidl_runtime_c/string_functions.h"

bool
utils__msg__TopicInfo__init(utils__msg__TopicInfo * msg)
{
  if (!msg) {
    return false;
  }
  // topic_id
  // topic_name
  if (!rosidl_runtime_c__String__init(&msg->topic_name)) {
    utils__msg__TopicInfo__fini(msg);
    return false;
  }
  // message_type
  if (!rosidl_runtime_c__String__init(&msg->message_type)) {
    utils__msg__TopicInfo__fini(msg);
    return false;
  }
  // md5sum
  if (!rosidl_runtime_c__String__init(&msg->md5sum)) {
    utils__msg__TopicInfo__fini(msg);
    return false;
  }
  // buffer_size
  return true;
}

void
utils__msg__TopicInfo__fini(utils__msg__TopicInfo * msg)
{
  if (!msg) {
    return;
  }
  // topic_id
  // topic_name
  rosidl_runtime_c__String__fini(&msg->topic_name);
  // message_type
  rosidl_runtime_c__String__fini(&msg->message_type);
  // md5sum
  rosidl_runtime_c__String__fini(&msg->md5sum);
  // buffer_size
}

bool
utils__msg__TopicInfo__are_equal(const utils__msg__TopicInfo * lhs, const utils__msg__TopicInfo * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // topic_id
  if (lhs->topic_id != rhs->topic_id) {
    return false;
  }
  // topic_name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->topic_name), &(rhs->topic_name)))
  {
    return false;
  }
  // message_type
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->message_type), &(rhs->message_type)))
  {
    return false;
  }
  // md5sum
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->md5sum), &(rhs->md5sum)))
  {
    return false;
  }
  // buffer_size
  if (lhs->buffer_size != rhs->buffer_size) {
    return false;
  }
  return true;
}

bool
utils__msg__TopicInfo__copy(
  const utils__msg__TopicInfo * input,
  utils__msg__TopicInfo * output)
{
  if (!input || !output) {
    return false;
  }
  // topic_id
  output->topic_id = input->topic_id;
  // topic_name
  if (!rosidl_runtime_c__String__copy(
      &(input->topic_name), &(output->topic_name)))
  {
    return false;
  }
  // message_type
  if (!rosidl_runtime_c__String__copy(
      &(input->message_type), &(output->message_type)))
  {
    return false;
  }
  // md5sum
  if (!rosidl_runtime_c__String__copy(
      &(input->md5sum), &(output->md5sum)))
  {
    return false;
  }
  // buffer_size
  output->buffer_size = input->buffer_size;
  return true;
}

utils__msg__TopicInfo *
utils__msg__TopicInfo__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__msg__TopicInfo * msg = (utils__msg__TopicInfo *)allocator.allocate(sizeof(utils__msg__TopicInfo), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(utils__msg__TopicInfo));
  bool success = utils__msg__TopicInfo__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
utils__msg__TopicInfo__destroy(utils__msg__TopicInfo * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    utils__msg__TopicInfo__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
utils__msg__TopicInfo__Sequence__init(utils__msg__TopicInfo__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__msg__TopicInfo * data = NULL;

  if (size) {
    data = (utils__msg__TopicInfo *)allocator.zero_allocate(size, sizeof(utils__msg__TopicInfo), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = utils__msg__TopicInfo__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        utils__msg__TopicInfo__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
utils__msg__TopicInfo__Sequence__fini(utils__msg__TopicInfo__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      utils__msg__TopicInfo__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

utils__msg__TopicInfo__Sequence *
utils__msg__TopicInfo__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__msg__TopicInfo__Sequence * array = (utils__msg__TopicInfo__Sequence *)allocator.allocate(sizeof(utils__msg__TopicInfo__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = utils__msg__TopicInfo__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
utils__msg__TopicInfo__Sequence__destroy(utils__msg__TopicInfo__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    utils__msg__TopicInfo__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
utils__msg__TopicInfo__Sequence__are_equal(const utils__msg__TopicInfo__Sequence * lhs, const utils__msg__TopicInfo__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!utils__msg__TopicInfo__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
utils__msg__TopicInfo__Sequence__copy(
  const utils__msg__TopicInfo__Sequence * input,
  utils__msg__TopicInfo__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(utils__msg__TopicInfo);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    utils__msg__TopicInfo * data =
      (utils__msg__TopicInfo *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!utils__msg__TopicInfo__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          utils__msg__TopicInfo__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!utils__msg__TopicInfo__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
