/*
** $Id: sch_tbldefs.h 1.3 2017/06/21 15:29:42EDT mdeschu Exp  $
**
**  Copyright (c) 2007-2014 United States Government as represented by the 
**  Administrator of the National Aeronautics and Space Administration. 
**  All Other Rights Reserved.  
**
**  This software was created at NASA's Goddard Space Flight Center.
**  This software is governed by the NASA Open Source Agreement and may be 
**  used, distributed and modified only pursuant to the terms of that 
**  agreement.
**
** Subsystem: Scheduler (SCH) table definitions
**
** Author:
**
** Notes:
**
*/

/*************************************************************************
**
** Ensure that "this" header is included only once
**
**************************************************************************/

#ifndef _sch_tbldefs_
#define _sch_tbldefs_

/*************************************************************************
**
** SCH table structure definitions
**
**************************************************************************/

/*
** Schedule definition table entry
*/
typedef struct
{
    uint8    EnableState;          /**< \brief State may be #SCH_UNUSED, #SCH_ENABLED, #SCH_DISABLED */
    uint8    Type;                 /**< \brief Activity Type may be #SCH_ACTIVITY_NONE or #SCH_ACTIVITY_SEND_MSG */
    uint16   Frequency;            /**< \brief Number of seconds between Activity execution */
    uint16   Remainder;            /**< \brief Seconds offset to perform Activity */
    uint16   MessageIndex;         /**< \brief Byte index into Message Definition Table */

    uint32   GroupData;            /**< \brief Group and Multi-Group membership definitions */
    uint32   Deadline;             /**< \brief Number of frames the activity is required to complete. */

} SCH_ScheduleEntry_t;

/*
** Message definition table entry
*/
typedef struct
{
    uint16   MessageBuffer[SCH_MAX_MSG_WORDS]; /**< \brief Packed Messages */

} SCH_MessageEntry_t;


typedef enum
{
	SCH_DEADLINE_STATE_UNKNOWN 	= 0,
	SCH_DEADLINE_STATE_PENDED	= 1,
	SCH_DEADLINE_STATE_IDLE		= 2
} SCH_ActivityDeadlineState_t;

typedef struct
{
	CFE_SB_MsgId_t					MsgID;
	SCH_ActivityDeadlineState_t		State;
	uint32							OverrunCount;
} SCH_ActivityDeadlineStatus_t;


typedef struct
{
	SCH_ActivityDeadlineStatus_t Status[SCH_DEADLINES_PER_SLOT];
} SCH_SlotDeadlineStatus_t;

typedef struct
{
	SCH_SlotDeadlineStatus_t	Slot[SCH_TOTAL_SLOTS];
} SCH_DeadlineTable_t;

#endif /* _sch_tbldefs_ */
