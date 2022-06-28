"""
CompilationEngine.py
Jannah El-Rayess
2022-05-13

A program that compiles jack code into its respective VM code whilst following jack grammar.
"""

class CompilationEngine():
    def __init__(self, tokenizer, table, writer):
        self.__tokenizer = tokenizer 
        self.__table = table 
        self.__write = writer
        self.__void = False
        self.__sub_type = ""
        self.__class_name = ""
        self.__function_name = ""
        self.__if_label_counter = 0
        self.__while_label_counter = 0
        self.__exp_counter = 0
 
    # __token: -> str
    # Returns the current token
    def __token(self):
        if self.__tokenizer.tokenType() == "STRING_CONST":
            return self.__tokenizer.stringVal()
        else:
            return self.__tokenizer.get_token()

    # __compileMultiVarName: str bool str -> 
    # Compiles multiple variables whether they are of the same type or not
    def __compileMultiVarName(self, type, need, kind):
        while self.__token() == ",":
            self.__tokenizer.advance() # type or varName
            # Compiles type if needed
            if need:
                type = self.__token()
                self.__tokenizer.advance() # varName
            # Compiles varName
            name = self.__token()
            self.__table.define(name, type, kind.upper()) # add variable to symbol table
            self.__tokenizer.advance() # next token

    # __subroutineCall: ->
    # Compiles when a subroutine is called 
    def __subroutineCall(self, identifier):
        # A method that is called within its own class
        if self.__token() == '(':
            self.__tokenizer.advance() # next token
            self.__write.writePush("POINTER", 0) 
            self.compileExpressionList()
            self.__write.writeCall(f"{self.__class_name}.{identifier}", self.__exp_counter + 1)
            self.__tokenizer.advance() # next token
        # Could be a method, function, or constructor
        elif self.__token() == '.':
            self.__tokenizer.advance() # subroutineName
            subroutineName = self.__token()
            self.__tokenizer.advance() # (
            self.__tokenizer.advance() # next token
            # If the subroutine is called on a variable, it must be a method
            if self.__table.inTable(identifier): # varName
                self.__write.writePush(self.__table.kindOf(identifier), self.__table.indexOf(identifier)) # push varName
                self.compileExpressionList()
                self.__write.writeCall(f"{self.__table.typeOf(identifier)}.{subroutineName}", self.__exp_counter + 1) 
                self.__tokenizer.advance() # next token
            # Otherwise, the subroutine is a function from a particular class
            else: # className
                self.compileExpressionList()
                self.__write.writeCall(f"{identifier}.{subroutineName}", self.__exp_counter)
                self.__tokenizer.advance() # next token

    # compileClass: ->
    # Compiles a class
    def compileClass(self):
        self.__tokenizer.advance() # class
        self.__tokenizer.advance() # className
        self.__class_name = self.__token() 
        self.__tokenizer.advance() # {
        self.__tokenizer.advance()
        # While class wide variables are being declared
        while self.__token() in ["static", "field"]:
            self.compileClassVarDec()
        # While there are subroutines within the class
        while self.__token() in ["constructor", "function", "method"]:
            self.compileSubroutineDec()
            self.__tokenizer.advance()

    # compileClassVarDec: ->
    # Saves class wide variable declarations in the class symbol table
    def compileClassVarDec(self):
        kind = self.__token()
        self.__tokenizer.advance() # type 
        type = self.__token()
        self.__tokenizer.advance() # varName
        name = self.__token()
        self.__table.define(name, type, kind.upper()) # add first variable to class symbol table
        self.__tokenizer.advance() # , 
        self.__compileMultiVarName(type, False, kind.upper())
        self.__tokenizer.advance() # next token

    # compileSubroutineDec: ->
    # Compiles the the entire subroutine from variable decleration to the body
    def compileSubroutineDec(self):
        # Saves the type of subroutine the current one is
        if self.__token() == "function":
            self.__sub_type = "function" 
        elif self.__token() == "method":
            self.__sub_type = "method"
        elif self.__token() == "constructor":
            self.__sub_type = "constructor"
        # Resets the symbol table for the new subroutine
        self.__table.startSubroutine(self.__sub_type)
        self.__tokenizer.advance() # void or type
        # Saves whether the current subroutine is void
        if self.__token() == "void":
            self.__void = True
        self.__tokenizer.advance() # subroutineName
        self.__function_name = self.__token()
        self.__tokenizer.advance() # (
        self.__tokenizer.advance() # next token
        self.compileParameterList()
        self.__tokenizer.advance()
        self.compileSubroutineBody()
 
    # compileParameterList: ->
    # Compiles parameter list that containts the arguments of the current subroutine
    def compileParameterList(self):
        # Check if the current token is a type
        if self.__token() in ["int", "char", "boolean"] or self.__tokenizer.tokenType() == "IDENTIFIER":
            type = self.__token()
            kind = "ARG" 
            self.__tokenizer.advance() # varName
            name = self.__token()
            self.__table.define(name, type, kind.upper())
            self.__tokenizer.advance() # , or )
            self.__compileMultiVarName(type, True, kind.upper())

    # compileSubroutineBody: ->
    # Compiles the body of the subroutine, which is the statements within it 
    def compileSubroutineBody(self):
        self.__tokenizer.advance() # next token
        # Saves the local variables in the subroutine symbol table
        while self.__token() == "var":
            self.compileVarDec()
        # Writes function
        self.__write.writeFunction(f"{self.__class_name}.{self.__function_name}", self.__table.varCount("VAR"))
        if self.__sub_type == "method":
            self.__write.writePush("ARG", 0) # push argument 0
            self.__write.writePop("POINTER", 0) # pop pointer 0
        elif self.__sub_type == "constructor":
            self.__write.writePush("CONSTANT", self.__table.varCount("FIELD")) # push constant fields
            self.__write.writeCall("Memory.alloc", 1) # call Memory.alloc 1 
            self.__write.writePop("POINTER", 0) # pop pointer 0
        self.compileStatements()

    # compileVarDec: ->
    # Saves subroutine variable declarations in the subroutine symbol table 
    def compileVarDec(self):
        self.__tokenizer.advance() # type
        type = self.__token()
        self.__tokenizer.advance() # varName
        name = self.__token()
        kind = "VAR"
        self.__table.define(name, type, kind.upper())
        self.__tokenizer.advance() # , 
        self.__compileMultiVarName(type, False, kind.upper())
        self.__tokenizer.advance() # next token

    # compileStatements: ->
    # Compiles let, if, while, do, and return statements 
    def compileStatements(self):
        while self.__token() in ["let", "if", "while", "do", "return"]:
            if self.__token() == "let":
                self.compileLet()
            elif self.__token() == "if":
                self.__if_label_counter += 1 
                self.compileIf()
            elif self.__token() == "while":
                self.__while_label_counter += 1 
                self.compileWhile()
            elif self.__token() == "do":
                self.compileDo()
            elif self.__token() == "return":
                self.compileReturn()

    # compileLet: ->
    # Compiles a let statement
    def compileLet(self):
        self.__tokenizer.advance() # varName
        identifier = self.__token()
        self.__tokenizer.advance() # [ or =
        # If the left-hand side of the let statement is an array
        if self.__token() == "[": # array access
            self.__write.writePush(self.__table.kindOf(identifier), self.__table.indexOf(identifier)) # push array
            self.__tokenizer.advance() # next token
            self.compileExpression() # expression 1
            self.__exp_counter = 0
            self.__tokenizer.advance() # =
            self.__tokenizer.advance() # next token
            self.__write.writeArithmetic("ADD") # add
            self.compileExpression() # expression 2
            self.__exp_counter = 0
            self.__write.writePop("TEMP", 0) # pop temp 0
            self.__write.writePop("POINTER", 1) # pop pointer 1
            self.__write.writePush("TEMP", 0) # push temp 0
            self.__write.writePop("THAT", 0) # pop that 0
            self.__tokenizer.advance() # next token
        else: # normal let
            self.__tokenizer.advance() # next token
            self.compileExpression()
            self.__exp_counter = 0
            self.__write.writePop(self.__table.kindOf(identifier), self.__table.indexOf(identifier)) # pop varName
            self.__tokenizer.advance() # next token

    # compileIf: ->
    # Compiles an if statement
    def compileIf(self):
        self.__tokenizer.advance() # (
        self.__tokenizer.advance() # next token
        self.compileExpression()
        self.__write.writeArithmetic("NOT") # not
        L1 = f"if.L1.{self.__if_label_counter}"
        L2 = f"if.L2.{self.__if_label_counter}"  
        self.__write.writeIf(f"{L1}") # if-goto L1
        self.__tokenizer.advance() # {
        self.__tokenizer.advance() # next token 
        self.compileStatements() # statements 1
        self.__write.writeGoto(f"{L2}") # goto L1
        self.__write.writeLabel(f"{L1}") # L1
        self.__tokenizer.advance() # else?
        if self.__token() == "else": 
            self.__tokenizer.advance() # {
            self.__tokenizer.advance() # next token 
            self.compileStatements() # statements 2
            self.__tokenizer.advance() # next token 
        self.__write.writeLabel(f"{L2}") # L2

    # compileWhile: ->
    # Compiles a while statement
    def compileWhile(self):
        self.__tokenizer.advance() # (
        self.__tokenizer.advance() # next token
        L1 = f"while.L1.{self.__while_label_counter}" 
        L2 = f"while.L2.{self.__while_label_counter}" 
        self.__write.writeLabel(f"{L1}") # L1 
        self.compileExpression()
        self.__write.writeArithmetic("NOT") # not
        self.__tokenizer.advance() # {
        self.__tokenizer.advance() # next token
        self.__write.writeIf(f"{L2}") # if-goto L2
        self.compileStatements()
        self.__write.writeGoto(f"{L1}") # goto L1
        self.__write.writeLabel(f"{L2}") # L2 
        self.__tokenizer.advance() # next token

    # compileDo: ->
    # Compiles a do statement
    def compileDo(self):
        self.__tokenizer.advance() # identifier
        identifier = self.__token() 
        self.__tokenizer.advance() # next token
        self.__subroutineCall(identifier)
        self.__exp_counter = 0
        self.__write.writePop("TEMP", 0) 
        self.__tokenizer.advance() # next token

    # compileReturn: ->
    # Compiles a return statement
    def compileReturn(self):
        self.__tokenizer.advance() # next token
        # Check if the current token is the start of an expression
        if self.__token() in ["true", "false", "null", "this", "(", "-", "~"] or self.__tokenizer.tokenType() in ["INT_CONST", "STRING_CONST", "IDENTIFIER"]:
            self.compileExpression()
        # Pushes constant 0 if the current subroutine is void so it returns something
        elif self.__void == True:
            self.__write.writePush("CONSTANT", 0) # push constant 0
        self.__write.writeReturn()
        self.__tokenizer.advance() # }

    # compileExpression: -> 
    # Compiles an expression by compiling the left-hand side before an operator first,
    # And then compiling the right-hand side of the operator recursively
    def compileExpression(self):
        self.compileTerm()
        op = ""
        # While the current token is an operator, keep translating the expression
        while self.__token() in ["+", "-", "*", "/", "&", "|", "<", ">", "="]:
            op = self.__token()
            self.__tokenizer.advance() # next token
            self.compileTerm() 
        # Writes the operator after the left and right hand sides of the operator
        if op == "+":
            self.__write.writeArithmetic("ADD")
        elif op == "-":
            self.__write.writeArithmetic("SUB")
        elif op == "*":
            self.__write.writeCall("Math.multiply", 2)
        elif op == "/":
            self.__write.writeCall("Math.divide", 2)
        elif op == "|":
            self.__write.writeArithmetic("OR")
        elif op == "=":
            self.__write.writeArithmetic("EQ")
        elif op == "<":
            self.__write.writeArithmetic("LT")
        elif op == ">":
            self.__write.writeArithmetic("GT")
        elif op == "&":
            self.__write.writeArithmetic("AND")

    # compileTerm: -> 
    # Compiles a term that is either an integer, string, keyword in jack, variable, 
    # Array, called subroutine, expression, or a term with a unary operator
    def compileTerm(self):
        # If the term is an integer
        if self.__tokenizer.tokenType() == "INT_CONST":
            self.__write.writePush("CONSTANT", self.__token())
            self.__tokenizer.advance() 
        # If the term is a string 
        elif self.__tokenizer.tokenType() == "STRING_CONST":
            self.__write.writePush("CONSTANT", str(len(self.__token())))
            self.__write.writeCall("String.new", 1) # Creates a new string
            for char in self.__token():
                self.__write.writePush("CONSTANT", ord(char)) # Pushes the unicode of the given character 
                self.__write.writeCall("String.appendChar", 2) # Appends each character from the string
            self.__tokenizer.advance()
        # If the term is a keyword in jack
        elif self.__token() in ["true", "false", "null", "this"]:
            if self.__token() == "true":
                self.__write.writePush("CONSTANT", 1) 
                self.__write.writeArithmetic("NEG")  
            elif self.__token() in ["false", "null"]:
                self.__write.writePush("CONSTANT", 0)  
            elif self.__token() == "this":
                self.__write.writePush("POINTER", 0) 
            self.__tokenizer.advance()   
        elif self.__tokenizer.tokenType() == "IDENTIFIER": # varName, subroutineName, or className 
            identifier = self.__token()
            self.__tokenizer.advance() # next token
            # If the term is an array
            if self.__token() == "[": # array access
                self.__write.writePush(self.__table.kindOf(identifier), self.__table.indexOf(identifier)) # push array
                self.__tokenizer.advance() # next token
                self.compileExpression() # push expression within array
                self.__tokenizer.advance() # next token
                self.__write.writeArithmetic("ADD")
                self.__write.writePop("POINTER", 1)
                self.__write.writePush("THAT", 0)
            # If the term is a called subroutine
            elif self.__token() in ['(', '.']:
                self.__subroutineCall(identifier)
            # If the term is a variable
            else: 
                self.__write.writePush(self.__table.kindOf(identifier), self.__table.indexOf(identifier)) # push varName
        # If the term is an expression
        elif self.__token() == "(":
            self.__tokenizer.advance() # next token
            self.compileExpression()
            self.__tokenizer.advance() # next token
        # If the term has a unary operator before it 
        elif self.__token() in ["-", "~"]: # unaryOp
            op = self.__token()
            self.__tokenizer.advance() # next token
            self.compileTerm()
            # Writes the unary operator after the term
            if op == "-":
                self.__write.writeArithmetic("NEG") 
            else:
                self.__write.writeArithmetic("NOT")  

    # compileExpressionList: ->
    # Compiles a list of expressions
    def compileExpressionList(self):
        # Check if the current token is the start of an expression
        if self.__token() in ["true", "false", "null", "this", "(", "-", "~"] or self.__tokenizer.tokenType() in ["INT_CONST", "STRING_CONST", "IDENTIFIER"]:
            self.compileExpression()
            self.__exp_counter += 1
            # Compiles multiple expressions
            while self.__token() == ",":
                self.__tokenizer.advance() # ,
                self.compileExpression()
                self.__exp_counter += 1