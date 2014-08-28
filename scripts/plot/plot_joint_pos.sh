#!/bin/bash

# usage: plot_joint_pos.sh left
#        plot_joint_pos.sh right

# OR:    rosrun dumbo_scripts plot_joint_pos.sh left

# parameter specifies left or right arm

rqt_plot /$1_arm_controller/state/actual/positions[0] /$1_arm_controller/state/actual/positions[1] /$1_arm_controller/state/actual/positions[2] /$1_arm_controller/state/actual/positions[3] /$1_arm_controller/state/actual/positions[4] /$1_arm_controller/state/actual/positions[5] /$1_arm_controller/state/actual/positions[6]