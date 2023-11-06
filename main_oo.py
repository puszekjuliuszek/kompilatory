#object oriented version
from scanner_oo import Scanner
from parser_oo import CalcParser
from sly.lex import LexError

if __name__ == '__main__':
    scanner = Scanner()
    parser = CalcParser()
    with open("example.txt", "r") as infile:
        source_code = infile.read()
        infile.close()

    try:
        parser.parse(Scanner().tokenize(source_code))
    except LexError as e:
        print(f"Lexer error: {e}")


