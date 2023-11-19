from dataclasses import dataclass
from typing import Any


class Node(object):
    def print_indent(self, indent):
        print(indent * "|\t", end="")

@dataclass
class Return(Node):
    expr: Any = None

@dataclass
class Break(Node):
    pass

@dataclass
class Continue(Node):
    pass

@dataclass
class Print(Node):
    printargs: Any

#CZYM JEST INSTRUKCJA ZLOZONA XD

@dataclass
class Transpose(Node):
    val: Any

@dataclass
class Matrix(Node):
    matrix: Any

@dataclass
class MatrixFunc(Node):
    func: Any
    expr: Any

class Error(Node):
    def __init__(self):
        pass