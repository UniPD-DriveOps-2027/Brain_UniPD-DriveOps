// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from utils:srv/RequestParam.idl
// generated code does not contain a copyright notice
#include "utils/srv/detail/request_param__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `name`
#include "rosidl_runtime_c/string_functions.h"

bool
utils__srv__RequestParam_Request__init(utils__srv__RequestParam_Request * msg)
{
  if (!msg) {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__init(&msg->name)) {
    utils__srv__RequestParam_Request__fini(msg);
    return false;
  }
  return true;
}

void
utils__srv__RequestParam_Request__fini(utils__srv__RequestParam_Request * msg)
{
  if (!msg) {
    return;
  }
  // name
  rosidl_runtime_c__String__fini(&msg->name);
}

bool
utils__srv__RequestParam_Request__are_equal(const utils__srv__RequestParam_Request * lhs, const utils__srv__RequestParam_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->name), &(rhs->name)))
  {
    return false;
  }
  return true;
}

bool
utils__srv__RequestParam_Request__copy(
  const utils__srv__RequestParam_Request * input,
  utils__srv__RequestParam_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__copy(
      &(input->name), &(output->name)))
  {
    return false;
  }
  return true;
}

utils__srv__RequestParam_Request *
utils__srv__RequestParam_Request__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__srv__RequestParam_Request * msg = (utils__srv__RequestParam_Request *)allocator.allocate(sizeof(utils__srv__RequestParam_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(utils__srv__RequestParam_Request));
  bool success = utils__srv__RequestParam_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
utils__srv__RequestParam_Request__destroy(utils__srv__RequestParam_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    utils__srv__RequestParam_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
utils__srv__RequestParam_Request__Sequence__init(utils__srv__RequestParam_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__srv__RequestParam_Request * data = NULL;

  if (size) {
    data = (utils__srv__RequestParam_Request *)allocator.zero_allocate(size, sizeof(utils__srv__RequestParam_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = utils__srv__RequestParam_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        utils__srv__RequestParam_Request__fini(&data[i - 1]);
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
utils__srv__RequestParam_Request__Sequence__fini(utils__srv__RequestParam_Request__Sequence * array)
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
      utils__srv__RequestParam_Request__fini(&array->data[i]);
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

utils__srv__RequestParam_Request__Sequence *
utils__srv__RequestParam_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__srv__RequestParam_Request__Sequence * array = (utils__srv__RequestParam_Request__Sequence *)allocator.allocate(sizeof(utils__srv__RequestParam_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = utils__srv__RequestParam_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
utils__srv__RequestParam_Request__Sequence__destroy(utils__srv__RequestParam_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    utils__srv__RequestParam_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
utils__srv__RequestParam_Request__Sequence__are_equal(const utils__srv__RequestParam_Request__Sequence * lhs, const utils__srv__RequestParam_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!utils__srv__RequestParam_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
utils__srv__RequestParam_Request__Sequence__copy(
  const utils__srv__RequestParam_Request__Sequence * input,
  utils__srv__RequestParam_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(utils__srv__RequestParam_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    utils__srv__RequestParam_Request * data =
      (utils__srv__RequestParam_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!utils__srv__RequestParam_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          utils__srv__RequestParam_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!utils__srv__RequestParam_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `ints`
// Member `floats`
#include "rosidl_runtime_c/primitives_sequence_functions.h"
// Member `strings`
// already included above
// #include "rosidl_runtime_c/string_functions.h"

bool
utils__srv__RequestParam_Response__init(utils__srv__RequestParam_Response * msg)
{
  if (!msg) {
    return false;
  }
  // ints
  if (!rosidl_runtime_c__int32__Sequence__init(&msg->ints, 0)) {
    utils__srv__RequestParam_Response__fini(msg);
    return false;
  }
  // floats
  if (!rosidl_runtime_c__float__Sequence__init(&msg->floats, 0)) {
    utils__srv__RequestParam_Response__fini(msg);
    return false;
  }
  // strings
  if (!rosidl_runtime_c__String__Sequence__init(&msg->strings, 0)) {
    utils__srv__RequestParam_Response__fini(msg);
    return false;
  }
  return true;
}

void
utils__srv__RequestParam_Response__fini(utils__srv__RequestParam_Response * msg)
{
  if (!msg) {
    return;
  }
  // ints
  rosidl_runtime_c__int32__Sequence__fini(&msg->ints);
  // floats
  rosidl_runtime_c__float__Sequence__fini(&msg->floats);
  // strings
  rosidl_runtime_c__String__Sequence__fini(&msg->strings);
}

bool
utils__srv__RequestParam_Response__are_equal(const utils__srv__RequestParam_Response * lhs, const utils__srv__RequestParam_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // ints
  if (!rosidl_runtime_c__int32__Sequence__are_equal(
      &(lhs->ints), &(rhs->ints)))
  {
    return false;
  }
  // floats
  if (!rosidl_runtime_c__float__Sequence__are_equal(
      &(lhs->floats), &(rhs->floats)))
  {
    return false;
  }
  // strings
  if (!rosidl_runtime_c__String__Sequence__are_equal(
      &(lhs->strings), &(rhs->strings)))
  {
    return false;
  }
  return true;
}

bool
utils__srv__RequestParam_Response__copy(
  const utils__srv__RequestParam_Response * input,
  utils__srv__RequestParam_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // ints
  if (!rosidl_runtime_c__int32__Sequence__copy(
      &(input->ints), &(output->ints)))
  {
    return false;
  }
  // floats
  if (!rosidl_runtime_c__float__Sequence__copy(
      &(input->floats), &(output->floats)))
  {
    return false;
  }
  // strings
  if (!rosidl_runtime_c__String__Sequence__copy(
      &(input->strings), &(output->strings)))
  {
    return false;
  }
  return true;
}

utils__srv__RequestParam_Response *
utils__srv__RequestParam_Response__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__srv__RequestParam_Response * msg = (utils__srv__RequestParam_Response *)allocator.allocate(sizeof(utils__srv__RequestParam_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(utils__srv__RequestParam_Response));
  bool success = utils__srv__RequestParam_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
utils__srv__RequestParam_Response__destroy(utils__srv__RequestParam_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    utils__srv__RequestParam_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
utils__srv__RequestParam_Response__Sequence__init(utils__srv__RequestParam_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__srv__RequestParam_Response * data = NULL;

  if (size) {
    data = (utils__srv__RequestParam_Response *)allocator.zero_allocate(size, sizeof(utils__srv__RequestParam_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = utils__srv__RequestParam_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        utils__srv__RequestParam_Response__fini(&data[i - 1]);
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
utils__srv__RequestParam_Response__Sequence__fini(utils__srv__RequestParam_Response__Sequence * array)
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
      utils__srv__RequestParam_Response__fini(&array->data[i]);
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

utils__srv__RequestParam_Response__Sequence *
utils__srv__RequestParam_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__srv__RequestParam_Response__Sequence * array = (utils__srv__RequestParam_Response__Sequence *)allocator.allocate(sizeof(utils__srv__RequestParam_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = utils__srv__RequestParam_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
utils__srv__RequestParam_Response__Sequence__destroy(utils__srv__RequestParam_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    utils__srv__RequestParam_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
utils__srv__RequestParam_Response__Sequence__are_equal(const utils__srv__RequestParam_Response__Sequence * lhs, const utils__srv__RequestParam_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!utils__srv__RequestParam_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
utils__srv__RequestParam_Response__Sequence__copy(
  const utils__srv__RequestParam_Response__Sequence * input,
  utils__srv__RequestParam_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(utils__srv__RequestParam_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    utils__srv__RequestParam_Response * data =
      (utils__srv__RequestParam_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!utils__srv__RequestParam_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          utils__srv__RequestParam_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!utils__srv__RequestParam_Response__copy(
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
// #include "utils/srv/detail/request_param__functions.h"

bool
utils__srv__RequestParam_Event__init(utils__srv__RequestParam_Event * msg)
{
  if (!msg) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__init(&msg->info)) {
    utils__srv__RequestParam_Event__fini(msg);
    return false;
  }
  // request
  if (!utils__srv__RequestParam_Request__Sequence__init(&msg->request, 0)) {
    utils__srv__RequestParam_Event__fini(msg);
    return false;
  }
  // response
  if (!utils__srv__RequestParam_Response__Sequence__init(&msg->response, 0)) {
    utils__srv__RequestParam_Event__fini(msg);
    return false;
  }
  return true;
}

void
utils__srv__RequestParam_Event__fini(utils__srv__RequestParam_Event * msg)
{
  if (!msg) {
    return;
  }
  // info
  service_msgs__msg__ServiceEventInfo__fini(&msg->info);
  // request
  utils__srv__RequestParam_Request__Sequence__fini(&msg->request);
  // response
  utils__srv__RequestParam_Response__Sequence__fini(&msg->response);
}

bool
utils__srv__RequestParam_Event__are_equal(const utils__srv__RequestParam_Event * lhs, const utils__srv__RequestParam_Event * rhs)
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
  if (!utils__srv__RequestParam_Request__Sequence__are_equal(
      &(lhs->request), &(rhs->request)))
  {
    return false;
  }
  // response
  if (!utils__srv__RequestParam_Response__Sequence__are_equal(
      &(lhs->response), &(rhs->response)))
  {
    return false;
  }
  return true;
}

bool
utils__srv__RequestParam_Event__copy(
  const utils__srv__RequestParam_Event * input,
  utils__srv__RequestParam_Event * output)
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
  if (!utils__srv__RequestParam_Request__Sequence__copy(
      &(input->request), &(output->request)))
  {
    return false;
  }
  // response
  if (!utils__srv__RequestParam_Response__Sequence__copy(
      &(input->response), &(output->response)))
  {
    return false;
  }
  return true;
}

utils__srv__RequestParam_Event *
utils__srv__RequestParam_Event__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__srv__RequestParam_Event * msg = (utils__srv__RequestParam_Event *)allocator.allocate(sizeof(utils__srv__RequestParam_Event), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(utils__srv__RequestParam_Event));
  bool success = utils__srv__RequestParam_Event__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
utils__srv__RequestParam_Event__destroy(utils__srv__RequestParam_Event * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    utils__srv__RequestParam_Event__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
utils__srv__RequestParam_Event__Sequence__init(utils__srv__RequestParam_Event__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__srv__RequestParam_Event * data = NULL;

  if (size) {
    data = (utils__srv__RequestParam_Event *)allocator.zero_allocate(size, sizeof(utils__srv__RequestParam_Event), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = utils__srv__RequestParam_Event__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        utils__srv__RequestParam_Event__fini(&data[i - 1]);
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
utils__srv__RequestParam_Event__Sequence__fini(utils__srv__RequestParam_Event__Sequence * array)
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
      utils__srv__RequestParam_Event__fini(&array->data[i]);
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

utils__srv__RequestParam_Event__Sequence *
utils__srv__RequestParam_Event__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__srv__RequestParam_Event__Sequence * array = (utils__srv__RequestParam_Event__Sequence *)allocator.allocate(sizeof(utils__srv__RequestParam_Event__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = utils__srv__RequestParam_Event__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
utils__srv__RequestParam_Event__Sequence__destroy(utils__srv__RequestParam_Event__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    utils__srv__RequestParam_Event__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
utils__srv__RequestParam_Event__Sequence__are_equal(const utils__srv__RequestParam_Event__Sequence * lhs, const utils__srv__RequestParam_Event__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!utils__srv__RequestParam_Event__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
utils__srv__RequestParam_Event__Sequence__copy(
  const utils__srv__RequestParam_Event__Sequence * input,
  utils__srv__RequestParam_Event__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(utils__srv__RequestParam_Event);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    utils__srv__RequestParam_Event * data =
      (utils__srv__RequestParam_Event *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!utils__srv__RequestParam_Event__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          utils__srv__RequestParam_Event__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!utils__srv__RequestParam_Event__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
