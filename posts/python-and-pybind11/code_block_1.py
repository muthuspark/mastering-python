cmake_minimum_required(VERSION 3.10)
project(example)

add_subdirectory(pybind11) # Path to your pybind11 directory

add_library(example SHARED cpp_module.cpp)
target_link_libraries(example pybind11::pybind11)

install(TARGETS example DESTINATION ${CMAKE_INSTALL_PREFIX}/lib)
install(FILES example.py DESTINATION ${CMAKE_INSTALL_PREFIX}/lib)