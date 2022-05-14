# Jannah El-Rayess
# 2021-12-17
# code_writer.py
# A CodeWriter class that translates each type of vm code to asm code.

class CodeWriter:

    # Constructor 
    def __init__(self, output_file):
        self.__output_file = open(output_file, "w")
        self.__label_counter = 0
        self.__var_name = output_file[:-4]
    
    # writeArithmetic: str -> 
    # Translates an arithmetic vm line of code to asm and writes the translated 
    # Line to the output file as a side effect. 
    def writeArithmetic(self, command):
        final_line = "\t//" + command + "\n\t"
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
        final_line = "\t//" + arg1 + " " + arg2 + " " + "\n\t" 
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
                static_name = self.__var_name + "." + arg2
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
                static_name = self.__var_name + "." + arg2
                final_line += f"@SP\n\tM=M-1\n\tA=M\n\tD=M\n\t@{static_name}\n\tM=D\n"
            # Translates pop pointer 
            elif segment == "pointer":
                final_line += f"@SP\n\tM=M-1\n\tA=M\n\tD=M\n\t@{this_or_that[int(arg2)]}\n\tM=D\n"
            # Translates pop temp
            elif segment == "temp":
                final_line += f"@SP\n\tM=M-1\n\tA=M\n\tD=M\n\t@{5+int(arg2)}\n\tM=D\n"
        
        self.__output_file.write(final_line)

    # close: ->
    # Closes the output file 
    def close(self):
        self.__output_file.write('(LOOP)\n\t@LOOP\n\t0;JMP\n')
        self.__output_file.close()