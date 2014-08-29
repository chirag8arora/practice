# Definition for a  binary tree node
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        res = str(self.val)
        if self.left:
            res += str(self.left)
        if self.right:
            res += str(self.right)
        return res

class Solution:
    unique_trees = {0:[TreeNode(None)], 1:[TreeNode(1)]}

    def copyTreeAndPlus(self, root, x):
        if not root.val:
            return root

        new = TreeNode(root.val + x)
        if root.left:
            new.left = self.copyTreeAndPlus(root.left, x)
        if root.right:
            new.right = self.copyTreeAndPlus(root.right, x)
        return new

    def generateTrees(self, n):
        # base
        if n in self.unique_trees:
            return self.unique_trees[n]
        self.unique_trees[n] = []
        for i in range(n):
            for l in self.generateTrees(i):
                for r in self.generateTrees(n-i-1):
                    new = TreeNode(i + 1)
                    new.left = l
                    new.right = self.copyTreeAndPlus(r, i+1)
                    self.unique_trees[n].append(new)
        return self.unique_trees[n]


def main():
    s = Solution()
    s.generateTrees(10)
    # for i in s.generateTrees(12):
    #     print i

if __name__ == '__main__':
    main()
