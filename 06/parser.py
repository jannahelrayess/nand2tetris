# A Parser class for parsing through the asm files
class Parser:
    def __init__(self, source_txt):
        self.__file = open(source_txt, "r").read().splitlines()
        self.__line_num = -1
        self.__lines = self._removeCommentSpace()
        self.__line = None
    
    def get_len(self):
        return len(self.__lines)
    
    def get_line(self):
        return self.__line

    # _removeCommentSpace: -> list
    # Removes the comments and white space from the data file
    def _removeCommentSpace(self):
        lines = []

        for i in range(len(self.__file)):
            if self.__file[i] != '':
                if '//' in self.__file[i]:
                    if self.__file[i].split('//')[0] != '':
                        lines.append(self.__file[i].split('//')[0].strip())
                else:
                    lines.append(self.__file[i].strip())
                
        return lines
    
    # hasMoreLines: -> boolean
    # A boolean function that returns whether there are more lines or not to parse through
    def hasMoreLines(self):
        return self.__line_num < len(self.__lines) - 1
    
    # advance: ->
    # Advances in parsing if there are more lines 
    def advance(self):
        if self.hasMoreLines():
            self.__line_num += 1
            self.__line = self.__lines[self.__line_num]
    
    # instructionType: -> str
    # Returns the instruction type of the current line
    def instructionType(self):
        if "@" in self.__line:
            return "A_INSTRUCTION"
        elif "(" in self.__line:
            return "L_INSTRUCTION" 
        else:
            return "C_INSTRUCTION"
    
    # symbol: -> str
    # Returns the line without the symbols 
    def symbol(self):
        if "@" in self.__line:
            return self.__line[1:len(self.__line)]
        elif "(" in self.__line:
            return self.__line[1:len(self.__line) - 1]
    
    # dest: -> str
    # Returns the dest part of the C-instruction
    def dest(self):
        if '=' in self.__line:
            return self.__line.split('=')[0]
        else:
            return ''

    # comp: -> str
    # Returns the comp part of the C-instruction 
    def comp(self):
        if '=' in self.__line:
            line = self.__line.split('=')[1]
            if ';' in line:
                line = line.split(';')[0]
        elif ';' in self.__line:
            line = self.__line.split(';')[0]
        
        return line
    
    # jump: -> str
    # Returns the jump part of the C-instruction
    def jump(self):
        if ';' in self.__line:
            return self.__line.split(';')[1]
        else:
            return ''