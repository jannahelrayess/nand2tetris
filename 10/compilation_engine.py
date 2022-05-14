"""
compilation_engine.py
Jannah El-Rayess
2022-04-14

A program that sorts each token from a jack program and compiles those tokens 
Into a xml file following the jack grammar. 
"""

class CompilationEngine():
    def __init__(self, output_file, tokenizer):
        self.__output_file = output_file 
        self.__tokenizer = tokenizer 
    
    # __compileIdentifier: ->
    # Compiles an identifier 
    def __compileIdentifier(self):
        self.__output_file.write(f"<identifier> {self.__token()} </identifier>\n")
        self.__tokenizer.advance()
    
    # __compileSymbol: ->
    # Compiles a symbol
    def __compileSymbol(self):
        self.__output_file.write(f"<symbol> {self.__token()} </symbol>\n")
        self.__tokenizer.advance() 

    # __compileType: ->
    # Compiles type 
    def __compileType(self):
        self.__output_file.write(f"<{self.__tokenizer.tokenType().lower()}> {self.__token()} </{self.__tokenizer.tokenType().lower()}>\n")
        self.__tokenizer.advance()
    
    # __token: -> string
    # Returns the current token
    def __token(self):
        if self.__tokenizer.tokenType() == "STRING_CONST":
            return self.__tokenizer.stringVal()
        # Special Symbols 
        elif self.__tokenizer.get_token() == "<":
            return "&lt;"
        elif self.__tokenizer.get_token() == ">":
            return "&gt;" 
        elif self.__tokenizer.get_token() == "&":
            return "&amp;"  
        else:
            return self.__tokenizer.get_token()
    
    # __compileMultiVarName: string -> 
    # Compiles multiple variables including type if needed
    def __compileMultiVarName(self, t):
        while self.__tokenizer.get_token() == ",":
            self.__compileSymbol()
            # Compiles type if needed
            if t == "type":
                self.__compileType()
            # Compiles varName
            self.__compileIdentifier()

    # __subroutineCall: ->
    # Compiles subroutineCall 
    def __subroutineCall(self):
        if self.__tokenizer.get_token() == '(':
            self.__compileSymbol()
            self.compileExpressionList()
            self.__compileSymbol() 
        elif self.__tokenizer.get_token() == '.':
            self.__compileSymbol()  
            # Compiles subroutineName
            self.__compileIdentifier()
            self.__compileSymbol()
            self.compileExpressionList()
            self.__compileSymbol()

    # compileClass: ->
    # Compiles class  
    def compileClass(self):
        self.__output_file.write("<class>\n")
        self.__tokenizer.advance()
        self.__output_file.write("<keyword> class </keyword>\n")
        self.__tokenizer.advance()
        # Compiles className
        self.__compileIdentifier() 
        self.__compileSymbol()
        while self.__tokenizer.get_token() in ["static", "field"]:
            self.compileClassVarDec()
        while self.__tokenizer.get_token() in ["constructor", "function", "method"]:
            self.compileSubroutineDec()
        self.__compileSymbol()
        self.__output_file.write("</class>\n")

    # compileClassVarDec: ->
    # Compiles classVarDec
    def compileClassVarDec(self):
        self.__output_file.write("<classVarDec>\n")
        # Compiles either static or field 
        self.__output_file.write(f"<keyword> {self.__token()} </keyword>\n")
        self.__tokenizer.advance()
        self.__compileType()
        # Compiles varName
        self.__compileIdentifier()
        self.__compileMultiVarName("")
        self.__compileSymbol()
        self.__output_file.write("</classVarDec>\n")

    # compileSubroutineDec: ->
    # Compiles subroutineDec
    def compileSubroutineDec(self):
        self.__output_file.write("<subroutineDec>\n")
        # Compiles either constructor, function, or method
        self.__output_file.write(f"<keyword> {self.__token()} </keyword>\n")
        self.__tokenizer.advance()
        # Compiles void or type
        self.__compileType() 
        # Compiles subroutineName
        self.__compileIdentifier()
        self.__compileSymbol()
        self.compileParameterList()
        self.__compileSymbol()
        self.compileSubroutineBody()
        self.__output_file.write("</subroutineDec>\n")

    # compileParameterList: ->
    # Compiles parameterList
    def compileParameterList(self):
        self.__output_file.write("<parameterList>\n")
        # Check if type
        if self.__tokenizer.get_token() in ["int", "char", "boolean"] or self.__tokenizer.tokenType() == "IDENTIFIER":
            self.__compileType()
            # Compiles varName
            self.__compileIdentifier()
            self.__compileMultiVarName("type")
        self.__output_file.write("</parameterList>\n")

    # compileSubroutineBody: ->
    # Compiles subroutineBody 
    def compileSubroutineBody(self):
        self.__output_file.write("<subroutineBody>\n")
        self.__compileSymbol()
        while self.__tokenizer.get_token() == "var":
            self.compileVarDec()
        self.compileStatements()
        self.__compileSymbol()
        self.__output_file.write("</subroutineBody>\n")

    # compileVarDec: ->
    # Compiles varDec 
    def compileVarDec(self):
        self.__output_file.write("<varDec>\n")
        self.__output_file.write("<keyword> var </keyword>\n")
        self.__tokenizer.advance()
        self.__compileType()
        # Compiles varName
        self.__compileIdentifier()
        self.__compileMultiVarName("")
        self.__compileSymbol()
        self.__output_file.write("</varDec>\n")

    # compileStatements: ->
    # Compiles statements 
    def compileStatements(self):
        self.__output_file.write("<statements>\n")
        while self.__tokenizer.get_token() in ["let", "if", "while", "do", "return"]:
            if self.__tokenizer.get_token() == "let":
                self.compileLet()
            if self.__tokenizer.get_token() == "if":
                self.compileIf() 
            if self.__tokenizer.get_token() == "while":
                self.compileWhile()
            if self.__tokenizer.get_token() == "do":
                self.compileDo()
            if self.__tokenizer.get_token() == "return":
                self.compileReturn()
        self.__output_file.write("</statements>\n")

    # compileLet: ->
    # Compiles let 
    def compileLet(self):
        self.__output_file.write("<letStatement>\n")
        self.__output_file.write("<keyword> let </keyword>\n")
        self.__tokenizer.advance()
        # Compiles varName
        self.__compileIdentifier()
        if self.__tokenizer.get_token() == "[":
            self.__compileSymbol()
            self.compileExpression()
            self.__compileSymbol()
        self.__compileSymbol()
        self.compileExpression()
        self.__compileSymbol() 
        self.__output_file.write("</letStatement>\n")

    # compileIf: ->
    # Compiles if 
    def compileIf(self):
        self.__output_file.write("<ifStatement>\n")
        self.__output_file.write("<keyword> if </keyword>\n")
        self.__tokenizer.advance()
        self.__compileSymbol()
        self.compileExpression()
        self.__compileSymbol() 
        self.__compileSymbol()
        self.compileStatements()
        self.__compileSymbol() 
        if self.__tokenizer.get_token() == "else":
            self.__output_file.write("<keyword> else </keyword>\n")
            self.__tokenizer.advance()
            self.__compileSymbol() 
            self.compileStatements()
            self.__compileSymbol()
        self.__output_file.write("</ifStatement>\n")

    # compileWhile: ->
    # Compiles while
    def compileWhile(self):
        self.__output_file.write("<whileStatement>\n")
        self.__output_file.write("<keyword> while </keyword>\n")
        self.__tokenizer.advance()
        self.__compileSymbol()
        self.compileExpression()
        self.__compileSymbol() 
        self.__compileSymbol()
        self.compileStatements()
        self.__compileSymbol()
        self.__output_file.write("</whileStatement>\n")

    # compileDo: ->
    # Compiles do
    def compileDo(self):
        self.__output_file.write("<doStatement>\n")
        self.__output_file.write("<keyword> do </keyword>\n")
        self.__tokenizer.advance()
        # Compiles subroutineName, className, or varName
        self.__compileIdentifier()
        self.__subroutineCall()
        self.__compileSymbol()   
        self.__output_file.write("</doStatement>\n")

    # compileReturn: ->
    # Compiles return 
    def compileReturn(self):
        self.__output_file.write("<returnStatement>\n")
        self.__output_file.write("<keyword> return </keyword>\n")
        self.__tokenizer.advance()
        # Check if expression
        if self.__tokenizer.get_token() in ["true", "false", "null", "this", "(", "-", "~"] or self.__tokenizer.tokenType() in ["INT_CONST", "STRING_CONST", "IDENTIFIER"]:
            self.compileExpression()
        self.__compileSymbol()
        self.__output_file.write("</returnStatement>\n")

    # compileExpression: -> 
    # Compiles expression  
    def compileExpression(self):
        self.__output_file.write("<expression>\n")
        self.compileTerm()
        while self.__tokenizer.get_token() in ["+", "-", "*", "/", "&", "|", "<", ">", "="]:
            self.__compileSymbol()
            self.compileTerm()
        self.__output_file.write("</expression>\n")

    # compileTerm: -> 
    # Compiles term 
    def compileTerm(self):
        self.__output_file.write("<term>\n")
        if self.__tokenizer.tokenType() == "INT_CONST":
            self.__output_file.write(f"<integerConstant> {self.__token()} </integerConstant>\n")
            self.__tokenizer.advance()  
        elif self.__tokenizer.tokenType() == "STRING_CONST":
            self.__output_file.write(f"<stringConstant> {self.__token()} </stringConstant>\n")
            self.__tokenizer.advance()   
        elif self.__tokenizer.get_token() in ["true", "false", "null", "this"]:
            self.__output_file.write(f"<keyword> {self.__token()} </keyword>\n")
            self.__tokenizer.advance()   
        elif self.__tokenizer.tokenType() == "IDENTIFIER":
            # Compiles varName, subroutineName, or className 
            self.__compileIdentifier()
            if self.__tokenizer.get_token() == "[":
                self.__compileSymbol()
                self.compileExpression()
                self.__compileSymbol()
            else:
                self.__subroutineCall()
        elif self.__tokenizer.get_token() == "(":
            self.__compileSymbol()
            self.compileExpression()
            self.__compileSymbol() 
        elif self.__tokenizer.get_token() in ["-", "~"]:
            # Compiles unaryOp
            self.__compileSymbol()
            self.compileTerm()
        self.__output_file.write("</term>\n")

    # compileExpressionList: ->
    # Compiles expressionList 
    def compileExpressionList(self):
        self.__output_file.write("<expressionList>\n")
        # Check if expression
        if self.__tokenizer.get_token() in ["true", "false", "null", "this", "(", "-", "~"] or self.__tokenizer.tokenType() in ["INT_CONST", "STRING_CONST", "IDENTIFIER"]:
            self.compileExpression()
            while self.__tokenizer.get_token() == ",":
                self.__compileSymbol()
                self.compileExpression()
        self.__output_file.write("</expressionList>\n")