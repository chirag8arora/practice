# AC Rate: 26.4%
# SOURCE URL: https://oj.leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
# Note:

# You may assume that duplicates do not exist in the tree.

#
#


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node

    def buildTree(self, preorder, inorder):
        if not inorder or not preorder:
            return None
        root = TreeNode(preorder[0])
        inorder_root_index = inorder.index(preorder[0])
        left_inorder = inorder[:inorder_root_index]
        left_preorder = preorder[1:1 + inorder_root_index]
        right_inorder, right_preorder = [], []
        if inorder_root_index < len(inorder) - 1:
            right_inorder = inorder[inorder_root_index+1:]
            right_preorder = preorder[inorder_root_index+1:]
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root


#    1
#  2   3
# 4 5 6 7
# preorder 1 2 4 5 3 6 7
# inorder  4 2 5 1 6 3 7

# preorder 1st is the root
