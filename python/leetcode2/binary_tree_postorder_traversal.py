# AC Rate: 31.0%
# SOURCE URL: https://oj.leetcode.com/problems/binary-tree-postorder-traversal/
# 
# Given a binary tree, return the postorder traversal of its nodes' values.
# 

# For example:

# Given binary tree {1,#,2,3},
# 

#    1

#     \

#      2

#     /

#    3

# 
# 
# 

# return [3,2,1].

# 
# Note: Recursive solution is trivial, could you do it iteratively?
# 


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):

        def helper(root):
            if root:
                if root.left:
                    for i in helper(root.left):
                        yield i
                if root.right:
                    for i in helper(root.right):
                        yield i
                yield root

        return [i.val for i in helper(root)]
