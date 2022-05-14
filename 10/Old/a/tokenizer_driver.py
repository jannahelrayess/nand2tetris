"""
tokenizer_driver.py
Jannah El-Rayess
2022-04-02

A driver program for testing the correctness of the jack_tokenizer program.
Produces an XML file containing each token and its classification.
In the Computing Systems textbook, this is considered a basic version of 
the Jack analyzer.
"""

import os
import sys
import jack_tokenizer

def main():
    inputFileName = sys.argv[1]
    if os.path.isfile(inputFileName): # Handle a single file
        outputFileName = inputFileName[:-5] + 'T1.xml' # Differentiate from provided output
        outfp = open(outputFileName, 'w')
        tokenizer = jack_tokenizer.JackTokenizer(inputFileName)
        tokenize(tokenizer, outfp)
        outfp.close()
        os.remove(tokenizer.get_out_file())
    else: # Handle a folder
        os.chdir(inputFileName) # Enter folder
        for f in os.listdir():
            if os.path.isfile(f) and f[-5:] == '.jack': # Only process Jack files
                outputFileName = f[:-5] + 'T1.xml' # Differentiate from provided output
                outfp = open(outputFileName, 'w')
                tokenizer = jack_tokenizer.JackTokenizer(f)
                tokenize(tokenizer, outfp)
                outfp.close()
                os.remove(tokenizer.get_out_file())

def tokenize(tokenizer, outfp):
    """ Prints each token and its classification according to the form
        <tokenType> token </tokenType> to an XML file.

    Parameters:
        tokenizer: A jackTokenizer
        outfp: A file object for the output XML file

    Return type: None
    """
    special_symbols = {'<':'&lt;', '>':'&gt;', '"': '&quote;', '&': '&amp;'}
    
    print('<tokens>', file=outfp)

    while tokenizer.hasMoreTokens():
        tokenizer.advance()
        
        # Construct tag name
        if tokenizer.tokenType() == 'INT_CONST':
            tagName = 'integerConstant'
        elif tokenizer.tokenType() == 'STRING_CONST':
            tagName = 'stringConstant'
        else:
            tagName = tokenizer.tokenType().lower()

        line = '<' + tagName + '> ' # Open tag
        
        # Add the token
        if tokenizer.tokenType() == 'KEYWORD':
            line += tokenizer.keyWord().lower()
        elif tokenizer.tokenType() == 'SYMBOL':
            if tokenizer.symbol() in special_symbols:
                line += special_symbols[tokenizer.symbol()]
            else:
                line += tokenizer.symbol()
        elif tokenizer.tokenType() == 'IDENTIFIER':
            line += tokenizer.identifier()
        elif tokenizer.tokenType() == 'INT_CONST':
            line += str(tokenizer.intVal())
        else:
            line += tokenizer.stringVal()

        line += ' </' + tagName + '>' # Close tag
        
        # Write line of XML to output file and advance the tokenizer
        print(line, file=outfp)

    print('</tokens>', file=outfp)
    
main()
