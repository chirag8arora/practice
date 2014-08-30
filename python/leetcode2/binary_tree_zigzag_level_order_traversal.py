# AC Rate: 26.6%
# SOURCE URL: https://oj.leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
#
# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
#

# For example:

# Given binary tree {3,9,20,#,#,15,7},
#

#     3

#    / \

#   9  20

#     /  \

#    15   7

#
#
#

# return its zigzag level order traversal as:
#

# [

#   [3],

#   [20,9],

#   [15,7]

# ]

#
#
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
# OJ's Binary Tree Serialization:
#

# The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.

#
#

# Here's an example:
#

#    1

#   / \

#  2   3

#     /

#    4

#     \

#      5

#

# The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".

#
#
#


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        res = []
        level = []
        current_level_counter = 1
        next_level_counter = 0
        queue = [root]
        left_to_right = True
        while queue:
            node = queue.pop(0)

            if left_to_right:
                level.append(node.val)
            else:
                level.insert(0, node.val)

            if node.left:
                next_level_counter += 1
                queue.append(node.left)
            if node.right:
                next_level_counter += 1
                queue.append(node.right)

            current_level_counter -= 1
            if current_level_counter == 0:
                left_to_right = not left_to_right
                current_level_counter = next_level_counter
                next_level_counter = 0
                res.append(level)
                level = []
        if level:
            res.append(level)
        return res




if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.left.left = TreeNode(5)
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(7)
    # root.left.left.left = TreeNode(8)
    # root.left.left.right = TreeNode(9)
    s = Solution()
    print s.zigzagLevelOrder(root)

