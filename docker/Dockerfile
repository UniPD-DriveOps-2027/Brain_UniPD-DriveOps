# UniPD DriveOps Brain container.
# The OAK-D camera is intentionally part of this image and is launched by
# brain_bringup/hardware.launch.py. Isaac ROS Visual SLAM consumes the camera
# topics from another container; it does not open the camera device.

FROM ros:jazzy-ros-base

ENV DEBIAN_FRONTEND=noninteractive \
    ROS_DISTRO=jazzy \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
    libgl1 \
    libglib2.0-0 \
    python3-dev \
    python3-pip \
    python3-venv \
    python3-numpy \
    python3-opencv \
    ros-jazzy-cv-bridge \
    ros-jazzy-image-transport \
    && rm -rf /var/lib/apt/lists/*

# Keep non-ROS Python dependencies isolated from the ROS Python installation.
# This also avoids PEP 668 errors on Ubuntu 24.04/Jazzy hosts.
RUN python3 -m venv --system-site-packages /opt/brain_venv

WORKDIR /opt/brain_ws
COPY requirements.txt /tmp/brain-requirements.txt
RUN /opt/brain_venv/bin/pip install --no-cache-dir --upgrade pip setuptools wheel \
    && /opt/brain_venv/bin/pip install --no-cache-dir -r /tmp/brain-requirements.txt

COPY src ./src

RUN source /opt/ros/jazzy/setup.bash \
    && rosdep update \
    && rosdep install --from-paths src --ignore-src --rosdistro jazzy -r -y \
    && colcon build --merge-install --cmake-args -DBUILD_TESTING=OFF

COPY docker/entrypoint.sh /usr/local/bin/brain-entrypoint
RUN chmod +x /usr/local/bin/brain-entrypoint

ENTRYPOINT ["/usr/local/bin/brain-entrypoint"]
CMD ["ros2", "launch", "brain_bringup", "hardware.launch.py"]
