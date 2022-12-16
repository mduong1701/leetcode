class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def preorder(root):
    result = []
    if root:
        helper(root, result)
    return result

def helper(root, result):
    if root.children == None:
        result.append(root.val)

    result.append(root.val)
    for child in root.children:
        helper(child, result)

        