from sly import Lexer


class Scanner(Lexer):
    # Set of token names.   This is always required
    tokens = {DOTADD, DOTSUB, DOTMUL, DOTDIV,
                ADDASSIGN, SUBASSIGN, MULASSIGN, DIVASSIGN,
              AND, OR, XOR, NOT,
              ID,
              IF, ELSE,
              WHILE, FOR,
              BREAK, CONTINUE,
              RETURN,
              EYE, ZEROS, ONES,
              PRINT,
              FLOATNUM, INTNUM, STRING,
              GREATER, LESSER, GREATEREQUAL, LESSEREQUAL, NOTEQUAL, EQUAL}

    # String containing ignored characters between tokens
    ignore = ' \t'
    ignore_comment = r'\#.*'
    literals = {'+', '-', '*', '/', '=','(', ')','[',']','{','}', ',', ';', '\'', ':'}

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    # Regular expression rules for tokens
    DOTADD = r'\.\+'
    DOTSUB = r'\.-'
    DOTMUL = r'\.\*'
    DOTDIV = r'\./'
    ADDASSIGN = r'\+='
    SUBASSIGN = r'-='
    MULASSIGN = r'\*='
    DIVASSIGN = r'/='
    GREATEREQUAL = '>='
    LESSEREQUAL = '<='
    GREATER = '>'
    LESSER = '<'
    NOTEQUAL = '!='
    EQUAL = '=='


    # Base ID rule
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

    # Special cases
    ID['if'] = IF
    ID['else'] = ELSE
    ID['while'] = WHILE
    ID['for'] = FOR
    ID['break'] = BREAK
    ID['continue'] = CONTINUE
    ID['return'] = RETURN
    ID['eye'] = EYE
    ID['zeros'] = ZEROS
    ID['ones'] = ONES
    ID['print'] = PRINT
    ID['and'] = AND
    ID['or'] = OR
    ID['xor'] = XOR
    ID['not'] = NOT

    @_(r'[a-zA-Z_][a-zA-Z0-9_]*')
    def ID(self, t):
        t.value = str(t.value)
        return t

    @_(r'\d*\.\d+(E[-+]?\d+)?|\d+\.\d*(E[-+]?\d+)?')
    def FLOATNUM(self, t):
        t.value = float(t.value)
        return t

    @_(r'\d+')
    def INTNUM(self, t):
        t.value = int(t.value)
        return t

    @_(r'\"(\\.|[^\"])*\"')
    def STRING(self, t):
        t.value = str(t.value)
        t.value = t.value[1:-1].replace('\\"', '"')
        return t

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1

    def input(self, data):
        tokenized = self.tokenize((data))
        for tok in tokenized:
            print(f"({tok.lineno}): {tok.type}({tok.value})")