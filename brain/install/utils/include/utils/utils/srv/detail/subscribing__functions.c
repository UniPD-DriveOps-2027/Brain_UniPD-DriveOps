// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from utils:srv/Subscribing.idl
// generated code does not contain a copyright notice
#include "utils/srv/detail/subscribing__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `code`
// Member `topic`
#include "rosidl_runtime_c/string_functions.h"

bool
utils__srv__Subscribing_Request__init(utils__srv__Subscribing_Request * msg)
{
  if (!msg) {
    return false;
  }
  // subscribing
  // code
  if (!rosidl_runtime_c__String__init(&msg->code)) {
    utils__srv__Subscribing_Request__fini(msg);
    return false;
  }
  // topic
  if (!rosidl_runtime_c__String__init(&msg->topic)) {
    utils__srv__Subscribing_Request__fini(msg);
    return false;
  }
  return true;
}

void
utils__srv__Subscribing_Request__fini(utils__srv__Subscribing_Request * msg)
{
  if (!msg) {
    return;
  }
  // subscribing
  // code
  rosidl_runtime_c__String__fini(&msg->code);
  // topic
  rosidl_runtime_c__String__fini(&msg->topic);
}

bool
utils__srv__Subscribing_Request__are_equal(const utils__srv__Subscribing_Request * lhs, const utils__srv__Subscribing_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // subscribing
  if (lhs->subscribing != rhs->subscribing) {
    return false;
  }
  // code
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->code), &(rhs->code)))
  {
    return false;
  }
  // topic
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->topic), &(rhs->topic)))
  {
    return false;
  }
  return true;
}

bool
utils__srv__Subscribing_Request__copy(
  const utils__srv__Subscribing_Request * input,
  utils__srv__Subscribing_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // subscribing
  output->subscribing = input->subscribing;
  // code
  if (!rosidl_runtime_c__String__copy(
      &(input->code), &(output->code)))
  {
    return false;
  }
  // topic
  if (!rosidl_runtime_c__String__copy(
      &(input->topic), &(output->topic)))
  {
    return false;
  }
  return true;
}

