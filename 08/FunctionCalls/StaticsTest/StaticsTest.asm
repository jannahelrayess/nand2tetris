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
//push constant 6
	@6
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push constant 8
	@8
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//Call
//push retAddrLabel
	@Class1.set$ret.1
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
	@7
	D=D-A
	@ARG
	M=D
//LCL = SP
	@SP
	D=M
	@LCL
	M=D
//goto Class1.set
	@Class1.set
	0;JMP
(Class1.set$ret.1)
//pop temp 0
	@SP
	M=M-1
	A=M
	D=M
	@5
	M=D
//push constant 23
	@23
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push constant 15
	@15
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//Call
//push retAddrLabel
	@Class2.set$ret.2
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
	@7
	D=D-A
	@ARG
	M=D
//LCL = SP
	@SP
	D=M
	@LCL
	M=D
//goto Class2.set
	@Class2.set
	0;JMP
(Class2.set$ret.2)
//pop temp 0
	@SP
	M=M-1
	A=M
	D=M
	@5
	M=D
//Call
//push retAddrLabel
	@Class1.get$ret.3
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
//goto Class1.get
	@Class1.get
	0;JMP
(Class1.get$ret.3)
//Call
//push retAddrLabel
	@Class2.get$ret.4
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
//goto Class2.get
	@Class2.get
	0;JMP
(Class2.get$ret.4)
(WHILE)
//goto WHILE
	@WHILE
	0;JMP
//Function
(Class1.set)
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
//pop static 0
	@SP
	M=M-1
	A=M
	D=M
	@Class1.StaticsTest.0
	M=D
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
//pop static 1
	@SP
	M=M-1
	A=M
	D=M
	@Class1.StaticsTest.1
	M=D
//push constant 0
	@0
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//Return
//endFrame = LCL
	@LCL
	D=M
	@endFrame.5
	M=D
//retAddr = *(endFrame – 5)
	@5
	D=A
	@endFrame.5
	D=M-D
	A=D
	D=M
	@retAddr.5
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
	@endFrame.5
	D=M
	@1
	D=D-A
	A=D
	D=M
	@THAT
	M=D
//THIS = *(endFrame – 2)
	@endFrame.5
	D=M
	@2
	D=D-A
	A=D
	D=M
	@THIS
	M=D
//ARG = *(endFrame – 3)
	@endFrame.5
	D=M
	@3
	D=D-A
	A=D
	D=M
	@ARG
	M=D
//LCL = *(endFrame – 4)
	@endFrame.5
	D=M
	@4
	D=D-A
	A=D
	D=M
	@LCL
	M=D
//goto retAddr.5
	@retAddr.5
	A=M
	0;JMP
//Function
(Class1.get)
//push static 0
	@Class1.StaticsTest.0
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push static 1
	@Class1.StaticsTest.1
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
	@endFrame.5
	M=D
//retAddr = *(endFrame – 5)
	@5
	D=A
	@endFrame.5
	D=M-D
	A=D
	D=M
	@retAddr.5
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
	@endFrame.5
	D=M
	@1
	D=D-A
	A=D
	D=M
	@THAT
	M=D
//THIS = *(endFrame – 2)
	@endFrame.5
	D=M
	@2
	D=D-A
	A=D
	D=M
	@THIS
	M=D
//ARG = *(endFrame – 3)
	@endFrame.5
	D=M
	@3
	D=D-A
	A=D
	D=M
	@ARG
	M=D
//LCL = *(endFrame – 4)
	@endFrame.5
	D=M
	@4
	D=D-A
	A=D
	D=M
	@LCL
	M=D
//goto retAddr.5
	@retAddr.5
	A=M
	0;JMP
//Function
(Class2.set)
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
//pop static 0
	@SP
	M=M-1
	A=M
	D=M
	@Class2.StaticsTest.0
	M=D
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
//pop static 1
	@SP
	M=M-1
	A=M
	D=M
	@Class2.StaticsTest.1
	M=D
//push constant 0
	@0
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//Return
//endFrame = LCL
	@LCL
	D=M
	@endFrame.5
	M=D
//retAddr = *(endFrame – 5)
	@5
	D=A
	@endFrame.5
	D=M-D
	A=D
	D=M
	@retAddr.5
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
	@endFrame.5
	D=M
	@1
	D=D-A
	A=D
	D=M
	@THAT
	M=D
//THIS = *(endFrame – 2)
	@endFrame.5
	D=M
	@2
	D=D-A
	A=D
	D=M
	@THIS
	M=D
//ARG = *(endFrame – 3)
	@endFrame.5
	D=M
	@3
	D=D-A
	A=D
	D=M
	@ARG
	M=D
//LCL = *(endFrame – 4)
	@endFrame.5
	D=M
	@4
	D=D-A
	A=D
	D=M
	@LCL
	M=D
//goto retAddr.5
	@retAddr.5
	A=M
	0;JMP
//Function
(Class2.get)
//push static 0
	@Class2.StaticsTest.0
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//push static 1
	@Class2.StaticsTest.1
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
	@endFrame.5
	M=D
//retAddr = *(endFrame – 5)
	@5
	D=A
	@endFrame.5
	D=M-D
	A=D
	D=M
	@retAddr.5
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
	@endFrame.5
	D=M
	@1
	D=D-A
	A=D
	D=M
	@THAT
	M=D
//THIS = *(endFrame – 2)
	@endFrame.5
	D=M
	@2
	D=D-A
	A=D
	D=M
	@THIS
	M=D
//ARG = *(endFrame – 3)
	@endFrame.5
	D=M
	@3
	D=D-A
	A=D
	D=M
	@ARG
	M=D
//LCL = *(endFrame – 4)
	@endFrame.5
	D=M
	@4
	D=D-A
	A=D
	D=M
	@LCL
	M=D
//goto retAddr.5
	@retAddr.5
	A=M
	0;JMP
