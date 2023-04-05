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
        self.root = Node(-1)
        self.root.color = NodeColor.BLACK

    def insert(self, key) -> None:
        node = self._insert_at(key, self.root)

    def _insert_at(self, key, parent: Node) -> Node:
        if key > parent.key:
            if parent.right is not None:
                return self._insert_at(key, parent.right)
            node = Node(key)
            node.parent = parent
            parent.right = node
        else:
            if parent.left is not None:
                return self._insert_at(key, parent.left)
            node = Node(key)
            node.parent = parent
            parent.left = node

        return node

    def search(self, key) -> Node:
        pass

    def height(self) -> int:
        pass

    def size(self) -> int:
        pass

