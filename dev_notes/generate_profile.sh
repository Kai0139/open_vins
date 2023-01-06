#!/bin/sh

PATH_TO_EXECUTABLE=${HOME}/catkin_ws_cb/devel/lib/ov_msckf/run_subscribe_msckf
PROFILE_PATH=${HOME}/perftools/profiles/open_vins_t0.prof
OUTPUT_PATH=${HOME}/perftools/profiles/results/
OUTPUT_NAME=open_vins_t0_0

pprof --pdf ${PATH_TO_EXECUTABLE} ${PROFILE_PATH} > ${OUTPUT_PATH}${OUTPUT_NAME}.pdf