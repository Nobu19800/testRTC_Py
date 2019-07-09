set(IDL_FILES ""
              MyService.idl
)

if(WIN32)
    set(SCRIPT_FILE ""
                    ${PROJECT_SOURCE_DIR}/idlcompile.bat ${PROJECT_SOURCE_DIR}/delete.bat)
else()
    set(SCRIPT_FILE ""
                    ${PROJECT_SOURCE_DIR}/idlcompile.sh)
endif()

foreach(target ${SCRIPT_FILE})
  add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy
        ${target} ${PROJECT_BINARY_DIR}
  )
endforeach()


if(UNIX)
  add_custom_target(idlcompile ALL sh ${CMAKE_BINARY_DIR}/idlcompile.sh
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
  )
else()
  add_custom_target(idlcompile ALL ${CMAKE_BINARY_DIR}/idlcompile.bat
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
  )
endif()

add_dependencies(idlcompile ${PROJECT_NAME})

install(PROGRAMS ${SCRIPT_FILE} DESTINATION "${INSTALL_PREFIX}"
        COMPONENT component)
install(FILES ${IDL_FILES} DESTINATION idl
        COMPONENT component)