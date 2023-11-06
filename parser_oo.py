from sly import Parser
from scanner_oo import Scanner
from sly.lex import LexError

def print_error(p, message):
    p = p.error
    print("Syntax error in {0}, at line {1}: LexToken({2}, '{3}')".format(message, p.lineno, p.type, p.value))

class CalcParser(Parser):
    # Get the token list from the lexer (required)
    tokens = Scanner.tokens
    debugfile = 'parser.out'

    precedence = (
        ('right', IFX),
        ('right', ELSE),
        ('nonassoc', GREATEREQUAL, LESSEREQUAL, GREATER, LESSER, NOTEQUAL, EQUAL),
        ('left', AND, OR, XOR),
        ('left', "+", "-", DOTADD, DOTSUB),
        ('left', "*", "/", DOTMUL, DOTDIV),
        ('right', NOT, UMINUS),
    )

    start = 'program'

    @_('instructions_or_empty')
    def program(self, p):
        return p

    @_('instructions')
    def instructions_or_empty(self, p):
        return p

    @_('')
    def instructions_or_empty(self, p):
        return p

    @_('instructions instruction',
       'instruction')
    def instructions(self, p):
        return p

    @_('if_i',
       'return_i ";"',
       'BREAK ";"',
       'CONTINUE ";"',
       'for_l',
       'while_l',
       'assign ";"',
       'print_i ";"',
       '"{" instructions "}"')
    def instruction(self, p):
        return p

    @_('var',
       '"(" expr ")"',
       'INTNUM',
       'FLOATNUM',
       'STRING')
    def expr(self, p):
        return p

    @_('ID',
       'matel')
    def var(self, p):
        return p

    @_('ID "[" expr "," expr "]"')
    def matel(self, p):
        return p

# operatory relacyjne, operacje arytmetyczne i element po elemencie
    @_('expr "+" expr',
       'expr "-" expr',
       'expr "*" expr',
       'expr "/" expr',

       'expr EQUAL expr',
       'expr NOTEQUAL expr',
       'expr GREATER expr',
       'expr LESSER expr',
       'expr GREATEREQUAL expr',
       'expr LESSEREQUAL expr',

       'expr DOTMUL expr',
       'expr DOTDIV expr',
       'expr DOTADD expr',
       'expr DOTSUB expr',

       'expr XOR expr',
       'expr AND expr',
       'expr OR expr'
       )
    def expr(self, p):
        return p

#przypisania
    @_('var "=" expr',
       'var ADDASSIGN expr',
       'var SUBASSIGN expr',
       'var MULASSIGN expr',
       'var DIVASSIGN expr')
    def assign(self, p):
        return p



#negacje
    @_('"-" expr %prec UMINUS',
       'NOT expr %prec NOT',
       '''expr "'"''')
    def expr(self, p):
        return p  # -p.expr

#reprezewntacja macierzy
    @_('matrix')
    def expr(self, p):
        return p

    @_('"[" vectors "]"')
    def matrix(self, p):
        return p

    @_('vectors "," vector',
       'vector')
    def vectors(self, p):
        return p

    @_('"[" variables "]"')
    def vector(self, p):
        return p

    @_('variables "," variable',
       'variable')
    def variables(self, p):
        return p

    @_('expr')
    def variable(self, p):
        return p

# macierzowe funkcje specjalne
    @_('mat_fun "(" expr ")"')
    def expr(self, p):
        return p

    @_('ZEROS',
       'EYE',
       'ONES')
    def mat_fun(self, p):
        return p

# instrukcje wartunkowe
    @_('IF "(" expr ")" instruction %prec IFX',
       'IF "(" expr ")" instruction ELSE instruction')
    def if_i(self, p):
        return p

#pętle
    @_('WHILE "(" expr ")" instruction')
    def while_l(self, p):
        return p

    @_('FOR ID "=" expr ":" expr instruction', )
    def for_l(self, p):
        return p

# break continue i return
    @_('RETURN',
       'RETURN expr')
    def return_i(self, p):
        return p

# print
    @_('PRINT printargs')
    def print_i(self,p):
        return p

    @_('expr "," printargs',
       'expr')
    def printargs(self, p):
        return p

#tablice
    @_('ID "[" expr "]"',
       'ID "[" expr ":" expr "]"',
       'ID "[" ":" expr "]"',
       'ID "[" expr ":" "]"')
    def vector(self,p):
        return p

if __name__ == '__main__':
    scanner = Scanner()
    parser = CalcParser()
    with open("example_3.txt", "r") as infile:
        source_code = infile.read()
        infile.close()

    try:
        parser.parse(scanner.tokenize(source_code))
    except LexError as e:
        print(f"Lexer error: {e}")