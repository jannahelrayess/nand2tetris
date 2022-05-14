# A SymbolTable class for saving and accessing the symbols from the asm file
class SymbolTable:
    def __init__(self):
        self.__table = dict()

        self.__symbolDIC = {
            "R0": "0",
            "R1": "1",
            "R2": "2",
            "R3": "3",
            "R4": "4",
            "R5": "5",
            "R6": "6",
            "R7": "7",
            "R8": "8",
            "R9": "9",
            "R10": "10",
            "R11": "11",
            "R12": "12",
            "R13": "13",
            "R14": "14",
            "R15": "15",
            "SCREEN": "16384", 
            "KBD": "24576",
            "SP": "0",
            "LCL": "1",
            "ARG": "2",
            "THIS": "3",
            "THAT": "4",
        }

    def get_table(self):
        return self.__table

    # addEntry: str, str ->
    # Adds the entry given to the table
    def addEntry(self, symbol, address):
        self.__table[symbol] = address

    # contains: str -> boolean
    # Returns a boolean on whether the given symbol is in either table
    def contains(self, symbol):
        return (symbol in list(self.__table)) or (symbol in list(self.__symbolDIC))
    
    # getAddress: str -> str
    # Returns the address of the given symbol 
    def getAddress(self, symbol):
        if symbol in list(self.__table):
            return self.__table[symbol]
        elif symbol in list(self.__symbolDIC):
            return self.__symbolDIC[symbol]