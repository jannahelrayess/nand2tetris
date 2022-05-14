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

# main: ->
# Runs the translation process where each line of code will be translated respective
# Of the line's command type and immediately written into the output file. 
def main():
    input_file = sys.argv[1]
    file_and_len = removeCommentSpace(input_file)
    parser = Parser(file_and_len[0], file_and_len[1])
    file_name = parser.getName() + ".asm"
    clean_file_name = parser.getName() + ".txt"
    code_writer = CodeWriter(file_name) 
    types = ["C_PUSH", "C_POP"]
    parser.advance()

    while parser.hasMoreCommands():
        if parser.commandType() == "C_ARITHMETIC":
            arg1 = parser.arg1()
            code_writer.writeArithmetic(arg1.split()[0].strip())
        elif parser.commandType() in types:
            code_writer.writePushPop(parser.arg1(), parser.arg2()) 
        
        parser.advance()
    code_writer.close()
    os.remove(clean_file_name)

# Calls main function to run the program
main()