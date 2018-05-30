import sys


def checkBST(root):
    return checkBSTUtil(root, -sys.maxint - 1, sys.maxint)


def checkBSTUtil(node, left, right):
    if node is None:
        return True
    if node.data <= left or node.data >= right:
        return False
    return checkBSTUtil(node.left, left, node.data) and checkBSTUtil(node.right, node.data, right)
