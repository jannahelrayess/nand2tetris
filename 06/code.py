# A Code class for translating C-instructions
class Code:
    def __init__(self, dest, comp, jump):
        self.__dest = dest
        self.__comp = comp
        self.__jump = jump

        self.__destDIC = {
            "null": "000",
            "M": "001",
            "D": "010",
            "DM": "011",
            "MD": "011", 
            "A": "100",
            "AM": "101",
            "MA": "101",
            "AD": "110",
            "DA": "110",
            "AMD": "111",
            "ADM": "111",
            "DMA": "111",
            "DAM": "111",
            "MAD": "111",
            "MDA": "111",
        }

        self.__compDIC = {
            "0": "0101010",
            "1": "0111111",
            "-1": "0111010",
            "D": "0001100", 
            "A": "0110000",
            "!D": "0001101",
            "!A": "0110001",
            "-D": "0001111",
            "-A": "0110011",
            "D+1": "0011111",
            "A+1": "0110111",
            "D-1": "0001110", 
            "A-1": "0110010",
            "D+A": "0000010",
            "D-A": "0010011",
            "A-D": "0000111",
            "D&A": "0000000",
            "D|A": "0010101",
            "M": "1110000",
            "!M": "1110001",
            "-M": "1110011",
            "M+1": "1110111",
            "M-1": "1110010",
            "D+M": "1000010",
            "D-M": "1010011",
            "M-D": "1000111",
            "D&M": "1000000",
            "D|M": "1010101"
        }

        self.__jumpDIC = {
            "null": "000",
            "JGT": "001",
            "JEQ": "010",
            "JGE": "011", 
            "JLT": "100",
            "JNE": "101",
            "JLE": "110",
            "JMP": "111"
        }

    # destC: -> str
    # Returns the dest bits in binary that correspond to the dest symbolic code using the dest dictionary 
    def destC(self):
        if self.__dest == '':
            return self.__destDIC['null']
        else:
            return self.__destDIC[self.__dest]

    # compC: -> str
    # Returns the comp bits in binary that correspond to the comp symbolic code using the comp dictionary 
    def compC(self):
        if self.__comp == '':
            return ''
        else:
            return self.__compDIC[self.__comp]
    
    # jumpC: -> str
    # Returns the jump bits in binary that correspond to the jump symbolic code using the jump dictionary 
    def jumpC(self):
        if self.__jump == '':
            return self.__jumpDIC['null']
        else:
            return self.__jumpDIC[self.__jump]