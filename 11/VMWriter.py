"""
VMWriter.py
Jannah El-Rayess
2022-05-13

A simple program that writes VM code to the output VM file.
"""

class VMWriter():
    def __init__(self, output_file):
        self.__output_file = output_file
    
    # writePush: str int ->
    # Writes the VM push code to the output VM file based on the 
    # Given segment and index
    def writePush(self, segment, index):
        if segment == "VAR":
            segment = "LOCAL"
        elif segment == "ARG":
            segment = "ARGUMENT"
        self.__output_file.write(f"push {segment.lower()} {index}\n")

    # writePop: str int ->
    # Writes the VM pop code to the output VM file based on the 
    # Given segment and index
    def writePop(self, segment, index):
        if segment == "VAR":
            segment = "LOCAL"
        elif segment == "ARG":
            segment = "ARGUMENT"
        self.__output_file.write(f"pop {segment.lower()} {index}\n")
    
    # writeArithmetic: str ->
    # Writes the VM arithmetic code to the output VM file based 
    # On the given command
    def writeArithmetic(self, command):
        self.__output_file.write(f"{command.lower()}\n")

    # writeLabel: str ->
    # Writes the VM label code to the output VM file based on the 
    # Given label
    def writeLabel(self, label):
        self.__output_file.write(f"label {label}\n")

    # writeGoto: str ->
    # Writes the VM goto code to the output VM file based on the 
    # Given label
    def writeGoto(self, label):
        self.__output_file.write(f"goto {label}\n")

    # writeIf: str ->
    # Writes the VM if-goto code to the output VM file based on the 
    # Given label    
    def writeIf(self, label):
        self.__output_file.write(f"if-goto {label}\n")  
    
    # writeCall: str int ->
    # Writes the VM call code to the output VM file based on the 
    # Given function name and number of arguments
    def writeCall(self, name, nArgs):
        self.__output_file.write(f"call {name} {nArgs}\n")  
    
    # writeFunction: str int ->
    # Writes the VM function code to the output VM file based on the 
    # Given function name and number of local variables
    def writeFunction(self, name, nLocals):
        self.__output_file.write(f"function {name} {nLocals}\n") 

    # writeReturn: ->
    # Writes the VM return code to the output VM file
    def writeReturn(self):
        self.__output_file.write("return\n") 
    
    # close: ->
    # Closes the output VM file
    def close(self):
        self.__output_file.close()