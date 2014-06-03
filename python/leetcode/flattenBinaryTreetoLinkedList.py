"""
Make sure left is None
"""

# Definition for a  binary tree node

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return nothing, do it in place

    def helper(self, root):
        leaf = root
        tmp_right = root.right
        if root.left:
            root.right = root.left
            root.left = None
            leaf = self.helper(root.right)
        leaf.right = tmp_right
        if leaf.right:
            return self.helper(leaf.right)
        else:
            return leaf

    def flatten(self, root):
            self.helper(root)


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)

    t1.left = t2
    t2.left = t3
    t2.right = t4
    t1.right = t5
    t5.right = t6

    s = Solution()
    s.flatten(t1)
    r = t1
    while r.right:
        print r.right.val
        r = r.right
