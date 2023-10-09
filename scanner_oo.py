from sly import Lexer

class Scanner(Lexer):
    # Set of token names.   This is always required
    tokens = {ADD, SUB, MUL, DIV,
              DOTADD, DOTSUB, DOTMUL, DOTDIV,
              ASSIGN, ADDASSIGN, SUBASSIGN, MULASSIGN, DIVASSIGN,
              GREATER, LESSER, GEATEREQUAL, LESSEREQUAL, NOTEQUAL, EQUAL,
              BRACKETOPEN, BRACKETCLOSE, SQBRACKETOPEN, SQBRACKETCLOSE, MSTBRACKETOPEN, MSTBRACKETCLOSE,
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
    SQBRACKETOPEN = r'\['
    SQBRACKETCLOSE = r'\]'
    MSTBRACKETOPEN = r'\{'
    MSTBRACKETCLOSE = r'\}'
    COLON = r':'
    APOSTROPHE = r'\''
    COMMA = r','
    SEMICOLON = r';'

if __name__ == '__main__':
    data = '.+  + ++ -'
    lexer = Scanner()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))