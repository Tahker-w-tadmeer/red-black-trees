from collections import deque
from helper import Printable, NodeColor


class Node(Printable):
    def __init__(self, key):
        self.color = NodeColor.RED
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.root = None

    def insert(self, key) -> None:
        if self.root is None:
            self.root = Node(key)
            self.root.color = NodeColor.BLACK
            return

        node = Node(key)
        self._insert_at(node, self.root)

        self._fix_insert(node)

    def printRoot(self):
        print(self.root.display())

    @staticmethod
    def _get_uncle(node: Node):
        if node.parent is None:
            return None

        grandparent = node.parent.parent
        if grandparent is None:
            return None

        if grandparent.right == node.parent:
            return grandparent.left
        else:
            return grandparent.right

    @staticmethod
    def _is_black(node: Node) -> bool:
        if node is None:
            return True

        return node.color == NodeColor.BLACK

    def _fix_insert(self, node: Node):
        if node.parent is None:
            node.color = NodeColor.BLACK
            return

        if RBTree._is_black(node.parent):
            return

        uncle = RBTree._get_uncle(node)
        if not RBTree._is_black(uncle):
            node.parent.color = NodeColor.BLACK
            uncle.color = NodeColor.BLACK
            node.parent.parent.color = NodeColor.RED
            self._fix_insert(node.parent.parent)
            return

        parent = node.parent
        grandparent = node.parent.parent
        if parent == grandparent.left and node == parent.left:
            parent.color = NodeColor.BLACK
            grandparent.color = NodeColor.RED
            self.rotate_right(grandparent)
        elif parent == grandparent.left and node == parent.right:
            self.rotate_left(parent)
            node.color = NodeColor.BLACK
            grandparent.color = NodeColor.RED
            self.rotate_right(grandparent)
        elif parent == grandparent.right and node == parent.right:
            parent.color = NodeColor.BLACK
            grandparent.color = NodeColor.RED
            self.rotate_left(grandparent)
        elif parent == grandparent.right and node == parent.left:
            self.rotate_right(parent)
            node.color = NodeColor.BLACK
            grandparent.color = NodeColor.RED
            self.rotate_left(grandparent)

    def _insert_at(self, node, parent: Node) -> Node:
        while True:
            node.parent = parent
            if node.key > parent.key:
                if parent.right is None:
                    parent.right = node
                    return node
                parent = parent.right
            else:
                if parent.left is None:
                    parent.left = node
                    return node
                parent = parent.left

    def search(self, key):
        node = self.root

        while node is not None:
            if node.key == key:
                return node
            elif node.key < key:
                node = node.right
            else:
                node = node.left

        return None

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

    def rotate_left(self, node: Node):
        if node.right is None:
            return

        y = node.right
        node.right = y.left
        if y.left is not None:
            y.left.parent = node

        y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y

    def rotate_right(self, node: Node):
        if node.left is None:
            return

        y = node.left
        node.left = y.right
        if y.right is not None:
            y.right.parent = node

        y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y
        y.right = node
        node.parent = y
