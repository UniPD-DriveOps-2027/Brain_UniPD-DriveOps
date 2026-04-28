// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from utils:msg/Trafficsignprediction.idl
// generated code does not contain a copyright notice
#include "utils/msg/detail/trafficsignprediction__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `prediction`
#include "rosidl_runtime_c/string_functions.h"

bool
utils__msg__Trafficsignprediction__init(utils__msg__Trafficsignprediction * msg)
{
  if (!msg) {
    return false;
  }
  // prediction
  if (!rosidl_runtime_c__String__init(&msg->prediction)) {
    utils__msg__Trafficsignprediction__fini(msg);
    return false;
  }
  // conf
  return true;
}

void
utils__msg__Trafficsignprediction__fini(utils__msg__Trafficsignprediction * msg)
{
  if (!msg) {
    return;
  }
  // prediction
  rosidl_runtime_c__String__fini(&msg->prediction);
  // conf
}

bool
utils__msg__Trafficsignprediction__are_equal(const utils__msg__Trafficsignprediction * lhs, const utils__msg__Trafficsignprediction * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // prediction
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->prediction), &(rhs->prediction)))
  {
    return false;
  }
  // conf
  if (lhs->conf != rhs->conf) {
    return false;
  }
  return true;
}

bool
utils__msg__Trafficsignprediction__copy(
  const utils__msg__Trafficsignprediction * input,
  utils__msg__Trafficsignprediction * output)
{
  if (!input || !output) {
    return false;
  }
  // prediction
  if (!rosidl_runtime_c__String__copy(
      &(input->prediction), &(output->prediction)))
  {
    return false;
  }
  // conf
  output->conf = input->conf;
  return true;
}

utils__msg__Trafficsignprediction *
utils__msg__Trafficsignprediction__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__msg__Trafficsignprediction * msg = (utils__msg__Trafficsignprediction *)allocator.allocate(sizeof(utils__msg__Trafficsignprediction), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(utils__msg__Trafficsignprediction));
  bool success = utils__msg__Trafficsignprediction__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
utils__msg__Trafficsignprediction__destroy(utils__msg__Trafficsignprediction * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    utils__msg__Trafficsignprediction__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
utils__msg__Trafficsignprediction__Sequence__init(utils__msg__Trafficsignprediction__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__msg__Trafficsignprediction * data = NULL;

  if (size) {
    data = (utils__msg__Trafficsignprediction *)allocator.zero_allocate(size, sizeof(utils__msg__Trafficsignprediction), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = utils__msg__Trafficsignprediction__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        utils__msg__Trafficsignprediction__fini(&data[i - 1]);
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
utils__msg__Trafficsignprediction__Sequence__fini(utils__msg__Trafficsignprediction__Sequence * array)
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
      utils__msg__Trafficsignprediction__fini(&array->data[i]);
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

utils__msg__Trafficsignprediction__Sequence *
utils__msg__Trafficsignprediction__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__msg__Trafficsignprediction__Sequence * array = (utils__msg__Trafficsignprediction__Sequence *)allocator.allocate(sizeof(utils__msg__Trafficsignprediction__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = utils__msg__Trafficsignprediction__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
utils__msg__Trafficsignprediction__Sequence__destroy(utils__msg__Trafficsignprediction__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    utils__msg__Trafficsignprediction__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
utils__msg__Trafficsignprediction__Sequence__are_equal(const utils__msg__Trafficsignprediction__Sequence * lhs, const utils__msg__Trafficsignprediction__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!utils__msg__Trafficsignprediction__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
utils__msg__Trafficsignprediction__Sequence__copy(
  const utils__msg__Trafficsignprediction__Sequence * input,
  utils__msg__Trafficsignprediction__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(utils__msg__Trafficsignprediction);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    utils__msg__Trafficsignprediction * data =
      (utils__msg__Trafficsignprediction *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!utils__msg__Trafficsignprediction__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          utils__msg__Trafficsignprediction__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!utils__msg__Trafficsignprediction__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
