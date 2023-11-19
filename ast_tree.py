from dataclasses import dataclass
from typing import Any


class Node(object):
    def print_indent(self, indent):
        print(indent * "|\t", end="")