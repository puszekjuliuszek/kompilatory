import os

from sly.lex import LexError

from scanner_oo import Scanner
from parser_oo import CalcParser
import ast_tree

def addToClass(cls):

    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator

class TreePrinter:

    @addToClass(ast_tree.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(ast_tree.Return)
    def printTree(self, indent):
        self.print_indent(indent)
        print("RETURN")
        if self.expr is not None:
            self.expr.printTree(indent+1)

    @addToClass(ast_tree.Break)
    def printTree(self, i):
        self.print_indent(i)
        print("BREAK")

    @addToClass(ast_tree.Continue)
    def printTree(self, i):
        self.print_indent(i)
        print("CONTINUE")

    @addToClass(ast_tree.Print)
    def printTree(self, i):
        self.print_indent(i)
        print("PRINT")
        for printarg in self.printargs:
            printarg.printTree(i+1)

    @addToClass(ast_tree.Transpose)
    def printTree(self, i):
        self.print_indent(i)
        print("TRANSPOSE")
        self.val.printTree(i + 1)

    @addToClass(ast_tree.Matrix)
    def printTree(self, i):
        self.print_indent(i)
        print("VECTOR")
        for row in self.matrix:
            self.print_indent(i + 1)
            print("VECTOR")
            for expr in row:
                expr.printTree(i+2)

    @addToClass(ast_tree.MatrixFunc)
    def printTree(self, i):
        self.print_indent(i)
        print(self.func)
        self.expr.printTree(i+1)

    @addToClass(ast_tree.InstrOrEmpty)
    def printTree(self, indent=0):
        self.instructions.printTree(indent)

    # @addToClass(AST.Instructions)
    # def printTree(self,i):

    @addToClass(ast_tree.Instructions)
    def printTree(self, indent=0):
        for instruction in self.instructions:
            # print(instruction)
            # print(self.instructions)
            # print(instruction)
            # print(instruction, type(instruction))
            instruction.printTree(indent)

    @addToClass(ast_tree.If)
    def printTree(self, indent):
        self.print_indent(indent)
        print("IF")
        self.cond.printTree(indent + 1)
        self.print_indent(indent)
        print("THEN")
        # for x in self.if_body:
        #     x.printTree(indent+1)
        self.if_body.printTree(indent + 1)
        if self.else_body is not None:
            self.print_indent(indent)
            print("ELSE")
            # for x in self.else_body:
            #     x.printTree(indent+1)
            self.else_body.printTree(indent + 1)

    @addToClass(ast_tree.While)
    def printTree(self, i):
        self.print_indent(i)
        print("WHILE")
        self.cond.printTree(i + 1)
        self.body.printTree(i + 1)

    @addToClass(ast_tree.AssignOp)
    def printTree(self, i):
        self.print_indent(i)
        print(self.op)
        self.left.printTree(i + 1)
        self.right.printTree(i + 1)

    @addToClass(ast_tree.String)
    def printTree(self, i):
        self.print_indent(i)
        print("STRING")
        self.print_indent(i + 1)
        print(self.string)

    @addToClass(ast_tree.IntNum)
    def printTree(self, i):
        # self.print_indent(i)
        # print("INTNUM")
        # self.print_indent(i+1)s
        self.print_indent(i)
        print(self.intnum)

    @addToClass(ast_tree.FloatNum)
    def printTree(self, i):
        self.print_indent(i)
        print("FLOATNUM")
        self.print_indent(i + 1)
        print(self.floatnum)

    @addToClass(ast_tree.Variable)
    def printTree(self, i):

        if self.index is not None:
            self.print_indent(i)
            print("REF")
            self.id.printTree(i + 1)

            for e in self.index:
                # self.print_indent(i+2)
                e.printTree(i + 1)

    @addToClass(ast_tree.Id)
    def printTree(self, i):
        self.print_indent(i)
        print(self.id)

    @addToClass(ast_tree.BinExpr)
    def printTree(self, i):
        self.print_indent(i)
        print(self.op)
        self.left.printTree(i + 1)
        self.right.printTree(i + 1)

    @addToClass(ast_tree.Uminus)
    def printTree(self, i):
        self.print_indent(i)
        print("-")
        self.val.printTree(i + 1)

    @addToClass(ast_tree.Uneg)
    def printTree(self, i):
        self.print_indent(i)
        print("NOT")
        self.val.printTree(i + 1)

    @addToClass(ast_tree.Unary)
    def printTree(self, i):
        self.print_indent(i)
        print(self.operation)
        self.expr.printTree(i + 1)

if __name__ == "__main__":
    file_list = ["example_1.txt"]
    parser = CalcParser()
    for filename in file_list:
        # if filename != "test_5.txt": continue
        file_path = os.path.join(filename)

        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                file_contents = file.read()
                print(f'Testing {filename}:')
            try:
                cos = parser.parse(Scanner().tokenize(file_contents))
                if cos is not None:
                    cos.printTree(0)

            except LexError as e:
                print(f"Lexer error: {e}")