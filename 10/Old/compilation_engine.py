class CompilationEngine():
    def __init__(self, output_file, tokenizer):
        self.__output_file = output_file 
        self.__tokenizer = tokenizer 

    def compileClass(self):
        # class
        self.__output_file.write("<class>")
        self.__output_file.write("\n")
        self.__tokenizer.advance()
        self.__output_file.write("<keyword> class </keyword>")
        self.__output_file.write("\n")
        self.__tokenizer.advance()
        # class name
        self.__output_file.write(f"<identifier> {self.__tokenizer.get_token()} </identifier>")
        self.__output_file.write("\n")
        self.__tokenizer.advance() 
        self.__output_file.write("<symbol> { </symbol>")
        self.__output_file.write("\n")
        self.__tokenizer.advance()
        #classvardec
        while self.__tokenizer.get_token() in ["static", "field"]:
            self.compileClassVarDec()
        #subroutinedec
        while self.__tokenizer.get_token() in ["constructor", "function", "method"]:
            self.compileSubroutineDec()
        self.__output_file.write("<symbol> } </symbol>")
        self.__output_file.write("\n")
        self.__output_file.write("</class>")
        self.__output_file.write("\n")

    def compileClassVarDec(self):
        self.__output_file.write("<classVarDec>")
        self.__output_file.write("\n")
        # static or field 
        self.__output_file.write(f"<keyword> {self.__tokenizer.get_token()} </keyword>")
        self.__output_file.write("\n")
        self.__tokenizer.advance()
        # type
        self.__output_file.write(f"<{self.__tokenizer.tokenType().lower()}> {self.__tokenizer.get_token()} </{self.__tokenizer.tokenType().lower()}>")
        self.__output_file.write("\n")
        self.__tokenizer.advance()  
        # varName
        self.__output_file.write(f"<identifier> {self.__tokenizer.get_token()} </identifier>")
        self.__output_file.write("\n")
        self.__tokenizer.advance()
        # (',' varName)* 
        while self.__tokenizer.get_token() == ",":
            self.__output_file.write(f"<symbol> , </symbol>")
            self.__output_file.write("\n")
            self.__tokenizer.advance()
            self.__output_file.write(f"<identifier> {self.__tokenizer.get_token()} </identifier>")
            self.__output_file.write("\n")
            self.__tokenizer.advance()
        self.__output_file.write("<symbol> ; </symbol>")
        self.__output_file.write("\n")
        self.__tokenizer.advance()
        self.__output_file.write("</classVarDec>")
        self.__output_file.write("\n")

    def compileSubroutineDec(self):
        self.__output_file.write("<subroutineDec>")
        self.__output_file.write("\n")
        # ('constructor' | 'function' | 'method')
        self.__output_file.write(f"<keyword> {self.__tokenizer.get_token()} </keyword>")
        self.__output_file.write("\n")
        self.__tokenizer.advance()
        # void or type
        self.__output_file.write(f"<{self.__tokenizer.tokenType().lower()}> {self.__tokenizer.get_token()} </{self.__tokenizer.tokenType().lower()}>")
        self.__output_file.write("\n")
        self.__tokenizer.advance()  
        # subroutineName
        self.__output_file.write(f"<identifier> {self.__tokenizer.get_token()} </identifier>")
        self.__output_file.write("\n")
        self.__tokenizer.advance() 
        self.__output_file.write("<symbol> ( </symbol>")
        self.__output_file.write("\n")
        self.__tokenizer.advance()
        self.compileParameterList()
        self.__output_file.write("<symbol> ) </symbol>")
        self.__output_file.write("\n")
        self.__tokenizer.advance() 
        self.compileSubroutineBody()
        self.__output_file.write("</subroutineDec>")
        self.__output_file.write("\n")

    def compileParameterList(self):
        self.__output_file.write("<parameterList>")
        self.__output_file.write("\n")
        # if type 
        if self.__tokenizer.get_token() in ["int", "char", "boolean"] or self.__tokenizer.tokenType() == "IDENTIFIER":
            # type 
            self.__output_file.write(f"<{self.__tokenizer.tokenType().lower()}> {self.__tokenizer.get_token()} </{self.__tokenizer.tokenType().lower()}>")
            self.__output_file.write("\n")
            self.__tokenizer.advance()
            # varName
            self.__output_file.write(f"<identifier> {self.__tokenizer.get_token()} </identifier>")
            self.__output_file.write("\n")
            self.__tokenizer.advance() 
            # (', ' type varName)*) 
            while self.__tokenizer.get_token() == ",":
                self.__output_file.write(f"<symbol> , </symbol>")
                self.__output_file.write("\n")
                self.__tokenizer.advance()
                # type 
                self.__output_file.write(f"<{self.__tokenizer.tokenType().lower()}> {self.__tokenizer.get_token()} </{self.__tokenizer.tokenType().lower()}>")
                self.__output_file.write("\n")
                self.__tokenizer.advance()
                # varName
                self.__output_file.write(f"<identifier> {self.__tokenizer.get_token()} </identifier>")
                self.__output_file.write("\n")
                self.__tokenizer.advance()
        self.__output_file.write("</parameterList>")
        self.__output_file.write("\n")

    def compileSubroutineBody(self):
        self.__output_file.write("<subroutineBody>")
        self.__output_file.write("\n")
        self.__output_file.write("<symbol> { </symbol>")
        self.__output_file.write("\n")
        # varDec
        self.__tokenizer.advance()
        while self.__tokenizer.get_token() == "var":
            self.compileVarDec()
        # statements 
        self.compileStatements()
        self.__output_file.write("<symbol> } </symbol>")
        self.__output_file.write("\n")
        self.__tokenizer.advance()
        self.__output_file.write("</subroutineBody>")
        self.__output_file.write("\n")

    def compileVarDec(self):
        self.__output_file.write("<varDec>")
        self.__output_file.write("\n")
        self.__output_file.write("<keyword> var </keyword>")
        self.__output_file.write("\n")
        self.__tokenizer.advance()
        # type
        self.__output_file.write(f"<{self.__tokenizer.tokenType().lower()}> {self.__tokenizer.get_token()} </{self.__tokenizer.tokenType().lower()}>")
        self.__output_file.write("\n")
        self.__tokenizer.advance() 
        # varName
        self.__output_file.write(f"<identifier> {self.__tokenizer.get_token()} </identifier>")
        self.__output_file.write("\n")
        self.__tokenizer.advance()
        # (',' varName)* 
        while self.__tokenizer.get_token() == ",":
            self.__output_file.write(f"<symbol> , </symbol>")
            self.__output_file.write("\n")
            self.__tokenizer.advance()
            self.__output_file.write(f"<identifier> {self.__tokenizer.get_token()} </identifier>")
            self.__output_file.write("\n")
            self.__tokenizer.advance()
        self.__output_file.write("<symbol> ; </symbol>")
        self.__output_file.write("\n")
        self.__tokenizer.advance()  
        self.__output_file.write("</varDec>")
        self.__output_file.write("\n")

    def compileStatements(self):
        self.__output_file.write("<statements>")
        self.__output_file.write("\n")
        # statements
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
        self.__output_file.write("</statements>")
        self.__output_file.write("\n")

    def compileLet(self):
        self.__output_file.write("<letStatement>")
        self.__output_file.write("\n")
        # let
        self.__output_file.write("<keyword> let </keyword>")
        self.__output_file.write("\n")
        self.__tokenizer.advance()
        # varName
        self.__output_file.write(f"<identifier> {self.__tokenizer.get_token()} </identifier>")
        self.__output_file.write("\n")
        self.__tokenizer.advance()
         # ('[' expression '] )?
        if self.__tokenizer.get_token() == "[":
            self.__output_file.write("<symbol> [ </symbol>")
            self.__output_file.write("\n")
            self.__tokenizer.advance()
            self.compileExpression()
            self.__output_file.write("<symbol> ] </symbol>")
            self.__output_file.write("\n")
            self.__tokenizer.advance()
        self.__output_file.write("<symbol> = </symbol>")
        self.__output_file.write("\n")
        self.__tokenizer.advance()
        self.compileExpression()
        self.__output_file.write("<symbol> ; </symbol>")
        self.__output_file.write("\n")
        self.__tokenizer.advance()  
        self.__output_file.write("</letStatement>")
        self.__output_file.write("\n")

    def compileIf(self):
        self.__output_file.write("<ifStatement>")
        self.__output_file.write("\n")
        # if
        self.__output_file.write("<keyword> if </keyword>")
        self.__output_file.write("\n")
        self.__tokenizer.advance()
        # expression 
        self.__output_file.write("<symbol> ( </symbol>")
        self.__output_file.write("\n")
        self.__tokenizer.advance() 
        self.compileExpression()
        self.__output_file.write("<symbol> ) </symbol>")
        self.__output_file.write("\n")
        self.__tokenizer.advance()  
        # statements 
        self.__output_file.write("<symbol> { </symbol>")
        self.__output_file.write("\n")
        self.__tokenizer.advance() 
        self.compileStatements()
        self.__output_file.write("<symbol> } </symbol>")
        self.__output_file.write("\n")
        self.__tokenizer.advance() 
        # ('else' '{' statements '}')?
        if self.__tokenizer.get_token() == "else":
            # else 
            self.__output_file.write("<keyword> else </keyword>")
            self.__output_file.write("\n")
            self.__tokenizer.advance()
            # statements 
            self.__output_file.write("<symbol> { </symbol>")
            self.__output_file.write("\n")
            self.__tokenizer.advance() 
            self.compileStatements()
            self.__output_file.write("<symbol> } </symbol>")
            self.__output_file.write("\n")
            self.__tokenizer.advance() 
        self.__output_file.write("</ifStatement>")
        self.__output_file.write("\n")

    def compileWhile(self):
        self.__output_file.write("<whileStatement>")
        self.__output_file.write("\n")
        # while
        self.__output_file.write("<keyword> while </keyword>")
        self.__output_file.write("\n")
        self.__tokenizer.advance()
        # expression 
        self.__output_file.write("<symbol> ( </symbol>")
        self.__output_file.write("\n")
        self.__tokenizer.advance() 
        self.compileExpression()
        self.__output_file.write("<symbol> ) </symbol>")
        self.__output_file.write("\n")
        self.__tokenizer.advance()  
        # statements 
        self.__output_file.write("<symbol> { </symbol>")
        self.__output_file.write("\n")
        self.__tokenizer.advance() 
        self.compileStatements()
        self.__output_file.write("<symbol> } </symbol>")
        self.__output_file.write("\n")
        self.__tokenizer.advance() 
        self.__output_file.write("</whileStatement>")
        self.__output_file.write("\n")

    def compileDo(self):
        self.__output_file.write("<doStatement>")
        self.__output_file.write("\n")
        # do
        self.__output_file.write("<keyword> do </keyword>")
        self.__output_file.write("\n")
        self.__tokenizer.advance()
        # subroutineCall
        # subroutineName or className or varName
        self.__output_file.write(f"<identifier> {self.__tokenizer.get_token()} </identifier>")
        self.__output_file.write("\n")
        self.__tokenizer.advance()
        if self.__tokenizer.get_token() == '(':
            # expressionList
            self.__output_file.write("<symbol> ( </symbol>")
            self.__output_file.write("\n")
            self.__tokenizer.advance() 
            self.compileExpressionList()
            self.__output_file.write("<symbol> ) </symbol>")
            self.__output_file.write("\n")
            self.__tokenizer.advance()   
        elif self.__tokenizer.get_token() == '.':
            self.__output_file.write("<symbol> . </symbol>")
            self.__output_file.write("\n")
            self.__tokenizer.advance()  
            # subroutineName
            self.__output_file.write(f"<identifier> {self.__tokenizer.get_token()} </identifier>")
            self.__output_file.write("\n")
            self.__tokenizer.advance()
            # expressionList
            self.__output_file.write("<symbol> ( </symbol>")
            self.__output_file.write("\n")
            self.__tokenizer.advance() 
            self.compileExpressionList()
            self.__output_file.write("<symbol> ) </symbol>")
            self.__output_file.write("\n")
            self.__tokenizer.advance()  
        self.__output_file.write("<symbol> ; </symbol>")
        self.__output_file.write("\n")
        self.__tokenizer.advance()   
        self.__output_file.write("</doStatement>")
        self.__output_file.write("\n")

    def compileReturn(self):
        self.__output_file.write("<returnStatement>")
        self.__output_file.write("\n")
        # return
        self.__output_file.write("<keyword> return </keyword>")
        self.__output_file.write("\n")
        self.__tokenizer.advance()
        # expression?
        if self.__tokenizer.get_token() in ["true", "false", "null", "this", "(", "-", "~"] or self.__tokenizer.tokenType() in ["INT_CONST", "STRING_CONST", "IDENTIFIER"]:
            self.compileExpression()
        self.__output_file.write("<symbol> ; </symbol>")
        self.__output_file.write("\n")
        self.__tokenizer.advance()  
        self.__output_file.write("</returnStatement>")
        self.__output_file.write("\n")

    def compileExpression(self):
        self.__output_file.write("<expression>")
        self.__output_file.write("\n")
        self.compileTerm()
        while self.__tokenizer.get_token() in ["+", "-", "*", "/", "&", "|", "<", ">", "="]:
            self.__output_file.write(f"<symbol> {self.__tokenizer.get_token()} </symbol>")
            self.__output_file.write("\n")
            self.__tokenizer.advance()
            self.compileTerm()
        self.__output_file.write("</expression>")
        self.__output_file.write("\n")

    def compileTerm(self):
        self.__output_file.write("<term>")
        self.__output_file.write("\n")
        if self.__tokenizer.tokenType() == "INT_CONST":
            self.__output_file.write(f"<integerConstant> {self.__tokenizer.get_token()} </integerConstant>")
            self.__output_file.write("\n")
            self.__tokenizer.advance()  
        elif self.__tokenizer.tokenType() == "STRING_CONST":
            self.__output_file.write(f"<stringConstant> {self.__tokenizer.get_token()} </stringConstant>")
            self.__output_file.write("\n")
            self.__tokenizer.advance()   
        elif self.__tokenizer.get_token() in ["true", "false", "null", "this"]:
            self.__output_file.write(f"<keyword> {self.__tokenizer.get_token()} </keyword>")
            self.__output_file.write("\n")
            self.__tokenizer.advance()   
        elif self.__tokenizer.tokenType() == "IDENTIFIER":
            # varName or subroutineName or className 
            self.__output_file.write(f"<identifier> {self.__tokenizer.get_token()} </identifier>")
            self.__output_file.write("\n")
            self.__tokenizer.advance()
            # varName 
            if self.__tokenizer.get_token() == "[":
                # expression 
                self.__output_file.write("<symbol> [ </symbol>")
                self.__output_file.write("\n")
                self.__tokenizer.advance() 
                self.compileExpression()
                self.__output_file.write("<symbol> ] </symbol>")
                self.__output_file.write("\n")
                self.__tokenizer.advance() 
            # subroutineCall
            elif self.__tokenizer.get_token() == '(':
                # expressionList
                self.__output_file.write("<symbol> ( </symbol>")
                self.__output_file.write("\n")
                self.__tokenizer.advance() 
                self.compileExpressionList()
                self.__output_file.write("<symbol> ) </symbol>")
                self.__output_file.write("\n")
                self.__tokenizer.advance()   
            elif self.__tokenizer.get_token() == '.':
                self.__output_file.write("<symbol> . </symbol>")
                self.__output_file.write("\n")
                self.__tokenizer.advance()  
                # subroutineName
                self.__output_file.write(f"<identifier> {self.__tokenizer.get_token()} </identifier>")
                self.__output_file.write("\n")
                self.__tokenizer.advance()
                # expressionList
                self.__output_file.write("<symbol> ( </symbol>")
                self.__output_file.write("\n")
                self.__tokenizer.advance() 
                self.compileExpressionList()
                self.__output_file.write("<symbol> ) </symbol>")
                self.__output_file.write("\n")
                self.__tokenizer.advance()   
        elif self.__tokenizer.get_token() == "(":
            # expression 
            self.__output_file.write("<symbol> ( </symbol>")
            self.__output_file.write("\n")
            self.__tokenizer.advance() 
            self.compileExpression()
            self.__output_file.write("<symbol> ) </symbol>")
            self.__output_file.write("\n")
            self.__tokenizer.advance()   
        elif self.__tokenizer.get_token() in ["-", "~"]:
            # unaryOp
            self.__output_file.write(f"<symbol> {self.__tokenizer.get_token()} </symbol>")
            self.__output_file.write("\n")
            self.__tokenizer.advance() 
            self.compileTerm()
        self.__output_file.write("</term>")
        self.__output_file.write("\n")

    def compileExpressionList(self):
        self.__output_file.write("<expressionList>")
        self.__output_file.write("\n")
        # (expression (',' expression)* )?
        # expression?
        if self.__tokenizer.get_token() in ["true", "false", "null", "this", "(", "-", "~"] or self.__tokenizer.tokenType() in ["INT_CONST", "STRING_CONST", "IDENTIFIER"]:
            self.compileExpression()
            while self.__tokenizer.get_token() == ",":
                self.__output_file.write(f"<symbol> , </symbol>")
                self.__output_file.write("\n")
                self.__tokenizer.advance()
                self.compileExpression()
        self.__output_file.write("</expressionList>")
        self.__output_file.write("\n")