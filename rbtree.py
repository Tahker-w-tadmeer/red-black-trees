from enum import Enum
from collections import deque



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

        self._fix_insert(node)

    @staticmethod
    def _get_uncle(node: Node):
        if node.parent is None:
            return None

        if node.parent.right == node:
            return node.parent.left
        else:
            return node.parent.right

    def _fix_insert(self, node: Node):
        if node.parent==None:
            node.color=NodeColor.BLACK
            return

        if node.parent.color == NodeColor.RED:
            uncle = self._get_uncle(node)
            if uncle.color==NodeColor.RED:
                node.parent.color=NodeColor.BLACK
                uncle.color=NodeColor.BLACK
                node.parent.parent.color=NodeColor.RED
                self._fix_insert(node.parent.parent)



    @staticmethod
    def _insert_at(key, parent: Node) -> Node:
        if parent.key == -1:
            parent.key = key
            return parent

        node = Node(key)

        while True:
            node.parent = parent
            if key > parent.key:
                if parent.right is None:
                    parent.right = node
                    return node
                parent = parent.right
            else:
                if parent.left is None:
                    parent.left = node
                    return node
                parent = parent.left

    def search(self, key) -> Node:
        pass

    def height(self) -> int:
        node = self.root
        if node is None:
            return 0

        queue = deque()
        queue.append(node)
        height = 0

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                current_node = queue.popleft()

                if current_node.left is not None:
                    queue.append(current_node.left)

                if current_node.right is not None:
                    queue.append(current_node.right)

            height += 1

        return height

    def size(self) -> int:
        node = self.root

        if node is None:
            return 0
        stack = [node]
        size = 0
        while stack:
            curr = stack.pop()
            size += 1
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return size



