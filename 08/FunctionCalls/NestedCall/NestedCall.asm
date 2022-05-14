//Function
(Sys.init)
//push constant 4000
	@4000
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//pop pointer 0
	@SP
	M=M-1
	A=M
	D=M
	@THIS
	M=D
//push constant 5000
	@5000
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//pop pointer 1
	@SP
	M=M-1
	A=M
	D=M
	@THAT
	M=D
//Call
//push retAddrLabel
	@Sys.main$ret.0
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
//goto Sys.main
	@Sys.main
	0;JMP
(Sys.main$ret.0)
//pop temp 1
	@SP
	M=M-1
	A=M
	D=M
	@6
	M=D
(LOOP)
//goto LOOP
	@LOOP
	0;JMP
//Function
(Sys.main)
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
//push 0
	@0
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push constant 4001
	@4001
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//pop pointer 0
	@SP
	M=M-1
	A=M
	D=M
	@THIS
	M=D
//push constant 5001
	@5001
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//pop pointer 1
	@SP
	M=M-1
	A=M
	D=M
	@THAT
	M=D
//push constant 200
	@200
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//pop local 1
	@LCL
	D=M
	@1
	D=D+A
	@R13
	M=D
	@SP
	M=M-1
	A=M
	D=M
	@R13
	A=M
	M=D
//push constant 40
	@40
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//pop local 2
	@LCL
	D=M
	@2
	D=D+A
	@R13
	M=D
	@SP
	M=M-1
	A=M
	D=M
	@R13
	A=M
	M=D
//push constant 6
	@6
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//pop local 3
	@LCL
	D=M
	@3
	D=D+A
	@R13
	M=D
	@SP
	M=M-1
	A=M
	D=M
	@R13
	A=M
	M=D
//push constant 123
	@123
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//Call
//push retAddrLabel
	@Sys.add12$ret.1
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
//goto Sys.add12
	@Sys.add12
	0;JMP
(Sys.add12$ret.1)
//pop temp 0
	@SP
	M=M-1
	A=M
	D=M
	@5
	M=D
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
//push local 2
	@LCL
	D=M
	@2
	D=D+A
	A=D
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push local 3
	@LCL
	D=M
	@3
	D=D+A
	A=D
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push local 4
	@LCL
	D=M
	@4
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
//Function
(Sys.add12)
//push constant 4002
	@4002
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//pop pointer 0
	@SP
	M=M-1
	A=M
	D=M
	@THIS
	M=D
//push constant 5002
	@5002
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//pop pointer 1
	@SP
	M=M-1
	A=M
	D=M
	@THAT
	M=D
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
//push constant 12
	@12
	D=A
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
