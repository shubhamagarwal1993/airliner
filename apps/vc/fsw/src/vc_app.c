/*==============================================================================
Copyright (c) 2017, Windhover Labs
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of CmdIn nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY VCPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, VCEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

/************************************************************************
** Pragmas
*************************************************************************/

/************************************************************************
** Includes
*************************************************************************/
#include "vc_app.h"
#include "vc_cmds.h"
#include "vc_msgids.h"
#include "vc_perfids.h"
#include <string.h>

/************************************************************************
** Local Defines
*************************************************************************/

/************************************************************************
** Local Structure Declarations
*************************************************************************/

/************************************************************************
** External Global Variables
*************************************************************************/

/************************************************************************
** Global Variables
*************************************************************************/
VC_AppData_t VC_AppData;

/************************************************************************
** Local Variables
*************************************************************************/

/************************************************************************
** Local Function Definitions
*************************************************************************/

/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
/*                                                                 */
/* Initialize event tables                                         */
/*                                                                 */
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */

int32 VC_InitEvent()
{
    int32  iStatus=CFE_SUCCESS;
    int32  ind = 0;

    /* Initialize the event filter table.
     * Note: 0 is the CFE_EVS_NO_FILTER mask and event 0 is reserved (not used) */
    memset((void*)VC_AppData.EventTbl, 0x00, sizeof(VC_AppData.EventTbl));

    /* TODO: Choose the events you want to filter.  CFE_EVS_MAX_EVENT_FILTERS
     * limits the number of filters per app.  An explicit CFE_EVS_NO_FILTER 
     * (the default) has been provided as an example. */
    VC_AppData.EventTbl[  ind].EventID = VC_RESERVED_EID;
    VC_AppData.EventTbl[ind++].Mask    = CFE_EVS_NO_FILTER;

    VC_AppData.EventTbl[  ind].EventID = VC_INIT_INF_EID;
    VC_AppData.EventTbl[ind++].Mask    = CFE_EVS_NO_FILTER;

    VC_AppData.EventTbl[  ind].EventID = VC_NOOP_INF_EID;
    VC_AppData.EventTbl[ind++].Mask    = CFE_EVS_NO_FILTER;

    VC_AppData.EventTbl[  ind].EventID = VC_RESET_INF_EID;
    VC_AppData.EventTbl[ind++].Mask    = CFE_EVS_NO_FILTER;

    VC_AppData.EventTbl[  ind].EventID = VC_PROCCESS_INF_EID;
    VC_AppData.EventTbl[ind++].Mask    = CFE_EVS_NO_FILTER;

    VC_AppData.EventTbl[  ind].EventID = VC_MID_ERR_EID;
    VC_AppData.EventTbl[ind++].Mask    = CFE_EVS_NO_FILTER;

    VC_AppData.EventTbl[  ind].EventID = VC_CC1_ERR_EID;
    VC_AppData.EventTbl[ind++].Mask    = CFE_EVS_NO_FILTER;
    
    VC_AppData.EventTbl[  ind].EventID = VC_LEN_ERR_EID;
    VC_AppData.EventTbl[ind++].Mask    = CFE_EVS_NO_FILTER;
        
    VC_AppData.EventTbl[  ind].EventID = VC_PIPE_ERR_EID;
    VC_AppData.EventTbl[ind++].Mask    = CFE_EVS_NO_FILTER;
        
    VC_AppData.EventTbl[  ind].EventID = VC_SOCKET_ERR_EID;
    VC_AppData.EventTbl[ind++].Mask    = CFE_EVS_NO_FILTER;
        
    VC_AppData.EventTbl[  ind].EventID = VC_DEVICE_ERR_EID;
    VC_AppData.EventTbl[ind++].Mask    = CFE_EVS_NO_FILTER;
    
    VC_AppData.EventTbl[  ind].EventID = VC_INIT_ERR_EID;
    VC_AppData.EventTbl[ind++].Mask    = CFE_EVS_NO_FILTER;

    VC_AppData.EventTbl[  ind].EventID = VC_UNINIT_ERR_EID;
    VC_AppData.EventTbl[ind++].Mask    = CFE_EVS_NO_FILTER;

    VC_AppData.EventTbl[  ind].EventID = VC_CHA_INF_EID;
    VC_AppData.EventTbl[ind++].Mask    = CFE_EVS_NO_FILTER;

    VC_AppData.EventTbl[  ind].EventID = VC_DEV_INF_EID;
    VC_AppData.EventTbl[ind++].Mask    = CFE_EVS_NO_FILTER;
    
    VC_AppData.EventTbl[  ind].EventID = VC_ADDR_ERR_EID;
    VC_AppData.EventTbl[ind++].Mask    = CFE_EVS_NO_FILTER;
    
    VC_AppData.EventTbl[  ind].EventID = VC_ADDR_NUL_ERR_EID;
    VC_AppData.EventTbl[ind++].Mask    = CFE_EVS_NO_FILTER;

    /* Register the table with CFE */
    iStatus = CFE_EVS_Register(VC_AppData.EventTbl,
                               VC_EVT_COUNT, CFE_EVS_BINARY_FILTER);
    if (iStatus != CFE_SUCCESS)
    {
        (void) CFE_ES_WriteToSysLog("VC - Failed to register with EVS (0x%08X)\n", (unsigned int)iStatus);
    }

    return (iStatus);
}


