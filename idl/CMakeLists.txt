if(UNIX)
  add_custom_target(idlcompile ALL sh ${CMAKE_BINARY_DIR}/idlcompile.sh
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
  )
else()
  add_custom_target(idlcompile ALL ${CMAKE_BINARY_DIR}/idlcompile.bat
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
  )
endif()