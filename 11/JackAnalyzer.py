"""
JackAnalyzer.py
Jannah El-Rayess
2022-05-13

A program that runs the compilation process using the Compilation Engine, 
Tokenizer, Symbol Table, and VM Writer classes in order to translate a given 
Jack program into its respective VM code.
"""

import JackTokenizer
import CompilationEngine
import VMWriter
import SymbolTable
import os
import sys

# main: ->
# Main function that runs the compilation program 
def main():
    inputFileName = sys.argv[1]
    # Handles a single file
    if os.path.isfile(inputFileName):
        outputFileName = inputFileName[:-5] + '.vm' 
        outfp = open(outputFileName, 'w')
        # Defined classes
        tokenizer = JackTokenizer.JackTokenizer(inputFileName)
        writer = VMWriter.VMWriter(outfp) 
        table = SymbolTable.SymbolTable()
        engine = CompilationEngine.CompilationEngine(tokenizer, table, writer) 
        # Compile jack class
        engine.compileClass()
        writer.close()
        os.remove(tokenizer.get_out_file())
    # Handles a folder
    else:
        os.chdir(inputFileName) 
        for f in os.listdir():
            if os.path.isfile(f) and f[-5:] == '.jack':
                inputFileName = f
                outputFileName = f[:-5] + '.vm' 
                outfp = open(outputFileName, 'w')
                # Defined classes
                tokenizer = JackTokenizer.JackTokenizer(inputFileName)
                writer = VMWriter.VMWriter(outfp) 
                table = SymbolTable.SymbolTable()
                engine = CompilationEngine.CompilationEngine(tokenizer, table, writer) 
                # Compile jack class 
                engine.compileClass()
                writer.close()
                os.remove(tokenizer.get_out_file())

# Calls main to run the program 
main()