void VC_AppMain(void)
{
    int32 Status = CFE_SUCCESS;
   
    /* Register the application with Executive Services */
    CFE_ES_RegisterApp();

    /* Create the first Performance Log entry */
    CFE_ES_PerfLogEntry(VC_APPMAIN_PERF_ID); 
   
    /* Perform application specific initialization */
    Status = VC_AppInit();
   
    if (Status != CFE_SUCCESS)
    {
        VC_AppData.RunStatus = CFE_ES_APP_ERROR;
    }
   
   /* Application main loop */
    while(CFE_ES_RunLoop(&VC_AppData.RunStatus) == TRUE)
    {
        /* Performance Log exit stamp */
        CFE_ES_PerfLogExit(VC_APPMAIN_PERF_ID);
        
        /* Wait for the next Software Bus message */
        Status = CFE_SB_RcvMsg(&VC_AppData.MsgPtr, VC_AppData.CmdPipe, VC_SB_TIMEOUT);

        /* Performance Log Entry Stamp */
        CFE_ES_PerfLogEntry(VC_APPMAIN_PERF_ID);

        if (Status == CFE_SUCCESS)
        {
            /*
             * Process Software Bus message. If there are fatal errors
             * in command processing the command can alter the global
             * RunStatus variable to exit the main event loop.
             */
            VC_AppPipe(VC_AppData.MsgPtr);
        }
        else
        {
           /* 
            * This is an example of exiting on an error.
            * Note that a SB read error is not always going to
            * result in an app quitting.
            */
            CFE_EVS_SendEvent(VC_PIPE_ERR_EID, CFE_EVS_ERROR, \
                              "SB Pipe Read Error, VC App will exit. RC = 0x%08X", (unsigned int)Status);

            VC_AppData.RunStatus = CFE_ES_APP_ERROR;
        }

   } /* end CFS_ES_RunLoop while */
   
   /* Performance Log exit stamp */
   CFE_ES_PerfLogExit(VC_APPMAIN_PERF_ID);
   
   /* Exit the application */
   CFE_ES_ExitApp(VC_AppData.RunStatus);
} /* end VC_AppMain */


void VC_CleanupCallback()
{
    if(VC_Transmit_Uninit() != TRUE)
    {
        CFE_EVS_SendEvent(VC_UNINIT_ERR_EID, CFE_EVS_ERROR,"VC_Transmit_Uninit failed");
    }
    
    if(VC_Devices_Stop() != TRUE)
    {
        CFE_EVS_SendEvent(VC_UNINIT_ERR_EID, CFE_EVS_ERROR,"VC_Devices_Stop failed");
    }
    
    if(VC_Devices_Uninit() != TRUE)
    {
        CFE_EVS_SendEvent(VC_UNINIT_ERR_EID, CFE_EVS_ERROR,"VC_Devices_Uninit failed");
    }
}


