// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from utils:msg/Localisation.idl
// generated code does not contain a copyright notice
#include "utils/msg/detail/localisation__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
utils__msg__Localisation__init(utils__msg__Localisation * msg)
{
  if (!msg) {
    return false;
  }
  // timestamp
  // pos_a
  // pos_b
  // rot_a
  // rot_b
  return true;
}

void
utils__msg__Localisation__fini(utils__msg__Localisation * msg)
{
  if (!msg) {
    return;
  }
  // timestamp
  // pos_a
  // pos_b
  // rot_a
  // rot_b
}

bool
utils__msg__Localisation__are_equal(const utils__msg__Localisation * lhs, const utils__msg__Localisation * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // timestamp
  if (lhs->timestamp != rhs->timestamp) {
    return false;
  }
  // pos_a
  if (lhs->pos_a != rhs->pos_a) {
    return false;
  }
  // pos_b
  if (lhs->pos_b != rhs->pos_b) {
    return false;
  }
  // rot_a
  if (lhs->rot_a != rhs->rot_a) {
    return false;
  }
  // rot_b
  if (lhs->rot_b != rhs->rot_b) {
    return false;
  }
  return true;
}

bool
utils__msg__Localisation__copy(
  const utils__msg__Localisation * input,
  utils__msg__Localisation * output)
{
  if (!input || !output) {
    return false;
  }
  // timestamp
  output->timestamp = input->timestamp;
  // pos_a
  output->pos_a = input->pos_a;
  // pos_b
  output->pos_b = input->pos_b;
  // rot_a
  output->rot_a = input->rot_a;
  // rot_b
  output->rot_b = input->rot_b;
  return true;
}

utils__msg__Localisation *
utils__msg__Localisation__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__msg__Localisation * msg = (utils__msg__Localisation *)allocator.allocate(sizeof(utils__msg__Localisation), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(utils__msg__Localisation));
  bool success = utils__msg__Localisation__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
utils__msg__Localisation__destroy(utils__msg__Localisation * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    utils__msg__Localisation__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
utils__msg__Localisation__Sequence__init(utils__msg__Localisation__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__msg__Localisation * data = NULL;

  if (size) {
    data = (utils__msg__Localisation *)allocator.zero_allocate(size, sizeof(utils__msg__Localisation), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = utils__msg__Localisation__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        utils__msg__Localisation__fini(&data[i - 1]);
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
utils__msg__Localisation__Sequence__fini(utils__msg__Localisation__Sequence * array)
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
      utils__msg__Localisation__fini(&array->data[i]);
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

utils__msg__Localisation__Sequence *
utils__msg__Localisation__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__msg__Localisation__Sequence * array = (utils__msg__Localisation__Sequence *)allocator.allocate(sizeof(utils__msg__Localisation__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = utils__msg__Localisation__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
utils__msg__Localisation__Sequence__destroy(utils__msg__Localisation__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    utils__msg__Localisation__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
utils__msg__Localisation__Sequence__are_equal(const utils__msg__Localisation__Sequence * lhs, const utils__msg__Localisation__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!utils__msg__Localisation__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
utils__msg__Localisation__Sequence__copy(
  const utils__msg__Localisation__Sequence * input,
  utils__msg__Localisation__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(utils__msg__Localisation);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    utils__msg__Localisation * data =
      (utils__msg__Localisation *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!utils__msg__Localisation__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          utils__msg__Localisation__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!utils__msg__Localisation__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
