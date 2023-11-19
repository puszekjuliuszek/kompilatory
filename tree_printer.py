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