#!/bin/sh

rosrun image_transport republish compressed in:=/stereo/frame_left/image_raw out:=/stereo/frame_left/image_raw_decomp