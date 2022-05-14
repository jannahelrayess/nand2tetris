# Jannah El-Rayess
# 2021-12-17
# code_writer.py
# A CodeWriter class that translates each type of vm code to asm code.

class CodeWriter:

    # Constructor 
    def __init__(self, output_file, label_counter, return_counter):
        self.__output_file = open(output_file, "w")
        self.__var_name = output_file[:-4]
        self.__file_name = ""
        self.__label_counter = label_counter
        self.__return_counter = return_counter
        self.__retAddrLabel = ""
    
    # writeArithmetic: str -> 
    # Translates an arithmetic vm line of code to asm and writes the translated 
    # Line to the output file as a side effect. 
    def writeArithmetic(self, command):
        final_line = "//" + command + "\n\t"
        takes_two = {
            "add":"M=M+D\n\t", 
            "sub":"M=M-D\n\t", 
            "and":"M=M&D\n\t", 
            "or":"M=M|D\n\t"
            }
        takes_one = {
            "neg":"M=-M\n\t", 
            "not":"M=!M\n\t"
            } 
        compares = {
            "eq":"D;JEQ\n", 
            "gt":"D;JGT\n", 
            "lt":"D;JLT\n"
            }
        
        # Translates add, sub, and, or
        if command in takes_two.keys():
            final_line += "@SP\n\tM=M-1\n\tA=M\n\tD=M\n\t@SP\n\tM=M-1\n\tA=M\n\t" + takes_two[command] + "@SP\n\tM=M+1\n"
        # Translates neg, not
        elif command in takes_one.keys():
            final_line += "@SP\n\tM=M-1\n\tA=M\n\t" + takes_one[command] + "@SP\n\tM=M+1\n"
        # Translates eq, gt, lt
        elif command in compares.keys():
            true_label = "TRUE." + str(self.__label_counter)
            false_label = "FALSE." + str(self.__label_counter)
            end_label = "END." + str(self.__label_counter)
            final_line += f"@SP\n\tM=M-1\n\tA=M\n\tD=M\n\t@SP\n\tM=M-1\n\tA=M\n\tM=M-D\n\tD=M\n\t@{true_label}\n\t{compares[command]}({false_label})\n\t@SP\n\tA=M\n\tM=0\n\t@{end_label}\n\t0;JMP\n({true_label})\n\t@SP\n\tA=M\n\tM=-1\n({end_label})\n\t@SP\n\tM=M+1\n"
            self.__label_counter += 1
        
        self.__output_file.write(final_line)

    # writePushPop: str str -> 
    # Translates either a push or pop vm line of code to asm and writes the translated 
    # Line to the output file as a side effect. 
    def writePushPop(self, arg1, arg2):
        command = arg1.split()[0].strip()
        segment = arg1.split()[1].strip()
        this_or_that = ["THIS", "THAT"]
        final_line = "//" + arg1 + " " + arg2 + "\n\t"
        bases_stored = {
            "local": "LCL",
            "argument": "ARG",
            "this": "THIS",
            "that": "THAT"
        }
        
        if command == "push":
            # Translates push local, argument, this, that
            if segment in bases_stored.keys():
                final_line += f"@{bases_stored[segment]}\n\tD=M\n\t@{arg2}\n\tD=D+A\n\tA=D\n\tD=M\n\t@SP\n\tA=M\n\tM=D\n\t@SP\n\tM=M+1\n"
            # Translates push constant
            elif segment == "constant":
                final_line += f"@{arg2}\n\tD=A\n\t@SP\n\tA=M\n\tM=D\n\t@SP\n\tM=M+1\n"
            # Translates push static
            elif segment == "static":
                static_name = self.__file_name + "." + self.__var_name + "." + arg2
                final_line += f"@{static_name}\n\tD=M\n\t@SP\n\tA=M\n\tM=D\n\t@SP\n\tM=M+1\n"
            # Translates push pointer
            elif segment == "pointer":
                final_line += f"@{this_or_that[int(arg2)]}\n\tD=M\n\t@SP\n\tA=M\n\tM=D\n\t@SP\n\tM=M+1\n"
            # Translates push temp
            elif segment == "temp":
                final_line += f"@5\n\tD=A\n\t@{arg2}\n\tD=D+A\n\tA=D\n\tD=M\n\t@SP\n\tA=M\n\tM=D\n\t@SP\n\tM=M+1\n"
        elif command == "pop":
            # Translates pop local, argument, this, that 
            if segment in bases_stored.keys():
                final_line += f"@{bases_stored[segment]}\n\tD=M\n\t@{arg2}\n\tD=D+A\n\t@R13\n\tM=D\n\t@SP\n\tM=M-1\n\tA=M\n\tD=M\n\t@R13\n\tA=M\n\tM=D\n"
            # Translates pop static
            elif segment == "static":
                static_name = self.__file_name + "." + self.__var_name + "." + arg2
                final_line += f"@SP\n\tM=M-1\n\tA=M\n\tD=M\n\t@{static_name}\n\tM=D\n"
            # Translates pop pointer 
            elif segment == "pointer":
                final_line += f"@SP\n\tM=M-1\n\tA=M\n\tD=M\n\t@{this_or_that[int(arg2)]}\n\tM=D\n"
            # Translates pop temp
            elif segment == "temp":
                final_line += f"@SP\n\tM=M-1\n\tA=M\n\tD=M\n\t@{5+int(arg2)}\n\tM=D\n"
        
        self.__output_file.write(final_line)

    # Setter
    def setFileName(self, file_name):
        self.__file_name = file_name 

    # writeLabel: ->
    # Writes an asm label based on the input.  
    def writeLabel(self, label):
        self.__output_file.write(f"({label})\n") 
    
    # writeGoto: ->
    # Writes the asm code to go to a label.
    def writeGoto(self, label):
        self.__output_file.write(f"//goto {label}\n\t@{label}\n\t0;JMP\n")
    
    # writeIf: ->
    # Writes the asm code for an if statement.
    def writeIf(self, label):
        self.__output_file.write(f"//if-goto {label}\n\t@SP\n\tM=M-1\n\tA=M\n\tD=M\n\t@{label}\n\tD;JNE\n")
    
    # writeFunction: ->
    # Writes the function label in asm and pushes 0 onto the
    # Stack for as many variables the function has. 
    def writeFunction(self, function_name, num_vars):
        final_line = f"//Function\n({function_name})\n"
        final_line += (f"//push 0\n\t@0\n\tD=A\n\t@SP\n\tA=M\n\tM=D\n\t@SP\n\tM=M+1\n" * num_vars)
        self.__output_file.write(final_line)
    
    # writeCall: -> 
    # Writes the asm code for when a function is called. 
    def writeCall(self, function_name, num_args):
        bases = ["LCL", "ARG", "THIS", "THAT"]
        ARG_reset_num = str(num_args + 5)
        self.__retAddrLabel = f"{function_name}$ret.{self.__return_counter}"
        self.__return_counter += 1#change 

        # Pushes the return label and the bases onto the stack.
        final_line = f"//Call\n//push retAddrLabel\n\t@{self.__retAddrLabel}\n\tD=A\n\t@SP\n\tA=M\n\tM=D\n\t@SP\n\tM=M+1\n"
        for i in range(len(bases)):
            final_line += f"//push {bases[i]}\n\t@{bases[i]}\n\tD=M\n\t@SP\n\tA=M\n\tM=D\n\t@SP\n\tM=M+1\n"

        # Repositions ARG and LCL
        final_line += f"//ARG = SP-5-nArgs\n\t@SP\n\tD=M\n\t@{ARG_reset_num}\n\tD=D-A\n\t@ARG\n\tM=D\n"
        final_line += f"//LCL = SP\n\t@SP\n\tD=M\n\t@LCL\n\tM=D\n"

        self.__output_file.write(final_line)
        self.writeGoto(function_name)
        self.writeLabel(self.__retAddrLabel)

    # writeInit: ->
    # Writes bootstrap code.  
    def writeInit(self):
        self.__output_file.write(f"//Bootstrap\n//SP = 256\n\t@256\n\tD=A\n\t@SP\n\tM=D\n")
        self.writeCall("Sys.init", 0)

    # writeReturn: -> 
    # Writes the asm code for when return is called.
    def writeReturn(self):
        end_frame = f"endFrame.{self.__return_counter}"
        ret_addr = f"retAddr.{self.__return_counter}"
        #self.__return_counter += 1

        final_line = f"//Return\n//endFrame = LCL\n\t@LCL\n\tD=M\n\t@{end_frame}\n\tM=D\n"
        final_line += f"//retAddr = *(endFrame – 5)\n\t@5\n\tD=A\n\t@{end_frame}\n\tD=M-D\n\tA=D\n\tD=M\n\t@{ret_addr}\n\tM=D\n"
        
        # Repositions SP and the return value of the caller.
        final_line += f"//*ARG = pop()\n\t@SP\n\tM=M-1\n\tA=M\n\tD=M\n\t@ARG\n\tA=M\n\tM=D\n"
        final_line += f"//SP = ARG + 1\n\t@ARG\n\tD=M\n\tD=D+1\n\t@SP\n\tM=D\n"

        # Restores the bases.
        final_line += f"//THAT = *(endFrame – 1)\n\t@{end_frame}\n\tD=M\n\t@1\n\tD=D-A\n\tA=D\n\tD=M\n\t@THAT\n\tM=D\n"
        final_line += f"//THIS = *(endFrame – 2)\n\t@{end_frame}\n\tD=M\n\t@2\n\tD=D-A\n\tA=D\n\tD=M\n\t@THIS\n\tM=D\n"
        final_line += f"//ARG = *(endFrame – 3)\n\t@{end_frame}\n\tD=M\n\t@3\n\tD=D-A\n\tA=D\n\tD=M\n\t@ARG\n\tM=D\n"
        final_line += f"//LCL = *(endFrame – 4)\n\t@{end_frame}\n\tD=M\n\t@4\n\tD=D-A\n\tA=D\n\tD=M\n\t@LCL\n\tM=D\n"
        
        final_line += f"//goto {ret_addr}\n\t@{ret_addr}\n\tA=M\n\t0;JMP\n"
        self.__output_file.write(final_line)

    # close: ->
    # Closes the output file 
    def close(self):
        self.__output_file.close()