#!/usr/bin/python


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Inorder (Left, Root, Right)
def left_node_right(node):
    if node:
        left_node_right(node.left)
        print(node.data)
        left_node_right(node.right)

# Preorder (Root, Left, Right)
def node_left_right(node):
    if node:
        print(node.data)
        node_left_right(node.left)
        node_left_right(node.right)

# Postorder (Left, Right, Root)
def left_right_node(node):
    if node:
        left_right_node(node.left)
        left_right_node(node.right)
        print(node.data)

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)

print("Inorder (Left, Root, Right)")
left_node_right(tree)
print("Preorder (Root, Left, Right)")
node_left_right(tree)
print("Postorder (Left, Right, Root)")
left_right_node(tree)
