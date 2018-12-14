cmake_minimum_required(VERSION 3.8)
project(BooleanSimplifier)

set(CMAKE_CXX_STANDARD 11)

FIND_PACKAGE( Boost 1.40 COMPONENTS program_options REQUIRED )
INCLUDE_DIRECTORIES( ${Boost_INCLUDE_DIR} )

ADD_EXECUTABLE( anyExecutable myMain.cpp )

TARGET_LINK_LIBRARIES( anyExecutable LINK_PUBLIC ${Boost_LIBRARIES} )

set(SOURCE_FILES main.cpp)
add_executable(C__ ${SOURCE_FILES})