//Bootstrap
//SP = 256
	@256
	D=A
	@SP
	M=D
//Call
//push retAddrLabel
	@Sys.init$ret.0
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push LCL
	@LCL
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push ARG
	@ARG
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push THIS
	@THIS
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push THAT
	@THAT
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//ARG = SP-5-nArgs
	@SP
	D=M
	@5
	D=D-A
	@ARG
	M=D
//LCL = SP
	@SP
	D=M
	@LCL
	M=D
//goto Sys.init
	@Sys.init
	0;JMP
(Sys.init$ret.0)
//Function
(Sys.init)
//push constant 4
	@4
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//Call
//push retAddrLabel
	@Main.fibonacci$ret.1
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push LCL
	@LCL
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push ARG
	@ARG
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push THIS
	@THIS
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push THAT
	@THAT
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//ARG = SP-5-nArgs
	@SP
	D=M
	@6
	D=D-A
	@ARG
	M=D
//LCL = SP
	@SP
	D=M
	@LCL
	M=D
//goto Main.fibonacci
	@Main.fibonacci
	0;JMP
(Main.fibonacci$ret.1)
(WHILE)
//goto WHILE
	@WHILE
	0;JMP
//Function
(Main.fibonacci)
//push argument 0
	@ARG
	D=M
	@0
	D=D+A
	A=D
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push constant 2
	@2
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//lt
	@SP
	M=M-1
	A=M
	D=M
	@SP
	M=M-1
	A=M
	M=M-D
	D=M
	@TRUE.0
	D;JLT
(FALSE.0)
	@SP
	A=M
	M=0
	@END.0
	0;JMP
(TRUE.0)
	@SP
	A=M
	M=-1
(END.0)
	@SP
	M=M+1
//if-goto IF_TRUE
	@SP
	M=M-1
	A=M
	D=M
	@IF_TRUE
	D;JNE
//goto IF_FALSE
	@IF_FALSE
	0;JMP
(IF_TRUE)
//push argument 0
	@ARG
	D=M
	@0
	D=D+A
	A=D
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//Return
//endFrame = LCL
	@LCL
	D=M
	@endFrame.2
	M=D
//retAddr = *(endFrame – 5)
	@5
	D=A
	@endFrame.2
	D=M-D
	A=D
	D=M
	@retAddr.2
	M=D
//*ARG = pop()
	@SP
	M=M-1
	A=M
	D=M
	@ARG
	A=M
	M=D
//SP = ARG + 1
	@ARG
	D=M
	D=D+1
	@SP
	M=D
//THAT = *(endFrame – 1)
	@endFrame.2
	D=M
	@1
	D=D-A
	A=D
	D=M
	@THAT
	M=D
//THIS = *(endFrame – 2)
	@endFrame.2
	D=M
	@2
	D=D-A
	A=D
	D=M
	@THIS
	M=D
//ARG = *(endFrame – 3)
	@endFrame.2
	D=M
	@3
	D=D-A
	A=D
	D=M
	@ARG
	M=D
//LCL = *(endFrame – 4)
	@endFrame.2
	D=M
	@4
	D=D-A
	A=D
	D=M
	@LCL
	M=D
//goto retAddr.2
	@retAddr.2
	A=M
	0;JMP
(IF_FALSE)
//push argument 0
	@ARG
	D=M
	@0
	D=D+A
	A=D
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push constant 2
	@2
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//sub
	@SP
	M=M-1
	A=M
	D=M
	@SP
	M=M-1
	A=M
	M=M-D
	@SP
	M=M+1
//Call
//push retAddrLabel
	@Main.fibonacci$ret.2
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push LCL
	@LCL
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push ARG
	@ARG
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push THIS
	@THIS
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push THAT
	@THAT
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//ARG = SP-5-nArgs
	@SP
	D=M
	@6
	D=D-A
	@ARG
	M=D
//LCL = SP
	@SP
	D=M
	@LCL
	M=D
//goto Main.fibonacci
	@Main.fibonacci
	0;JMP
(Main.fibonacci$ret.2)
//push argument 0
	@ARG
	D=M
	@0
	D=D+A
	A=D
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push constant 1
	@1
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//sub
	@SP
	M=M-1
	A=M
	D=M
	@SP
	M=M-1
	A=M
	M=M-D
	@SP
	M=M+1
//Call
//push retAddrLabel
	@Main.fibonacci$ret.3
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push LCL
	@LCL
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push ARG
	@ARG
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push THIS
	@THIS
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push THAT
	@THAT
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//ARG = SP-5-nArgs
	@SP
	D=M
	@6
	D=D-A
	@ARG
	M=D
//LCL = SP
	@SP
	D=M
	@LCL
	M=D
//goto Main.fibonacci
	@Main.fibonacci
	0;JMP
(Main.fibonacci$ret.3)
//add
	@SP
	M=M-1
	A=M
	D=M
	@SP
	M=M-1
	A=M
	M=M+D
	@SP
	M=M+1
//Return
//endFrame = LCL
	@LCL
	D=M
	@endFrame.4
	M=D
//retAddr = *(endFrame – 5)
	@5
	D=A
	@endFrame.4
	D=M-D
	A=D
	D=M
	@retAddr.4
	M=D
//*ARG = pop()
	@SP
	M=M-1
	A=M
	D=M
	@ARG
	A=M
	M=D
//SP = ARG + 1
	@ARG
	D=M
	D=D+1
	@SP
	M=D
//THAT = *(endFrame – 1)
	@endFrame.4
	D=M
	@1
	D=D-A
	A=D
	D=M
	@THAT
	M=D
//THIS = *(endFrame – 2)
	@endFrame.4
	D=M
	@2
	D=D-A
	A=D
	D=M
	@THIS
	M=D
//ARG = *(endFrame – 3)
	@endFrame.4
	D=M
	@3
	D=D-A
	A=D
	D=M
	@ARG
	M=D
//LCL = *(endFrame – 4)
	@endFrame.4
	D=M
	@4
	D=D-A
	A=D
	D=M
	@LCL
	M=D
//goto retAddr.4
	@retAddr.4
	A=M
	0;JMP
