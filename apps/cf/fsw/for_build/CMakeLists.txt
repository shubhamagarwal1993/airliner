 #############################################################################
 #
 #   Copyright (c) 2017 Windhover Labs, L.L.C. All rights reserved.
 #
 # Redistribution and use in source and binary forms, with or without
 # modification, are permitted provided that the following conditions
 # are met:
 #
 # 1. Redistributions of source code must retain the above copyright
 #    notice, this list of conditions and the following disclaimer.
 # 2. Redistributions in binary form must reproduce the above copyright
 #    notice, this list of conditions and the following disclaimer in
 #    the documentation and/or other materials provided with the
 #    distribution.
 # 3. Neither the name Windhover Labs nor the names of its contributors 
 #    may be used to endorse or promote products derived from this software
 #    without specific prior written permission.
 #
 # THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 # "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 # LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 # FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 # COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 # INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 # BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS
 # OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED
 # AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 # LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 # ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 # POSSIBILITY OF SUCH DAMAGE.
 #
 #############################################################################
 
add_airliner_app_def(cf
    FILE CF
    SOURCES
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_app.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_app.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_callbacks.c 
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_callbacks.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_cmds.c  
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_cmds.h   
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_defs.h   
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_events.h   
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_msg.h 
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_playback.c  
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_playback.h  
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_tbldefs.h  
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_utils.c   
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_utils.h    
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_verify.h     
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_version.h 
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/aaa.c  
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/aaa.h  
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/callbacks.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/callbacks.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/cfdp_lib.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/cfdp_private.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/default_filestore.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/default_indication.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/event.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/event.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/machine_list.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/machine_list.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/machine.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/message_class.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/message_class.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/mib.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/mib.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/misc.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/misc.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/nak_mem.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/nak_mem.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/nak.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/nak.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/pdu_as_string.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/pdu_as_string.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/pdu.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/pdu.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/r1.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/r1.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/r2.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/r2.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/s1.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/s1.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/s2.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/s2.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/structures.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/timer.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/timer.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/utils.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/utils.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/validate_user_config.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PUB/cfdp_config.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PUB/cfdp_data_structures.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PUB/cfdp_provides.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PUB/cfdp_requires.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PUB/cfdp_syntax.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PUB/cfdp.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_symbols.c
        
    INCLUDES
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PUB/
        
    USER_DOCS   ${CMAKE_CURRENT_SOURCE_DIR}/user_doxy.in   
    DESIGN_DOCS   ${CMAKE_CURRENT_SOURCE_DIR}/detail_doxy.in   
    
    MSG_OVERRIDES   ${CMAKE_CURRENT_SOURCE_DIR}/cf_msg_overrides.json 

    COMMANDER_PLUGIN
        ${CMAKE_CURRENT_SOURCE_DIR}/../../cdr
    
    REFERENCE_CONFIG
        ${PROJECT_SOURCE_DIR}/apps/cf/fsw/mission_inc
        ${PROJECT_SOURCE_DIR}/apps/cf/fsw/platform_inc
)


#add_airliner_app_unit_test(cf-ut
#    UTASSERT 
#    SOURCES
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_app.c
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_app.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_callbacks.c 
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_callbacks.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_cmds.c  
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_cmds.h   
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_defs.h   
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_events.h   
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_msg.h 
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_playback.c  
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_playback.h  
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_tbldefs.h  
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_utils.c   
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_utils.h    
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_verify.h     
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/cf_version.h 
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/aaa.c  
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/aaa.h  
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/callbacks.c
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/callbacks.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/cfdp_lib.c
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/cfdp_private.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/default_filestore.c
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/default_indication.c
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/event.c
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/event.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/machine_list.c
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/machine_list.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/machine.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/message_class.c
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/message_class.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/mib.c
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/mib.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/misc.c
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/misc.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/nak_mem.c
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/nak_mem.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/nak.c
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/nak.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/pdu_as_string.c
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/pdu_as_string.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/pdu.c
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/pdu.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/r1.c
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/r1.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/r2.c
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/r2.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/s1.c
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/s1.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/s2.c
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/s2.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/structures.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/timer.c
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/timer.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/utils.c
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/utils.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/validate_user_config.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PUB/cfdp_config.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PUB/cfdp_data_structures.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PUB/cfdp_provides.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PUB/cfdp_requires.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PUB/cfdp_syntax.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PUB/cfdp.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/cf_cfgtable.c
#        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/cf_msgids.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/cf_platform_cfg.h
#        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/cf_testcase.c
#        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/cf_testrunner.c
#        
#    INCLUDES
#        ${CMAKE_CURRENT_SOURCE_DIR}/../mission_inc/
#        ${CMAKE_CURRENT_SOURCE_DIR}/../platform_inc/
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PRI/
#        ${CMAKE_CURRENT_SOURCE_DIR}/../src/PUB/
#        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/
#        
#    VALGRIND_SUPPRESSION_FILE
#        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/valgrind.supp
#)


