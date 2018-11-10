cmake_minimum_required(VERSION 2.8.3)
project(ROSsocket1)

find_package(catkin REQUIRED COMPONENTS
  cv_bridge
  image_transport
  roscpp
  rospy
  std_msgs
  sensor_msgs
)

find_package(OpenCV)
find_package(PCL)
find_package(message_generation)

link_directories(
  ${catkin_LIBRARY_DIRS}
)

include_directories(
  ${catkin_INCLUDE_DIRS} ${OpenCV_INCLUDE_DIRS} ${PCL_INCLUDE_DIRS}
)

add_message_files(
  FILES
  rtklib.msg
)

generate_messages(
  DEPENDENCIES
  sensor_msgs
)

catkin_package(
  CATKIN_DEPENDS message_runtime
)


