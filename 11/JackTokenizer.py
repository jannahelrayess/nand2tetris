"""
JackTokenizer.py
Jannah El-Rayess
2022-05-13

A program that splits up a given jack file into its respective tokens and 
Returns these token as well as their respective token type.
"""

class JackTokenizer():
    def __init__(self, input_file):
        self.__out_file = self.__removeCommentSpace(input_file)
        self.__file = open(self.__out_file, "r") 
        self.__token_types = {
            "KEYWORD": ["class", "constructor", "function", "method", "field", 
                        "static", "var", "int", "char", "boolean", "void", 
                        "true", "false", "null", "this", "let", "do", "if", 
                        "else", "while", "return"],
            "SYMBOL": ["{", "}", "(", ")", "[", "]", ".", ",", ";", "+", 
                        "-", "*", "/", "&", "|", "<", ">", "=", "~"],
            "INT_CONST": range(0, 32768),
        }
        self.__token = None
        self.__token_num = 0
        self.__tokens_list = self.__tokenList()
        self.__tokens_list_iter = iter(self.__tokens_list) 
    
    # Getter
    def get_out_file(self):
        return self.__out_file
    
    # Getter 
    def get_token(self):
        return self.__token 
    
    # keyWord: -> str
    # Returns the current token if it is a keyword 
    def keyWord(self):
        if self.tokenType() == "KEYWORD": 
            return self.__token

    # symbol: -> str
    # Returns the current token if it is a symbol 
    def symbol(self):
        if self.tokenType() == "SYMBOL": 
            return self.__token

    # identifier: -> str
    # Returns the current token if it is an identifier  
    def identifier(self):
        if self.tokenType() == "IDENTIFIER": 
            return self.__token
    
    # intVal: -> str
    # Returns the current token if it is an integer 
    def intVal(self):
        if self.tokenType() == "INT_CONST": 
            return self.__token

    # stringVal: -> str
    # Returns the current token if it is a string  
    def stringVal(self):
        if self.tokenType() == "STRING_CONST":
            return self.__token[1:len(self.__token) - 1]
        
    # removeCommentSpace: file -> lst
    # Takes the input jack file and returns a new txt file without comments
    def __removeCommentSpace(self, file):
        input_file = open(file, 'r')
        out_file = str(file.split('.')[0]) + '.txt'
        output_file = open(out_file, 'w+')

        for line in input_file:
            if len(line.strip()) != 0:
                # Removes multiline comments
                if line.strip().startswith('/*') or line.strip().startswith("*") or "*/" in line.strip():
                    output_file.write("")
                # Removes singleline comments
                elif '//' in line:
                    if len(line.split('//')[0].strip()) != 0: 
                        new_line = line.split('//')[0].strip()
                        output_file.write(new_line + '\n')
                else:
                    output_file.write(line.strip() + '\n')
                
        return out_file
    
    # __tokenList: -> list
    # A Helper function that tokenizes the given jack program
    def __tokenList(self):
        tokens_list = []
        new_lst = []
        for line in self.__file:
            # Groups string constants together as 1 token
            if '"' in line:
                tokens = line.split('"')[0].split()
                tokens.append('"' + line.split('"')[1] + '"')
                tokens.append(line.split('"')[2].split())
            # Splits the rest of the file up by spaces
            else:
                tokens = line.split()
            for token in tokens:
                if type(token) == list:
                    token = token[0]
                tokens_list.append(token.strip())
        for item in tokens_list:
            # If a token is actually made up of multiple tokens,
            # Splits it up by symbol and appends each sub-token 
            # Including the symbols themselves 
            if '"' in item:
                new_lst.append(item)  
            elif any(symbol in item for symbol in self.__token_types["SYMBOL"]):
                item_sym_lst = []
                char_lst = [char for char in item]
                # Makes a list of all the symbols in the item made
                # Up of multiple tokens
                for char in char_lst:
                    if char in self.__token_types["SYMBOL"]:
                        item_sym_lst.append(char)
                # Splits up the multi-token item up by symbol
                for sym in item_sym_lst:
                    item_split = item.split(sym, 1) # Split by first occurrence of symbol 
                    if item_split[0] != "":
                        new_lst.append(item_split[0])
                    new_lst.append(sym)
                    if item_split[1] != "":
                        # If there are still more symbols, repeat the process recursively
                        if any(symbol in item_split[1] for symbol in self.__token_types["SYMBOL"]):
                            item = item_split[1]
                        else:
                            new_lst.append(item_split[1])    
            else:
                new_lst.append(item) 
        return new_lst

    # hasMoreTokens: -> boolean
    # Returns whether there are more tokens left or not
    def hasMoreTokens(self):
        return self.__token_num < len(self.__tokens_list)

    # advance: ->
    # Advances to the next token 
    def advance(self):
        if self.hasMoreTokens():
            self.__token = next(self.__tokens_list_iter)
            self.__token_num += 1

    # tokenType: -> str
    # Returns the token type of the current token 
    def tokenType(self):
        if self.__token in self.__token_types["KEYWORD"]:
            return "KEYWORD"
        elif self.__token in self.__token_types["SYMBOL"]:
            return "SYMBOL"
        elif self.__token in [str(n) for n in self.__token_types["INT_CONST"]]:
            return "INT_CONST"
        elif self.__token.startswith('"') and self.__token.endswith('"'):
            return "STRING_CONST"
        else:
            return "IDENTIFIER"