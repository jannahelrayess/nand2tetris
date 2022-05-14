"""
SymbolTable.py
Jannah El-Rayess
2022-05-13

A simple program that creates a class wide and subroutine symbol 
Tables where variables are stored.
"""

class SymbolTable():
    def __init__(self):
        self.__class_table = {}
        self.__sub_table = {}
        self.__countSTATIC = 0
        self.__countFIELD = 0
        self.__countARG = 0
        self.__countVAR = 0
    
    # inTable: str -> bool
    # Returns whether the given variable is defined in either 
    # The class wide or subroutine symbol table
    def inTable(self, name):
        return name in self.__class_table.keys() or name in self.__sub_table.keys()
     
    # kindOf: str -> str
    # Returns the kind of the variable given
    def kindOf(self, name): 
        if name in self.__sub_table.keys():
            return self.__sub_table[name][1]
        elif name in self.__class_table.keys():
            return self.__class_table[name][1]
        else:
            return "NONE"
    
    # typeOf: str -> str
    # Returns the type of the variable given
    def typeOf(self, name):
        if name in self.__sub_table.keys():
            return self.__sub_table[name][0]
        elif name in self.__class_table.keys():
            return self.__class_table[name][0]
    
    # indexOf: str -> int
    # Returns the index of the variable given
    def indexOf(self, name):
        if name in self.__sub_table.keys():
            return self.__sub_table[name][2]
        elif name in self.__class_table.keys():
            return self.__class_table[name][2]
    
    # startSubroutine: str ->
    # Resets the argument and local variable counters as well as 
    # Clears the subroutine table for the purpose of starting a
    # New subroutine
    def startSubroutine(self, type):
        if type == "method":
            self.__countARG = 1
        else:
            self.__countARG = 0
        self.__countVAR = 0
        self.__sub_table.clear()
    
    # define: str str str ->
    # Defines a new variable in either the class or subroutine 
    # Symbol table
    def define(self, name, type, kind):
        if kind == "STATIC":
            self.__class_table[name] = (type, kind.lower(), self.__countSTATIC)
            self.__countSTATIC += 1
        elif kind == "FIELD":
            self.__class_table[name] = (type, "this", self.__countFIELD)
            self.__countFIELD += 1
        elif kind == "ARG":
            self.__sub_table[name] = (type, "argument", self.__countARG)
            self.__countARG += 1
        elif kind == "VAR":
            self.__sub_table[name] = (type, "local", self.__countVAR)
            self.__countVAR += 1
    
    # varCount: str ->
    # Returns the number of variables of the given kind
    def varCount(self, kind):
        if kind == "STATIC":
            return self.__countSTATIC
        elif kind == "FIELD":
            return self.__countFIELD
        elif kind == "ARG":
            return self.__countARG
        elif kind == "VAR":
            return self.__countVAR