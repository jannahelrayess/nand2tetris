"""
jack_analyzer.py
Jannah El-Rayess
2022-04-14

A program that runs the compilation process using the compilation engine 
As well as the tokenizer in order to translate a given jack program 
Into its respective xml file.
"""

import jack_tokenizer
import compilation_engine
import os
import sys

# main: ->
# Main function that runs the compilation program 
def main():
    inputFileName = sys.argv[1]
    # Handles a single file
    if os.path.isfile(inputFileName):
        outputFileName = inputFileName[:-5] + 'T2.xml' 
        outfp = open(outputFileName, 'w')
        tokenizer = jack_tokenizer.JackTokenizer(inputFileName)
        engine = compilation_engine.CompilationEngine(outfp, tokenizer) 
        engine.compileClass()
        outfp.close()
        os.remove(tokenizer.get_out_file())
    # Handles a folder
    else:
        os.chdir(inputFileName) 
        for f in os.listdir():
            if os.path.isfile(f) and f[-5:] == '.jack':
                inputFileName = f
                outputFileName = f[:-5] + 'T2.xml' 
                outfp = open(outputFileName, 'w')
                tokenizer = jack_tokenizer.JackTokenizer(inputFileName)
                engine = compilation_engine.CompilationEngine(outfp, tokenizer) 
                engine.compileClass()
                outfp.close()
                os.remove(tokenizer.get_out_file())

# Calls main to run the program 
main()
