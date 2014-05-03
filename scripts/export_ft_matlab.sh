#!/bin/bash

# export dumbo F/T sensor readings from rosbag file to matlab

# parameter 1: bag file
# parameter 2: 'left' or 'right' arm

# usage: rosrun dumbo_scripts export_ft_matlab.sh <bagfile>.bag left

rostopic echo -b $1 -p /$2_arm_ft_sensor/ft_compensated/wrench > ft.txt