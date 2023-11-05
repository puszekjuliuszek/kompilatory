from sly import Parser
from scanner_oo import Scanner

class CalcParser(Parser):
    # Get the token list from the lexer (required)
    tokens = Scanner.tokens
    debugfile = 'parser.out'

    precedence = (
        ('left', AND, OR, XOR),
        ('left', "+", "-"),
        ('left', "*", "/"),
        ('left', DOTADD, DOTSUB),
        ('left', DOTMUL, DOTDIV),
        ('nonassoc', "<=", ">=", "==", "!=", "<", ">"),
        ('right', NOT, "-"),
    )
# operatory relacyjne, operacje arytmetyczne i element po elemencie
    @_('expr "+" expr',
       'expr "-" expr',
       'expr "*" expr',
       'expr "/" expr',

       'expr "==" expr',
       'expr "!=" expr',
       'expr ">" expr',
       'expr "<" expr',
       'expr ">=" expr',
       'expr "<=" expr',

       'expr DOTMUL expr',
       'expr DOTDIV expr',
       'expr DOTADD expr',
       'expr DOTSUB expr',
       )
    def expr(self, p):
        return p

#przypisania
    @_('var "=" expr',
       'var ADDASSIGN expr',
       'var UBASSIGN expr',
       'var MULASSIGN expr',
       'var DIVASSIGN expr')
    def assign(self, p):
        return p

#negacje
    @_('NOT expr',
       '''expr "'"''')
    def expr(self, p):
        return p

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


if __name__ == '__main__':
    lexer = Scanner()
    parser = CalcParser()

    with open("example.txt", "r") as f:
        data = f.read()

    # Give the lexer some input
    # lexer.input(data)
    result = parser.parse(lexer.tokenize(" 12.2 + 432"))
    print(result)