/* Automatically generated nanopb header */
/* Generated by nanopb-0.3.6 at Wed Oct 26 00:46:10 2016. */

#ifndef PB_EKF2_REPLAY_PB_H_INCLUDED
#define PB_EKF2_REPLAY_PB_H_INCLUDED
#include <pb.h>

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Struct definitions */
typedef struct _px4_ekf2_replay_pb {
    uint64_t timestamp;
    uint64_t time_ref;
    uint64_t magnetometer_timestamp;
    uint64_t baro_timestamp;
    uint64_t rng_timestamp;
    uint64_t flow_timestamp;
    uint64_t asp_timestamp;
    uint64_t ev_timestamp;
    uint64_t time_usec;
    uint64_t time_usec_vel;
    float gyro_integral_dt;
    float accelerometer_integral_dt;
    pb_size_t gyro_rad_count;
    float gyro_rad[3];
    pb_size_t accelerometer_m_s2_count;
    float accelerometer_m_s2[3];
    pb_size_t magnetometer_ga_count;
    float magnetometer_ga[3];
    float baro_alt_meter;
    int32_t lat;
    int32_t lon;
    int32_t alt;
    float eph;
    float epv;
    float sacc;
    float vel_m_s;
    float vel_n_m_s;
    float vel_e_m_s;
    float vel_d_m_s;
    float range_to_ground;
    pb_size_t flow_pixel_integral_count;
    float flow_pixel_integral[2];
    pb_size_t flow_gyro_integral_count;
    float flow_gyro_integral[2];
    uint32_t flow_time_integral;
    float indicated_airspeed_m_s;
    float true_airspeed_m_s;
    pb_size_t pos_ev_count;
    float pos_ev[3];
    pb_size_t quat_ev_count;
    float quat_ev[4];
    float pos_err;
    float ang_err;
    uint32_t fix_type;
    uint32_t nsats;
    bool vel_ned_valid;
    uint32_t flow_quality;
/* @@protoc_insertion_point(struct:px4_ekf2_replay_pb) */
} px4_ekf2_replay_pb;

/* Default values for struct fields */

/* Initializer values for message structs */
#define px4_ekf2_replay_pb_init_default          {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {0, 0, 0}, 0, {0, 0, 0}, 0, {0, 0, 0}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {0, 0}, 0, {0, 0}, 0, 0, 0, 0, {0, 0, 0}, 0, {0, 0, 0, 0}, 0, 0, 0, 0, 0, 0}
#define px4_ekf2_replay_pb_init_zero             {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {0, 0, 0}, 0, {0, 0, 0}, 0, {0, 0, 0}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {0, 0}, 0, {0, 0}, 0, 0, 0, 0, {0, 0, 0}, 0, {0, 0, 0, 0}, 0, 0, 0, 0, 0, 0}

/* Field tags (for use in manual encoding/decoding) */
#define px4_ekf2_replay_pb_timestamp_tag         1
#define px4_ekf2_replay_pb_time_ref_tag          2
#define px4_ekf2_replay_pb_magnetometer_timestamp_tag 3
#define px4_ekf2_replay_pb_baro_timestamp_tag    4
#define px4_ekf2_replay_pb_rng_timestamp_tag     5
#define px4_ekf2_replay_pb_flow_timestamp_tag    6
#define px4_ekf2_replay_pb_asp_timestamp_tag     7
#define px4_ekf2_replay_pb_ev_timestamp_tag      8
#define px4_ekf2_replay_pb_time_usec_tag         9
#define px4_ekf2_replay_pb_time_usec_vel_tag     10
#define px4_ekf2_replay_pb_gyro_integral_dt_tag  11
#define px4_ekf2_replay_pb_accelerometer_integral_dt_tag 12
#define px4_ekf2_replay_pb_gyro_rad_tag          13
#define px4_ekf2_replay_pb_accelerometer_m_s2_tag 14
#define px4_ekf2_replay_pb_magnetometer_ga_tag   15
#define px4_ekf2_replay_pb_baro_alt_meter_tag    16
#define px4_ekf2_replay_pb_lat_tag               17
#define px4_ekf2_replay_pb_lon_tag               18
#define px4_ekf2_replay_pb_alt_tag               19
#define px4_ekf2_replay_pb_eph_tag               20
#define px4_ekf2_replay_pb_epv_tag               21
#define px4_ekf2_replay_pb_sacc_tag              22
#define px4_ekf2_replay_pb_vel_m_s_tag           23
#define px4_ekf2_replay_pb_vel_n_m_s_tag         24
#define px4_ekf2_replay_pb_vel_e_m_s_tag         25
#define px4_ekf2_replay_pb_vel_d_m_s_tag         26
#define px4_ekf2_replay_pb_range_to_ground_tag   27
#define px4_ekf2_replay_pb_flow_pixel_integral_tag 28
#define px4_ekf2_replay_pb_flow_gyro_integral_tag 29
#define px4_ekf2_replay_pb_flow_time_integral_tag 30
#define px4_ekf2_replay_pb_indicated_airspeed_m_s_tag 31
#define px4_ekf2_replay_pb_true_airspeed_m_s_tag 32
#define px4_ekf2_replay_pb_pos_ev_tag            33
#define px4_ekf2_replay_pb_quat_ev_tag           34
#define px4_ekf2_replay_pb_pos_err_tag           35
#define px4_ekf2_replay_pb_ang_err_tag           36
#define px4_ekf2_replay_pb_fix_type_tag          37
#define px4_ekf2_replay_pb_nsats_tag             38
#define px4_ekf2_replay_pb_vel_ned_valid_tag     39
#define px4_ekf2_replay_pb_flow_quality_tag      40

/* Struct field encoding specification for nanopb */
extern const pb_field_t px4_ekf2_replay_pb_fields[41];

/* Maximum encoded size of messages (where known) */
#define px4_ekf2_replay_pb_size                  376

/* Message IDs (where set with "msgid" option) */
#ifdef PB_MSGID

#define EKF2_REPLAY_MESSAGES \


#endif

#ifdef __cplusplus
} /* extern "C" */
#endif
/* @@protoc_insertion_point(eof) */

#endif
