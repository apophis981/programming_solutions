#!/usr/bin/python


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def printLeftToRight(node, height):
    if height == 1:
        print(node.data)
    else:
        if node.left != None:
            printLeftToRight(node.left, height - 1)
        if node.right != None:
            printLeftToRight(node.right, height - 1)


def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

def printTree(node):
    nheight = height(node)
    for i in range(1, nheight + 1):
        printLeftToRight(node, i)

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.left = Node(6)
tree.right.right = Node(7)

printTree(tree)
