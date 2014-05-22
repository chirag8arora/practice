from math import floor, log


class TreeNode():

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bst(listA):
    length = len(listA)
    if length == 0:  # base case None
        return None
    height = int(floor(log(len(listA), 2))) + 1  # get height
    if len(listA) >= 3 * 2 ** (height - 2) - 1:  # check node number
        mid = 2 ** (height - 1) - 1  # left can be full
    else:
        mid = -2 ** (height - 2)  # right should be full
    root = TreeNode(listA[mid])  # root node
    root.left = bst(listA[:mid])  # recursion
    root.right = bst(listA[mid + 1:])  # recursion
    return root

if __name__ == '__main__':
    for i in range(10):

        root = bst(range(1, i + 1))
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                queue.append(node.left)
                queue.append(node.right)
                print node.val,
        print ''
