//Function
(SimpleFunction.test)
//push 0
	@0
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push 0
	@0
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push local 0
	@LCL
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
//push local 1
	@LCL
	D=M
	@1
	D=D+A
	A=D
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
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
//not
	@SP
	M=M-1
	A=M
	M=!M
	@SP
	M=M+1
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
//push argument 1
	@ARG
	D=M
	@1
	D=D+A
	A=D
	D=M
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
//Return
//endFrame = LCL
	@LCL
	D=M
	@endFrame.0
	M=D
//retAddr = *(endFrame – 5)
	@5
	D=A
	@endFrame.0
	D=M-D
	A=D
	D=M
	@retAddr.0
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
	@endFrame.0
	D=M
	@1
	D=D-A
	A=D
	D=M
	@THAT
	M=D
//THIS = *(endFrame – 2)
	@endFrame.0
	D=M
	@2
	D=D-A
	A=D
	D=M
	@THIS
	M=D
//ARG = *(endFrame – 3)
	@endFrame.0
	D=M
	@3
	D=D-A
	A=D
	D=M
	@ARG
	M=D
//LCL = *(endFrame – 4)
	@endFrame.0
	D=M
	@4
	D=D-A
	A=D
	D=M
	@LCL
	M=D
//goto retAddr.0
	@retAddr.0
	A=M
	0;JMP
