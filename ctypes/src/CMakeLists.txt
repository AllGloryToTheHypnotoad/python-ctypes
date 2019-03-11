cmake_minimum_required (VERSION 3.7)

project(HELLO)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(CMAKE_BUILD_TYPE Release)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/lib)

if( WIN32 )
    MESSAGE("Windows not supported ... ha, ha, ha, your OS sucks!")
else()
    include_directories(/usr/local/include ./)
    add_library(hello SHARED hello.cpp)
    # add_library(hello STATIC hello.cpp)
endif()
