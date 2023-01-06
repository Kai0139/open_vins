#!/bin/sh

PROFILE_NAME=open_vins_t1

source ~/catkin_ws_cb/devel/setup.bash
env CPUPROFILE=${HOME}/perftools/profiles/${PROFILE_NAME}.prof LD_PRELOAD=/usr/local/lib/libprofiler.so.0 roslaunch ov_msckf subscribe.launch
