#!/bin/bash

# plots gravity-compensated torque readings from F/T sensor

# usage: plot_torque.sh left
#        plot_torque.sh right

# OR:    rosrun dumbo_scripts plot_torque.sh left

# parameter specifies left or right arm

rqt_plot /$1_arm_ft_sensor/ft_gravity_compensated/wrench/torque/x /$1_arm_ft_sensor/ft_gravity_compensated/wrench/torque/y /$1_arm_ft_sensor/ft_gravity_compensated/wrench/torque/z