set(IDL_FILES ""
              MyService.idl
              BasicDataType.idl
)

if(UNIX)
  add_custom_target(idlcompile ALL sh ${CMAKE_BINARY_DIR}/idlcompile.sh
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
  )
else()
  add_custom_target(idlcompile ALL ${CMAKE_BINARY_DIR}/idlcompile.bat
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
  )
endif()


add_custom_target( ${PROJECT_NAME} ALL
  COMMAND ${CMAKE_COMMAND} -E make_directory ${PROJECT_BINARY_DIR}/idl
  COMMAND ${CMAKE_COMMAND} -E copy_directory
      ${PROJECT_SOURCE_DIR}/idl ${PROJECT_BINARY_DIR}/idl
)

install(DIRECTORY idl DESTINATION "${INSTALL_PREFIX}"
        COMPONENT component)