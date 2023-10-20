from sly import Lexer

class Scanner(Lexer):
    # Set of token names.   This is always required
    tokens = {ADD, SUB, MUL, DIV,
              DOTADD, DOTSUB, DOTMUL, DOTDIV,
              ASSIGN, ADDASSIGN, SUBASSIGN, MULASSIGN, DIVASSIGN,
              GREATER, LESSER, GEATEREQUAL, LESSEREQUAL, NOTEQUAL, EQUAL,
              BRACKETOPEN, BRACKETCLOSE, SQUAREBRACKETOPEN, SQUAREBRACKETCLOSE, CURLYBRACKETOPEN, CURLYBRACKETCLOSE,
              COLON,
              APOSTROPHE,
              COMMA, SEMICOLON}

    # String containing ignored characters between tokens
    ignore = ' \t'

    # Regular expression rules for tokens
    ADD = r'\+'
    SUB = r'-'
    MUL = r'\*'
    DIV = r'/'
    EQUAL = r'=='
    DOTADD = r'\.\+'
    DOTSUB = r'\.-'
    DOTMUL = r'\.\*'
    DOTDIV = r'\./'
    ASSIGN = r'='
    ADDASSIGN = r'\+='
    SUBASSIGN = r'-='
    MULASSIGN = r'\*='
    DIVASSIGN = r'/='
    GREATER = r'>'
    LESSER = r'<'
    GEATEREQUAL = r'>='
    LESSEREQUAL = r'<='
    NOTEQUAL = r'!='
    BRACKETOPEN = r'\('
    BRACKETCLOSE = r'\)'
    SQUAREBRACKETOPEN = r'\['
    SQUAREBRACKETCLOSE = r'\]'
    CURLYBRACKETOPEN = r'\{'
    CURLYBRACKETCLOSE = r'\}'
    COLON = r':'
    APOSTROPHE = r'\''
    COMMA = r','
    SEMICOLON = r';'

    ignore_comment = r'\#.*'

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        # exit(1)
        self.index += 1


if __name__ == '__main__':

    with open("example.txt", "r") as f:
        data = f.read()

    lexer = Scanner()
    tokenized = lexer.tokenize((data))
    for tok in tokenized:
        print(f"({tok.lineno}): {tok.type}({tok.value})")