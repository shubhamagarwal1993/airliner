/* Automatically generated nanopb header */
/* Generated by nanopb-0.3.6 at Wed Oct 26 00:46:16 2016. */

#ifndef PB_SYSTEM_POWER_PB_H_INCLUDED
#define PB_SYSTEM_POWER_PB_H_INCLUDED
#include <pb.h>

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Struct definitions */
typedef struct _px4_system_power_pb {
    uint64_t timestamp;
    float voltage5V_v;
    uint32_t usb_connected;
    uint32_t brick_valid;
    uint32_t servo_valid;
    uint32_t periph_5V_OC;
    uint32_t hipower_5V_OC;
/* @@protoc_insertion_point(struct:px4_system_power_pb) */
} px4_system_power_pb;

/* Default values for struct fields */

/* Initializer values for message structs */
#define px4_system_power_pb_init_default         {0, 0, 0, 0, 0, 0, 0}
#define px4_system_power_pb_init_zero            {0, 0, 0, 0, 0, 0, 0}

/* Field tags (for use in manual encoding/decoding) */
#define px4_system_power_pb_timestamp_tag        1
#define px4_system_power_pb_voltage5V_v_tag      2
#define px4_system_power_pb_usb_connected_tag    3
#define px4_system_power_pb_brick_valid_tag      4
#define px4_system_power_pb_servo_valid_tag      5
#define px4_system_power_pb_periph_5V_OC_tag     6
#define px4_system_power_pb_hipower_5V_OC_tag    7

/* Struct field encoding specification for nanopb */
extern const pb_field_t px4_system_power_pb_fields[8];

/* Maximum encoded size of messages (where known) */
#define px4_system_power_pb_size                 46

/* Message IDs (where set with "msgid" option) */
#ifdef PB_MSGID

#define SYSTEM_POWER_MESSAGES \


#endif

#ifdef __cplusplus
} /* extern "C" */
#endif
/* @@protoc_insertion_point(eof) */

#endif
