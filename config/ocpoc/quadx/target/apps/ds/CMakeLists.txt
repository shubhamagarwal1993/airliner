set(APP_NAME ds)

add_airliner_app_table(
    ${APP_NAME}
    NAME ds_file_tbl
    SOURCES ${CMAKE_CURRENT_SOURCE_DIR}/tables/ds_file_tbl.c
    INCLUDES ${CMAKE_CURRENT_SOURCE_DIR}/src/
)

add_airliner_app_table(
    ${APP_NAME}
    NAME ds_filter_tbl
    SOURCES ${CMAKE_CURRENT_SOURCE_DIR}/tables/ds_filter_tbl.c
    INCLUDES ${CMAKE_CURRENT_SOURCE_DIR}/src/
)

