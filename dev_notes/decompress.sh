#!/bin/sh

rosrun image_transport republish compressed in:=/stereo/frame_left/image_raw out:=/stereo/frame_left/image_raw_decomp
rosrun image_transport republish compressed in:=/stereo/frame_right/image_raw out:=/stereo/frame_right/image_raw_decomp