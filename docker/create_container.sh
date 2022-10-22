#!/bin/sh
IMAGE_NAME=osrf/ros
IMAGE_TAG=noetic-desktop-full

echo hello

DOCKER_CATKINWS=/home/username/workspace/catkin_ws_ov
DOCKER_DATASETS=/home/username/datasets

docker create --volume ${HOME}/bags:${HOME}/bags \
    --privileged \
    --net host \
    --env="DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume /tmp/.X11-unix:/tmp/.X11-unix:rw \
    --name open_vins_container \
    --interactive \
    ${IMAGE_NAME}:${IMAGE_TAG}

# DOCKER_CATKINWS=/home/username/workspace/catkin_ws_ov
# DOCKER_DATASETS=/home/username/datasets

# docker run -it --net=host \
#     --env="DISPLAY" \
#     --env="QT_X11_NO_MITSHM=1" \
#     --volume /tmp/.X11-unix:/tmp/.X11-unix:rw \
#     --volume ${HOME}/bags:${HOME}/bags \
#     --mount type=bind,source=$DOCKER_CATKINWS,target=/catkin_ws \
#     --mount type=bind,source=$DOCKER_DATASETS,target=/datasets $1
