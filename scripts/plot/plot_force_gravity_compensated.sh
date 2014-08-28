#!/bin/bash

# plots gravity-compensated force readings from F/T sensor

# usage: plot_force.sh left
#        plot_force.sh right

# OR:    rosrun dumbo_scripts plot_force.sh left

# parameter specifies left or right arm

rqt_plot /$1_arm_ft_sensor/ft_gravity_compensated/wrench/force/x /$1_arm_ft_sensor/ft_gravity_compensated/wrench/force/y /$1_arm_ft_sensor/ft_gravity_compensated/wrench/force/z