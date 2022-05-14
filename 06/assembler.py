'''
assembler.py is the main function that uses code.py, parser.py, and symboltable.py 
to translate asm files written in hack to binary syntax.
'''
import sys
from parser import Parser
from code import Code
from symboltable import SymbolTable

# translated: Parser, SymbolTable -> lst
# Parses through all of the asm code given and translates it into binary
def translated(data, data_table):
    trans_except_A = []
    trans_except_vars = []
    final = []
    x = 0
    var_num = 16
    
    # Parses through the code and appends the A and translated C-instructions 
    # To the trans_except_A list. Adds the label (L-instructions) symbols to
    # The symbol table if it is not already in it.
    for i in range(data.get_len()):
        data.advance()
        if data.instructionType() == "A_INSTRUCTION":
            x += 1
            trans_except_A.append(data.get_line().strip())
        elif data.instructionType() == "C_INSTRUCTION":
            x += 1
            trans_except_A.append(trans_C(data))
        elif data.instructionType() == "L_INSTRUCTION":
           if not data_table.contains(data.symbol()):
                data_table.addEntry(data.symbol(), str(x)) 

    # Loops through trans_except_A and translates the A-instructions that are 
    # Numbers, predefined variables, and Adds the undefined variables to the 
    # Symbol table. Appends the translated A-instructions, the undefined variables, 
    # And the translated C-instructions to the trans_except_vars list. 
    for i in range(len(trans_except_A)):
        if '@' in trans_except_A[i]:
            A_line = trans_except_A[i].split('@')[1]
            if A_line.isdigit():
                A_num = int(A_line)
                trans_except_vars.append(num_to_binary(A_num))
            elif data_table.contains(A_line):
                trans_except_vars.append(num_to_binary(int(data_table.getAddress(A_line))))
            else:
                if not data_table.contains(A_line):
                        data_table.addEntry(A_line, str(var_num))
                        var_num += 1
                trans_except_vars.append(trans_except_A[i])
        else:
            trans_except_vars.append(trans_except_A[i])

    # Loops through trans_except_vars and translates the leftover, previously 
    # Undefined variables and appends them as well as everything else in the list
    # To the final list.
    for i in range(len(trans_except_vars)):
        if '@' in trans_except_vars[i]:
            line = trans_except_vars[i].split('@')[1].strip()
            final.append(num_to_binary(int(data_table.getAddress(line))))
        else:
            final.append(trans_except_vars[i])
    
    # Returns the final translated list.
    return final

# num_to_binary: str -> str
# Converts a given integer to a 16 bit binary string
def num_to_binary(line):
    remainder = ''
    while int(line) > 0:
        remainder += str(line%2) 
        line = line // 2
    
    remainder = remainder + (16-len(remainder)) * '0'

    return remainder[::-1]

# trans_C: str -> str
# Translates the given line (assuming it's a C-instruction) using code.py
def trans_C(line):
    command = '111'
    code = Code(line.dest(), line.comp(), line.jump())
    command += code.compC() + code.destC() + code.jumpC()

    return command

# main: ->
# The main function that runs the assembler and outputs the translated code
# In binary to a new file it creates 
def main():
    input_file = sys.argv[1]
    parser = Parser(input_file)
    symboltable = SymbolTable()
    trans_lst = translated(parser, symboltable)
    
    file = str(input_file.split('.')[0]) + '.hack'
    output_file = open(file, 'w+')

    for i in range(len(trans_lst)):
        output_file.write(trans_lst[i] + '\n')

main()