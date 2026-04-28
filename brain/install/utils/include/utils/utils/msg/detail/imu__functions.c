// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from utils:msg/IMU.idl
// generated code does not contain a copyright notice
#include "utils/msg/detail/imu__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
utils__msg__IMU__init(utils__msg__IMU * msg)
{
  if (!msg) {
    return false;
  }
  // roll
  // pitch
  // yaw
  // accelx
  // accely
  // accelz
  // gyrox
  // gyroy
  // gyroz
  return true;
}

void
utils__msg__IMU__fini(utils__msg__IMU * msg)
{
  if (!msg) {
    return;
  }
  // roll
  // pitch
  // yaw
  // accelx
  // accely
  // accelz
  // gyrox
  // gyroy
  // gyroz
}

bool
utils__msg__IMU__are_equal(const utils__msg__IMU * lhs, const utils__msg__IMU * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // roll
  if (lhs->roll != rhs->roll) {
    return false;
  }
  // pitch
  if (lhs->pitch != rhs->pitch) {
    return false;
  }
  // yaw
  if (lhs->yaw != rhs->yaw) {
    return false;
  }
  // accelx
  if (lhs->accelx != rhs->accelx) {
    return false;
  }
  // accely
  if (lhs->accely != rhs->accely) {
    return false;
  }
  // accelz
  if (lhs->accelz != rhs->accelz) {
    return false;
  }
  // gyrox
  if (lhs->gyrox != rhs->gyrox) {
    return false;
  }
  // gyroy
  if (lhs->gyroy != rhs->gyroy) {
    return false;
  }
  // gyroz
  if (lhs->gyroz != rhs->gyroz) {
    return false;
  }
  return true;
}

bool
utils__msg__IMU__copy(
  const utils__msg__IMU * input,
  utils__msg__IMU * output)
{
  if (!input || !output) {
    return false;
  }
  // roll
  output->roll = input->roll;
  // pitch
  output->pitch = input->pitch;
  // yaw
  output->yaw = input->yaw;
  // accelx
  output->accelx = input->accelx;
  // accely
  output->accely = input->accely;
  // accelz
  output->accelz = input->accelz;
  // gyrox
  output->gyrox = input->gyrox;
  // gyroy
  output->gyroy = input->gyroy;
  // gyroz
  output->gyroz = input->gyroz;
  return true;
}

utils__msg__IMU *
utils__msg__IMU__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__msg__IMU * msg = (utils__msg__IMU *)allocator.allocate(sizeof(utils__msg__IMU), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(utils__msg__IMU));
  bool success = utils__msg__IMU__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
utils__msg__IMU__destroy(utils__msg__IMU * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    utils__msg__IMU__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
utils__msg__IMU__Sequence__init(utils__msg__IMU__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__msg__IMU * data = NULL;

  if (size) {
    data = (utils__msg__IMU *)allocator.zero_allocate(size, sizeof(utils__msg__IMU), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = utils__msg__IMU__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        utils__msg__IMU__fini(&data[i - 1]);
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
utils__msg__IMU__Sequence__fini(utils__msg__IMU__Sequence * array)
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
      utils__msg__IMU__fini(&array->data[i]);
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

utils__msg__IMU__Sequence *
utils__msg__IMU__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  utils__msg__IMU__Sequence * array = (utils__msg__IMU__Sequence *)allocator.allocate(sizeof(utils__msg__IMU__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = utils__msg__IMU__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
utils__msg__IMU__Sequence__destroy(utils__msg__IMU__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    utils__msg__IMU__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
utils__msg__IMU__Sequence__are_equal(const utils__msg__IMU__Sequence * lhs, const utils__msg__IMU__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!utils__msg__IMU__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
utils__msg__IMU__Sequence__copy(
  const utils__msg__IMU__Sequence * input,
  utils__msg__IMU__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(utils__msg__IMU);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    utils__msg__IMU * data =
      (utils__msg__IMU *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!utils__msg__IMU__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          utils__msg__IMU__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!utils__msg__IMU__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
