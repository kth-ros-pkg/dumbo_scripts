cmake_minimum_required(VERSION 2.8.3)
project(dumbo_scripts)

find_package(catkin REQUIRED COMPONENTS )

catkin_package(
  DEPENDS
  CATKIN_DEPENDS 
  INCLUDE_DIRS
  LIBRARIES 
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

link_directories(${catkin_LIBRARY_DIRS})


install(PROGRAMS scripts/plot_joint_pos.sh scripts/plot_joint_vel_command.sh scripts/plot_force_gravity_compensated.sh scripts/plot_torque_gravity_compensated.sh scripts/export_joint_pos_matlab scripts/export_joint_vel_command_matlab scripts/export_ft_gravity_compensated_matlab
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)