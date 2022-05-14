# Jannah El-Rayess
# 2021-12-17
# parser.py
# A Parser class for parsing each line of code. 

class Parser:

    # Constructor 
    def __init__(self, txt_clean, last_line_num):
        self.__file = open(txt_clean, "r")
        self.__line = None
        self.__line_num = 0
        self.__last_line_num = last_line_num
        self.__command_types = {
            "add": "C_ARITHMETIC",
            "sub": "C_ARITHMETIC",
            "neg": "C_ARITHMETIC",
            "eq": "C_ARITHMETIC",
            "gt": "C_ARITHMETIC",
            "lt": "C_ARITHMETIC",
            "and": "C_ARITHMETIC",
            "or": "C_ARITHMETIC",
            "not": "C_ARITHMETIC",
            "push": "C_PUSH",
            "pop": "C_POP",
            "label": "C_LABEL",
            "goto": "C_GOTO",
            "if-goto": "C_IF",
            "function": "C_FUNCTION",
            "return": "C_RETURN",
            "call": "C_CALL"
        }

    # Getter
    def getLine(self):
        return self.__line 

    # Getter   
    def getLineNum(self):
        return self.__line_num 

    # advance: ->
    # Advances the parser to the next line of code if there is one.
    def advance(self):
        if self.hasMoreCommands():
            self.__line = self.__file.readline().strip()
            self.__line_num += 1

    # commandType: -> str
    # Returns the line's command type.  
    def commandType(self):
        commands = self.__command_types.keys()
        for command in commands:
            if command == self.__line.split()[0].strip():
                return self.__command_types[command]

    # hasMoreCommands: -> bool
    # Returns whether there are more lines of code to parse through or not. 
    def hasMoreCommands(self):
        return self.__line_num <= self.__last_line_num
    
    # arg1: -> str
    # Returns the first argument in the line.
    def arg1(self):
        if self.commandType() != "C_RETURN":
            final_line = ""
            list_line = self.__line.split()[:2]

            for item in list_line:
                final_line += item + " "
            return final_line.strip() 
    
    # arg2: -> str
    # Returns the second argument in the line. 
    def arg2(self):
        possible_commands = ["C_PUSH", "C_POP", "C_FUNCTION", "C_CALL"]
        if self.commandType() in possible_commands:
            return self.__line.split()[2].strip()