int32 VC_AppInit(void)
{
    int32  Status = CFE_SUCCESS;
    int8   hasEvents = 0;
    
    Status = VC_InitEvent();
    
    Status = VC_InitEvent();
    if (Status != CFE_SUCCESS)
    {
        (void) CFE_ES_WriteToSysLog("VC - Failed to init events (0x%08X)\n", (unsigned int)Status);
        goto VC_InitApp_Exit_Tag;
    }
    else
    {
        hasEvents = 1;
    }

    /* Setup the RunStatus variable */
    VC_AppData.RunStatus = CFE_ES_APP_RUN;
    
    /* Setup app state enum */
    VC_AppData.AppState = VC_UNINITIALIZED;

    /* Initialize app command execution counters */
    VC_AppData.CmdCounter = 0;
    VC_AppData.ErrCounter = 0;

    /* Initialize app configuration data */
    strcpy(VC_AppData.PipeName, VC_SB_PIPE_1_NAME);

    VC_AppData.PipeDepth = VC_PIPE_DEPTH;

    /* Initialize housekeeping packet (clear user data area) */
    CFE_SB_InitMsg(&VC_AppData.HkPacket, VC_HK_TLM_MID, sizeof(VC_HkPacket_t), TRUE);

    /* Create Software Bus message pipe */
    Status = CFE_SB_CreatePipe(&VC_AppData.CmdPipe, VC_AppData.PipeDepth, VC_AppData.PipeName);
    
    if (Status != CFE_SUCCESS)
    {
        CFE_EVS_SendEvent(VC_PIPE_ERR_EID, CFE_EVS_ERROR, \
                              "SB Pipe Creation Error, VC App will exit. RC = 0x%08X", (unsigned int)Status);
    return (Status);
    }
    
    /* Subscribe to Housekeeping request commands */
    Status = CFE_SB_Subscribe(VC_SEND_HK_MID, VC_AppData.CmdPipe);

    if (Status != CFE_SUCCESS)
    {
        CFE_EVS_SendEvent(VC_PIPE_ERR_EID, CFE_EVS_ERROR, \
                            "Error Subscribing to HK Request, VC App will exit. RC = 0x%08X", (unsigned int)Status);
        return (Status);
    }
    
    /* Subscribe to VC ground command packets */
    Status = CFE_SB_Subscribe(VC_CMD_MID, VC_AppData.CmdPipe);
    if (Status != CFE_SUCCESS)
    {
       CFE_EVS_SendEvent(VC_PIPE_ERR_EID, CFE_EVS_ERROR, \
                            "Error Subscribing to VC Command, VC App will exit. RC = 0x%08X", (unsigned int)Status);
       return (Status);
    }
    
    /* Initialize data transmission resources */
    if (VC_Transmit_Init() != TRUE) 
    {
        /* Data transmit sink failed to initialize for now error out */   
        CFE_EVS_SendEvent(VC_INIT_ERR_EID, CFE_EVS_ERROR,"VC_Transmit_Init failed");
        Status = -1;
        return (Status);
    }
    
    /* Initialize devices */
    if (VC_Devices_Init() != TRUE) 
    {
        /* Device failed to initialize for now error out */
        CFE_EVS_SendEvent(VC_INIT_ERR_EID, CFE_EVS_ERROR,"VC_Devices_Init failed");
        Status = -1;
        return (Status);
    }
    else
    {
        /* Initialization was successful set state */
        VC_AppData.AppState = VC_INITIALIZED;
    }
    
    /* Start streaming */
    if (FALSE == VC_Devices_Start()) 
    {
        /* Start streaming failed, raise event but for now don't error out */
        CFE_EVS_SendEvent(VC_INIT_ERR_EID, CFE_EVS_ERROR,"VC_Devices_Start failed");
    }
    else
    {
        /* Streaming is successful set state */
        VC_AppData.AppState = VC_STREAMING;
    }
    
    /* Register the cleanup callback */
    Status = OS_TaskInstallDeleteHandler(&VC_CleanupCallback);
    if (Status != CFE_SUCCESS)
    {
        CFE_EVS_SendEvent(VC_INIT_ERR_EID, CFE_EVS_ERROR,
                                 "Failed to init register cleanup callback (0x%08X)",
                                 (unsigned int)Status);
        return (Status);
    }
    
VC_InitApp_Exit_Tag:
    if (Status == CFE_SUCCESS)
    {
        /* Application startup event message */
        (void) CFE_EVS_SendEvent(VC_INIT_INF_EID, CFE_EVS_INFORMATION,
                                 "Initialized.  Version %d.%d.%d.%d",
                                 VC_MAJOR_VERSION,
                                 VC_MINOR_VERSION,
                                 VC_REVISION,
                                 VC_MISSION_REV);
    }
    else
    {
        if (hasEvents == 1)
        {
            (void) CFE_EVS_SendEvent(VC_INIT_ERR_EID, CFE_EVS_ERROR, "Application failed to initialize");
        }
        else
        {
            (void) CFE_ES_WriteToSysLog("VC - Application failed to initialize\n");
        }
    }
    return(CFE_SUCCESS);
} /* End of VC_AppInit() */


void VC_AppPipe(CFE_SB_MsgPtr_t msg)
{
    CFE_SB_MsgId_t MessageID = 0;
    uint16 CommandCode = 0;

    MessageID = CFE_SB_GetMsgId(msg);
    switch (MessageID)
    {
        /* Housekeeping telemetry request */
        case VC_SEND_HK_MID:
            VC_HousekeepingCmd(msg);
            break;

        /* VC ground commands */
        case VC_CMD_MID:

            CommandCode = CFE_SB_GetCmdCode(msg);
            switch (CommandCode)
            {
                case VC_NOOP_CC:
                    VC_NoopCmd(msg);
                    break;

                case VC_RESET_CC:
                    VC_ResetCmd(msg);
                    break; 

                case VC_STARTSTREAMING_CC: 
                    VC_StartStreamingCmd(msg); 
                    break;
                case VC_STOPSTREAMING_CC:
                    VC_StopStreamingCmd(msg);
                    break;

                default:
                    CFE_EVS_SendEvent(VC_CC1_ERR_EID, CFE_EVS_ERROR, \
                    "Invalid ground command code: ID = 0x%X, CC = %d", \
                                    MessageID, CommandCode);
                    break;
            }
            break;

        default:
            VC_AppData.ErrCounter++;
            CFE_EVS_SendEvent(VC_MID_ERR_EID, CFE_EVS_ERROR,
                            "Invalid command pipe message ID: 0x%X",
                            MessageID);
            break;
    }

    return;

} /* End of VC_AppPipe() */