utils__srv__Subscribing_Request *
utils__srv__Subscribing_Request__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__srv__Subscribing_Request * msg = (utils__srv__Subscribing_Request *)allocator.allocate(sizeof(utils__srv__Subscribing_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(utils__srv__Subscribing_Request));
  bool success = utils__srv__Subscribing_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
utils__srv__Subscribing_Request__destroy(utils__srv__Subscribing_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    utils__srv__Subscribing_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
utils__srv__Subscribing_Request__Sequence__init(utils__srv__Subscribing_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__srv__Subscribing_Request * data = NULL;

  if (size) {
    data = (utils__srv__Subscribing_Request *)allocator.zero_allocate(size, sizeof(utils__srv__Subscribing_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = utils__srv__Subscribing_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        utils__srv__Subscribing_Request__fini(&data[i - 1]);
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
utils__srv__Subscribing_Request__Sequence__fini(utils__srv__Subscribing_Request__Sequence * array)
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
      utils__srv__Subscribing_Request__fini(&array->data[i]);
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

utils__srv__Subscribing_Request__Sequence *
utils__srv__Subscribing_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__srv__Subscribing_Request__Sequence * array = (utils__srv__Subscribing_Request__Sequence *)allocator.allocate(sizeof(utils__srv__Subscribing_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = utils__srv__Subscribing_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
utils__srv__Subscribing_Request__Sequence__destroy(utils__srv__Subscribing_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    utils__srv__Subscribing_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
utils__srv__Subscribing_Request__Sequence__are_equal(const utils__srv__Subscribing_Request__Sequence * lhs, const utils__srv__Subscribing_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!utils__srv__Subscribing_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
utils__srv__Subscribing_Request__Sequence__copy(
  const utils__srv__Subscribing_Request__Sequence * input,
  utils__srv__Subscribing_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(utils__srv__Subscribing_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    utils__srv__Subscribing_Request * data =
      (utils__srv__Subscribing_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!utils__srv__Subscribing_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          utils__srv__Subscribing_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!utils__srv__Subscribing_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
utils__srv__Subscribing_Response__init(utils__srv__Subscribing_Response * msg)
{
  if (!msg) {
    return false;
  }
  // topic
  return true;
}

void
utils__srv__Subscribing_Response__fini(utils__srv__Subscribing_Response * msg)
{
  if (!msg) {
    return;
  }
  // topic
}

bool
utils__srv__Subscribing_Response__are_equal(const utils__srv__Subscribing_Response * lhs, const utils__srv__Subscribing_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // topic
  if (lhs->topic != rhs->topic) {
    return false;
  }
  return true;
}

bool
utils__srv__Subscribing_Response__copy(
  const utils__srv__Subscribing_Response * input,
  utils__srv__Subscribing_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // topic
  output->topic = input->topic;
  return true;
}

utils__srv__Subscribing_Response *
utils__srv__Subscribing_Response__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__srv__Subscribing_Response * msg = (utils__srv__Subscribing_Response *)allocator.allocate(sizeof(utils__srv__Subscribing_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(utils__srv__Subscribing_Response));
  bool success = utils__srv__Subscribing_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
utils__srv__Subscribing_Response__destroy(utils__srv__Subscribing_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    utils__srv__Subscribing_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
utils__srv__Subscribing_Response__Sequence__init(utils__srv__Subscribing_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__srv__Subscribing_Response * data = NULL;

  if (size) {
    data = (utils__srv__Subscribing_Response *)allocator.zero_allocate(size, sizeof(utils__srv__Subscribing_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = utils__srv__Subscribing_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        utils__srv__Subscribing_Response__fini(&data[i - 1]);
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
utils__srv__Subscribing_Response__Sequence__fini(utils__srv__Subscribing_Response__Sequence * array)
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
      utils__srv__Subscribing_Response__fini(&array->data[i]);
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

utils__srv__Subscribing_Response__Sequence *
utils__srv__Subscribing_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__srv__Subscribing_Response__Sequence * array = (utils__srv__Subscribing_Response__Sequence *)allocator.allocate(sizeof(utils__srv__Subscribing_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = utils__srv__Subscribing_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
utils__srv__Subscribing_Response__Sequence__destroy(utils__srv__Subscribing_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    utils__srv__Subscribing_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
utils__srv__Subscribing_Response__Sequence__are_equal(const utils__srv__Subscribing_Response__Sequence * lhs, const utils__srv__Subscribing_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!utils__srv__Subscribing_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
utils__srv__Subscribing_Response__Sequence__copy(
  const utils__srv__Subscribing_Response__Sequence * input,
  utils__srv__Subscribing_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(utils__srv__Subscribing_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    utils__srv__Subscribing_Response * data =
      (utils__srv__Subscribing_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!utils__srv__Subscribing_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          utils__srv__Subscribing_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!utils__srv__Subscribing_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `info`
#include "service_msgs/msg/detail/service_event_info__functions.h"
// Member `request`
// Member `response`
// already included above
// #include "utils/srv/detail/subscribing__functions.h"

bool
utils__srv__Subscribing_Event__init(utils__srv__Subscribing_Event * msg)
{
  if (!msg) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__init(&msg->info)) {
    utils__srv__Subscribing_Event__fini(msg);
    return false;
  }
  // request
  if (!utils__srv__Subscribing_Request__Sequence__init(&msg->request, 0)) {
    utils__srv__Subscribing_Event__fini(msg);
    return false;
  }
  // response
  if (!utils__srv__Subscribing_Response__Sequence__init(&msg->response, 0)) {
    utils__srv__Subscribing_Event__fini(msg);
    return false;
  }
  return true;
}

void
utils__srv__Subscribing_Event__fini(utils__srv__Subscribing_Event * msg)
{
  if (!msg) {
    return;
  }
  // info
  service_msgs__msg__ServiceEventInfo__fini(&msg->info);
  // request
  utils__srv__Subscribing_Request__Sequence__fini(&msg->request);
  // response
  utils__srv__Subscribing_Response__Sequence__fini(&msg->response);
}

bool
utils__srv__Subscribing_Event__are_equal(const utils__srv__Subscribing_Event * lhs, const utils__srv__Subscribing_Event * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__are_equal(
      &(lhs->info), &(rhs->info)))
  {
    return false;
  }
  // request
  if (!utils__srv__Subscribing_Request__Sequence__are_equal(
      &(lhs->request), &(rhs->request)))
  {
    return false;
  }
  // response
  if (!utils__srv__Subscribing_Response__Sequence__are_equal(
      &(lhs->response), &(rhs->response)))
  {
    return false;
  }
  return true;
}

bool
utils__srv__Subscribing_Event__copy(
  const utils__srv__Subscribing_Event * input,
  utils__srv__Subscribing_Event * output)
{
  if (!input || !output) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__copy(
      &(input->info), &(output->info)))
  {
    return false;
  }
  // request
  if (!utils__srv__Subscribing_Request__Sequence__copy(
      &(input->request), &(output->request)))
  {
    return false;
  }
  // response
  if (!utils__srv__Subscribing_Response__Sequence__copy(
      &(input->response), &(output->response)))
  {
    return false;
  }
  return true;
}

utils__srv__Subscribing_Event *
utils__srv__Subscribing_Event__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__srv__Subscribing_Event * msg = (utils__srv__Subscribing_Event *)allocator.allocate(sizeof(utils__srv__Subscribing_Event), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(utils__srv__Subscribing_Event));
  bool success = utils__srv__Subscribing_Event__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
utils__srv__Subscribing_Event__destroy(utils__srv__Subscribing_Event * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    utils__srv__Subscribing_Event__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
utils__srv__Subscribing_Event__Sequence__init(utils__srv__Subscribing_Event__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__srv__Subscribing_Event * data = NULL;

  if (size) {
    data = (utils__srv__Subscribing_Event *)allocator.zero_allocate(size, sizeof(utils__srv__Subscribing_Event), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = utils__srv__Subscribing_Event__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        utils__srv__Subscribing_Event__fini(&data[i - 1]);
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
utils__srv__Subscribing_Event__Sequence__fini(utils__srv__Subscribing_Event__Sequence * array)
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
      utils__srv__Subscribing_Event__fini(&array->data[i]);
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

utils__srv__Subscribing_Event__Sequence *
utils__srv__Subscribing_Event__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__srv__Subscribing_Event__Sequence * array = (utils__srv__Subscribing_Event__Sequence *)allocator.allocate(sizeof(utils__srv__Subscribing_Event__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = utils__srv__Subscribing_Event__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
utils__srv__Subscribing_Event__Sequence__destroy(utils__srv__Subscribing_Event__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    utils__srv__Subscribing_Event__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
utils__srv__Subscribing_Event__Sequence__are_equal(const utils__srv__Subscribing_Event__Sequence * lhs, const utils__srv__Subscribing_Event__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!utils__srv__Subscribing_Event__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
utils__srv__Subscribing_Event__Sequence__copy(
  const utils__srv__Subscribing_Event__Sequence * input,
  utils__srv__Subscribing_Event__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(utils__srv__Subscribing_Event);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    utils__srv__Subscribing_Event * data =
      (utils__srv__Subscribing_Event *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!utils__srv__Subscribing_Event__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          utils__srv__Subscribing_Event__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!utils__srv__Subscribing_Event__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
