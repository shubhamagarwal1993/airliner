/****************************************************************************
*
*   Copyright (c) 2017 Windhover Labs, L.L.C. All rights reserved.
*
* Redistribution and use in source and binary forms, with or without
* modification, are permitted provided that the following conditions
* are met:
*
* 1. Redistributions of source code must retain the above copyright
*    notice, this list of conditions and the following disclaimer.
* 2. Redistributions in binary form must reproduce the above copyright
*    notice, this list of conditions and the following disclaimer in
*    the documentation and/or other materials provided with the
*    distribution.
* 3. Neither the name Windhover Labs nor the names of its 
*    contributors may be used to endorse or promote products derived 
*    from this software without specific prior written permission.
*
* THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
* "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
* LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
* FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
* COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
* INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
* BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS
* OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED
* AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
* LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
* ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
* POSSIBILITY OF SUCH DAMAGE.
*
*****************************************************************************/

#include "uttest.h"

#include "Matrix10F2_test.hpp"
#include "Matrix10F2_test_utils.hpp"

int main(void)
{   
	UtTest_Add(Test_Matrix10F2_Constructor, Matrix10F2_Test_Setup, Matrix10F2_Test_TearDown,
	         "Test_Matrix10F2_Constructor");
	UtTest_Add(Test_Matrix10F2_OutOfBounds, Matrix10F2_Test_Setup, Matrix10F2_Test_TearDown,
	         "Test_Matrix10F2_OutOfBounds");
	UtTest_Add(Test_Matrix10F2_Identity, Matrix10F2_Test_Setup, Matrix10F2_Test_TearDown,
	         "Test_Matrix10F2_Identity");
	UtTest_Add(Test_Matrix10F2_Zero, Matrix10F2_Test_Setup, Matrix10F2_Test_TearDown,
	         "Test_Matrix10F2_Zero");
	UtTest_Add(Test_Matrix10F2_Mult_2F, Matrix10F2_Test_Setup, Matrix10F2_Test_TearDown,
	         "Test_Matrix10F2_Mult_2F");
	UtTest_Add(Test_Matrix10F2_Mult_2F_Random, Matrix10F2_Test_Setup, Matrix10F2_Test_TearDown,
	         "Test_Matrix10F2_Mult_2F_Random");
	UtTest_Add(Test_Matrix10F2_Mult_2F2, Matrix10F2_Test_Setup, Matrix10F2_Test_TearDown,
	         "Test_Matrix10F2_Mult_2F2");
	UtTest_Add(Test_Matrix10F2_Mult_2F2_Random, Matrix10F2_Test_Setup, Matrix10F2_Test_TearDown,
	         "Test_Matrix10F2_Mult_2F2_Random");
	UtTest_Add(Test_Matrix10F2_Mult_2F10, Matrix10F2_Test_Setup, Matrix10F2_Test_TearDown,
	         "Test_Matrix10F2_Mult_2F10");
	UtTest_Add(Test_Matrix10F2_Mult_2F10_Random, Matrix10F2_Test_Setup, Matrix10F2_Test_TearDown,
	         "Test_Matrix10F2_Mult_2F10_Random");
	UtTest_Add(Test_Matrix10F2_Mult_Scaler, Matrix10F2_Test_Setup, Matrix10F2_Test_TearDown,
	         "Test_Matrix10F2_Mult_Scaler");
	UtTest_Add(Test_Matrix10F2_Transpose, Matrix10F2_Test_Setup, Matrix10F2_Test_TearDown,
	         "Test_Matrix10F2_Transpose");
	UtTest_Add(Test_Matrix10F2_Addition, Matrix10F2_Test_Setup, Matrix10F2_Test_TearDown,
	         "Test_Matrix10F2_Addition");

    return(UtTest_Run());

}

