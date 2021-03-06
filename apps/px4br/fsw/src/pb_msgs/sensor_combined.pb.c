/* Automatically generated nanopb constant definitions */
/* Generated by nanopb-0.3.6 at Wed Oct 26 00:46:16 2016. */

#include "sensor_combined.pb.h"

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif



const pb_field_t px4_sensor_combined_pb_fields[12] = {
    PB_FIELD(  1, UINT64  , REQUIRED, STATIC  , FIRST, px4_sensor_combined_pb, timestamp, timestamp, 0),
    PB_FIELD(  2, FLOAT   , REPEATED, STATIC  , OTHER, px4_sensor_combined_pb, gyro_rad, timestamp, 0),
    PB_FIELD(  3, FLOAT   , REQUIRED, STATIC  , OTHER, px4_sensor_combined_pb, gyro_integral_dt, gyro_rad, 0),
    PB_FIELD(  4, INT32   , REQUIRED, STATIC  , OTHER, px4_sensor_combined_pb, accelerometer_timestamp_relative, gyro_integral_dt, 0),
    PB_FIELD(  5, FLOAT   , REPEATED, STATIC  , OTHER, px4_sensor_combined_pb, accelerometer_m_s2, accelerometer_timestamp_relative, 0),
    PB_FIELD(  6, FLOAT   , REQUIRED, STATIC  , OTHER, px4_sensor_combined_pb, accelerometer_integral_dt, accelerometer_m_s2, 0),
    PB_FIELD(  7, INT32   , REQUIRED, STATIC  , OTHER, px4_sensor_combined_pb, magnetometer_timestamp_relative, accelerometer_integral_dt, 0),
    PB_FIELD(  8, FLOAT   , REPEATED, STATIC  , OTHER, px4_sensor_combined_pb, magnetometer_ga, magnetometer_timestamp_relative, 0),
    PB_FIELD(  9, INT32   , REQUIRED, STATIC  , OTHER, px4_sensor_combined_pb, baro_timestamp_relative, magnetometer_ga, 0),
    PB_FIELD( 10, FLOAT   , REQUIRED, STATIC  , OTHER, px4_sensor_combined_pb, baro_alt_meter, baro_timestamp_relative, 0),
    PB_FIELD( 11, FLOAT   , REQUIRED, STATIC  , OTHER, px4_sensor_combined_pb, baro_temp_celcius, baro_alt_meter, 0),
    PB_LAST_FIELD
};


/* @@protoc_insertion_point(eof) */
