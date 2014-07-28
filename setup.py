#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    scripts=['scripts/export_joint_pos_matlab', 'scripts/export_joint_vel_command_matlab', 'scripts/export_ft_gravity_compensated_matlab']
)

setup(**d)
