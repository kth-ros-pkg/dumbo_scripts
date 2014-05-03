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


install(DIRECTORY scripts 
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)