/* Automatically generated nanopb header */
/* Generated by nanopb-0.3.6 at Wed Oct 26 00:46:17 2016. */

#ifndef PB_VEHICLE_CONTROL_MODE_PB_H_INCLUDED
#define PB_VEHICLE_CONTROL_MODE_PB_H_INCLUDED
#include <pb.h>

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Struct definitions */
typedef struct _px4_vehicle_control_mode_pb {
    uint64_t timestamp;
    bool flag_armed;
    bool flag_external_manual_override_ok;
    bool flag_system_hil_enabled;
    bool flag_control_manual_enabled;
    bool flag_control_auto_enabled;
    bool flag_control_offboard_enabled;
    bool flag_control_rates_enabled;
    bool flag_control_attitude_enabled;
    bool flag_control_rattitude_enabled;
    bool flag_control_force_enabled;
    bool flag_control_acceleration_enabled;
    bool flag_control_velocity_enabled;
    bool flag_control_position_enabled;
    bool flag_control_altitude_enabled;
    bool flag_control_climb_rate_enabled;
    bool flag_control_termination_enabled;
/* @@protoc_insertion_point(struct:px4_vehicle_control_mode_pb) */
} px4_vehicle_control_mode_pb;

/* Default values for struct fields */

/* Initializer values for message structs */
#define px4_vehicle_control_mode_pb_init_default {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
#define px4_vehicle_control_mode_pb_init_zero    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

/* Field tags (for use in manual encoding/decoding) */
#define px4_vehicle_control_mode_pb_timestamp_tag 1
#define px4_vehicle_control_mode_pb_flag_armed_tag 2
#define px4_vehicle_control_mode_pb_flag_external_manual_override_ok_tag 3
#define px4_vehicle_control_mode_pb_flag_system_hil_enabled_tag 4
#define px4_vehicle_control_mode_pb_flag_control_manual_enabled_tag 5
#define px4_vehicle_control_mode_pb_flag_control_auto_enabled_tag 6
#define px4_vehicle_control_mode_pb_flag_control_offboard_enabled_tag 7
#define px4_vehicle_control_mode_pb_flag_control_rates_enabled_tag 8
#define px4_vehicle_control_mode_pb_flag_control_attitude_enabled_tag 9
#define px4_vehicle_control_mode_pb_flag_control_rattitude_enabled_tag 10
#define px4_vehicle_control_mode_pb_flag_control_force_enabled_tag 11
#define px4_vehicle_control_mode_pb_flag_control_acceleration_enabled_tag 12
#define px4_vehicle_control_mode_pb_flag_control_velocity_enabled_tag 13
#define px4_vehicle_control_mode_pb_flag_control_position_enabled_tag 14
#define px4_vehicle_control_mode_pb_flag_control_altitude_enabled_tag 15
#define px4_vehicle_control_mode_pb_flag_control_climb_rate_enabled_tag 16
#define px4_vehicle_control_mode_pb_flag_control_termination_enabled_tag 17

/* Struct field encoding specification for nanopb */
extern const pb_field_t px4_vehicle_control_mode_pb_fields[18];

/* Maximum encoded size of messages (where known) */
#define px4_vehicle_control_mode_pb_size         45

/* Message IDs (where set with "msgid" option) */
#ifdef PB_MSGID

#define VEHICLE_CONTROL_MODE_MESSAGES \


#endif

#ifdef __cplusplus
} /* extern "C" */
#endif
/* @@protoc_insertion_point(eof) */

#endif
