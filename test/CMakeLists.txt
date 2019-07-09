
if(UNIX)
  add_custom_target(idlcompile sh ${CMAKE_BINARY_DIR}/idlcompile.sh
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR} ALL
  )
else()
  add_custom_target(idlcompile ${CMAKE_BINARY_DIR}/idlcompile.bat
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR} ALL
  )
endif()

add_dependencies(idlcompile ${PROJECT_NAME})


add_test(NAME ${PROJECT_NAME}_test COMMAND ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/${PROJECT_NAME}Test.py -o "manager.components.precreate:${PROJECT_NAME}" -o "manager.components.preconnect:${PROJECT_NAME}0.in?port=${PROJECT_NAME}Test0.in,${PROJECT_NAME}0.out?port=${PROJECT_NAME}Test0.out,${PROJECT_NAME}0.MyServide?port=${PROJECT_NAME}Test0.MyServide" -o "manager.components.preactivation:${PROJECT_NAME}0,${PROJECT_NAME}Test0" WORKING_DIRECTORY ${CMAKE_BINARY_DIR})
string(REPLACE ";" "\\;" PYTHONPATH "$ENV{PYTHONPATH}")
set_tests_properties(${PROJECT_NAME}_test PROPERTIES ENVIRONMENT "PYTHONPATH=${CMAKE_SOURCE_DIR}\;${PYTHONPATH}")