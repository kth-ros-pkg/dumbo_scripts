#!/bin/bash

# export dumbo joint positions from rosbag file to matlab

# parameter 1: bag file
# parameter 2: 'left' or 'right' arm

# usage: rosrun dumbo_scripts export_joint_pos_matlab.sh <bagfile>.bag left

rostopic echo -b $1 -p /$2_arm_controller/state/actual/positions > joint_pos.txt