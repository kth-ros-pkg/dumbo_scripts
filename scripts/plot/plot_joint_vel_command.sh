#!/bin/bash

# usage: plot_joint_vel_command.sh left
#        plot_joint_vel_command.sh right

# OR:    rosrun dumbo_scripts plot_joint_vel_command.sh left

# parameter specifies left or right arm

rqt_plot /$1_arm_controller/command_vel/velocities[0]/value /$1_arm_controller/command_vel/velocities[1]/value /$1_arm_controller/command_vel/velocities[2]/value /$1_arm_controller/command_vel/velocities[3]/value /$1_arm_controller/command_vel/velocities[4]/value /$1_arm_controller/command_vel/velocities[5]/value /$1_arm_controller/command_vel/velocities[6]/value