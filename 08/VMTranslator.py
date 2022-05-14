# Jannah El-Rayess
# 2021-12-17
# VMTranslator.py
# A program that translates vm code to asm code using the parser and code_writer classes.

# Imports 
import sys
import os
from parser import Parser
from code_writer import CodeWriter

# removeCommentSpace: str -> lst
# Takes the input asm file and return a new file without comments and white space 
# As well as how many lines of code there are. 
def removeCommentSpace(file):
    input_file = open(file, 'r')
    out_file = str(file.split('.')[0]) + '.txt'
    output_file = open(out_file, 'w+')
    file_len = 0

    for line in input_file:
        if len(line.strip()) != 0:
            if '//' in line:
                if line.split('//')[0] != '':
                    new_line = line.split('//')[0].strip()
                    output_file.write(new_line + '\n')
                    file_len += 1
            else:
                output_file.write(line.strip() + '\n')
                file_len += 1

    return [out_file, file_len] 

# translate: ->
# Translates each line of vm code based on the asm code's command type 
# And immediately writes the translated line into the output file. 
def translate(input_file, code_writer):
    file_and_len = removeCommentSpace(input_file)
    parser = Parser(file_and_len[0], file_and_len[1])
    types = ["C_PUSH", "C_POP"]
    parser.advance()

    while parser.hasMoreCommands():
        arg1 = parser.arg1()
        if parser.commandType() == "C_ARITHMETIC":
            code_writer.writeArithmetic(arg1.split()[0].strip())
        elif parser.commandType() in types:
            code_writer.writePushPop(parser.arg1(), parser.arg2()) 
        elif parser.commandType() == "C_LABEL":
            code_writer.writeLabel(arg1.split()[1].strip())
        elif parser.commandType() == "C_GOTO":
            code_writer.writeGoto(arg1.split()[1].strip())
        elif parser.commandType() == "C_IF":
            code_writer.writeIf(arg1.split()[1].strip())
        elif parser.commandType() == "C_FUNCTION":
            code_writer.writeFunction(arg1.split()[1].strip(), int(parser.arg2()))
        elif parser.commandType() == "C_RETURN":
            code_writer.writeReturn()
        elif parser.commandType() == "C_CALL":
            code_writer.writeCall(parser.arg1().split()[1].strip(), int(parser.arg2()))
        parser.advance()
    
    os.remove(file_and_len[0])

# main: ->
# Runs the translation process while considering whether what needs
# To be translated is a file or a directory. 
def main():
    user_input = sys.argv[1]
    output_file = user_input.split(".")[0] + ".asm"
    global_label_counter = 0
    global_return_counter = 0
    code_w = CodeWriter(output_file, global_label_counter, global_return_counter)
    vm_file_lst = []

    # Does not put bootstrap code in front of certain files/directories 
    if user_input.split(".")[0].strip() in ["BasicLoop", "FibonacciSeries", "SimpleFunction", "NestedCall"]:
        pass
    else:
        code_w.writeInit()

    # Translates a file.
    if os.path.isfile(user_input):
        code_w.setFileName(user_input.split(".")[0])
        translate(user_input, code_w)
    #Translates every file in the directory, but ensures that 
    # Sys.vm is translated first.
    else:
        os.chdir(os.getcwd()+f"/{user_input}")
        for file in os.listdir():
            if file[-3:] == ".vm":
                vm_file_lst.append(file[:-3]) 
        
        for vm_file in vm_file_lst:
            if vm_file == "Sys":
                code_w.setFileName(vm_file) 
                translate(vm_file + ".vm", code_w)
                vm_file_lst.remove(vm_file)
        
        for vm_file in vm_file_lst: 
            code_w.setFileName(vm_file) 
            translate(vm_file + ".vm", code_w) 

    code_w.close()

# Calls main function to run the program.
main()