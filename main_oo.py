#object oriented version
import os

from scanner_oo import Scanner
from parser_oo import CalcParser
from sly.lex import LexError
from tree_printer import TreePrinter
from type_checker import TypeChecker

if __name__ == '__main__':
    file_list = ["./tests/example_incorrect_1.m","./tests/init.txt","./tests/opers.txt"]
    parser = CalcParser()
    for filename in file_list:
        file_path = os.path.join(filename)

        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                file_contents = file.read()
                print(f'Testing {filename}:')
            try:
                TreePrinter()
                parser = CalcParser()
                typeChecker = TypeChecker()
                cos = parser.parse(Scanner().tokenize(file_contents))
                # print(cos)
                if cos is not None:
                    cos.printTree(0)
                    typeChecker.visit(cos)

            except LexError as e:
                print(f"Lexer error: {e}")


