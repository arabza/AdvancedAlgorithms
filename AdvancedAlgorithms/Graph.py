# This code inserts input values into a Binary Search Tree (BST) and prints them in sorted order using in-order traversal
class Node:
    def __init__(self, value):
        self.left = None  
        self.right = None  
        self.value = value  

class BinarySearchTree:
    def __init__(self):
        self.root = None  

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)  
        else:
            self._insert_node(value, self.root)

    def _insert_node(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_node(value, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_node(value, current_node.right)

    def in_order_traversal(self):
        if self.root is not None:
            self._in_order_print(self.root)
        else:
            print("Tree is empty!")

    def _in_order_print(self, node):
        if node is not None:
            self._in_order_print(node.left)
            print(f'{node.value}', end=' ')
            self._in_order_print(node.right)

tree = BinarySearchTree()
elements = [11,6,8,19,4,10,5,17,43,49,31]

for element in elements:
    tree.insert(element)

print("In-order traversal:")
tree.in_order_traversal()
