# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "ROSsocket1: 1 messages, 0 services")

set(MSG_I_FLAGS "-IROSsocket1:/home/doopy/Documents/sockets/socketROS/src/ROSsocket1/msg;-Isensor_msgs:/opt/ros/indigo/share/sensor_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/indigo/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(ROSsocket1_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/doopy/Documents/sockets/socketROS/src/ROSsocket1/msg/rtklib.msg" NAME_WE)
add_custom_target(_ROSsocket1_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ROSsocket1" "/home/doopy/Documents/sockets/socketROS/src/ROSsocket1/msg/rtklib.msg" "sensor_msgs/NavSatStatus:std_msgs/Header:sensor_msgs/NavSatFix"
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(ROSsocket1
  "/home/doopy/Documents/sockets/socketROS/src/ROSsocket1/msg/rtklib.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/sensor_msgs/cmake/../msg/NavSatStatus.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/sensor_msgs/cmake/../msg/NavSatFix.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ROSsocket1
)

### Generating Services

### Generating Module File
_generate_module_cpp(ROSsocket1
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ROSsocket1
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(ROSsocket1_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(ROSsocket1_generate_messages ROSsocket1_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/doopy/Documents/sockets/socketROS/src/ROSsocket1/msg/rtklib.msg" NAME_WE)
add_dependencies(ROSsocket1_generate_messages_cpp _ROSsocket1_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ROSsocket1_gencpp)
add_dependencies(ROSsocket1_gencpp ROSsocket1_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ROSsocket1_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(ROSsocket1
  "/home/doopy/Documents/sockets/socketROS/src/ROSsocket1/msg/rtklib.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/sensor_msgs/cmake/../msg/NavSatStatus.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/sensor_msgs/cmake/../msg/NavSatFix.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ROSsocket1
)

### Generating Services

### Generating Module File
_generate_module_lisp(ROSsocket1
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ROSsocket1
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(ROSsocket1_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(ROSsocket1_generate_messages ROSsocket1_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/doopy/Documents/sockets/socketROS/src/ROSsocket1/msg/rtklib.msg" NAME_WE)
add_dependencies(ROSsocket1_generate_messages_lisp _ROSsocket1_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ROSsocket1_genlisp)
add_dependencies(ROSsocket1_genlisp ROSsocket1_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ROSsocket1_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(ROSsocket1
  "/home/doopy/Documents/sockets/socketROS/src/ROSsocket1/msg/rtklib.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/sensor_msgs/cmake/../msg/NavSatStatus.msg;/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/sensor_msgs/cmake/../msg/NavSatFix.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ROSsocket1
)

### Generating Services

### Generating Module File
_generate_module_py(ROSsocket1
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ROSsocket1
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(ROSsocket1_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(ROSsocket1_generate_messages ROSsocket1_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/doopy/Documents/sockets/socketROS/src/ROSsocket1/msg/rtklib.msg" NAME_WE)
add_dependencies(ROSsocket1_generate_messages_py _ROSsocket1_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ROSsocket1_genpy)
add_dependencies(ROSsocket1_genpy ROSsocket1_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ROSsocket1_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ROSsocket1)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ROSsocket1
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(ROSsocket1_generate_messages_cpp sensor_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ROSsocket1)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ROSsocket1
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(ROSsocket1_generate_messages_lisp sensor_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ROSsocket1)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ROSsocket1\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ROSsocket1
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(ROSsocket1_generate_messages_py sensor_msgs_generate_messages_py)
