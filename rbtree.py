from enum import Enum


class NodeColor(Enum):
    RED = 0
    BLACK = 1


class Node:
    def __init__(self, key):
        self.color = NodeColor.RED
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.NULL = Node(-1)
        self.NULL.color = NodeColor.BLACK
        self.root = self.NULL

    def insert(self, key) -> None:
        pass

    def search(self, key) -> Node:
        pass

    def height(self) -> int:
        pass

    def size(self) -> int:
        pass

