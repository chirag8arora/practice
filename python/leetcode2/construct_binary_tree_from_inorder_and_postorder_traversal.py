# AC Rate: 26.4%
# SOURCE URL: https://oj.leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
#
# Given inorder and postorder traversal of a tree, construct the binary tree.
# Note:

# You may assume that duplicates do not exist in the tree.

#
#


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node

    def buildTree(self, inorder, postorder):
        # last post order is the root
        if not inorder or not postorder:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])

        root = TreeNode(postorder[-1])
        inorder_root_index = inorder.index(postorder[-1])
        left_inorder = inorder[:inorder_root_index]
        left_postorder = postorder[:inorder_root_index]
        right_inorder, right_postorder = [], []
        if inorder_root_index < len(inorder) - 1:
            right_inorder = inorder[inorder_root_index + 1:]
            right_postorder = postorder[inorder_root_index: -2]
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        return root



# postorder[-1] = 2
# iri = 1
# l_i = [1,2][:1] = [1]
# r_i = []
# l_p = [2,1][:1] = [2]

#     1
#   2    3
# 4  5  6  7
# inorder 4 2 5 1 6 3 7
# postorder 4 5 2 6 7 3 1
