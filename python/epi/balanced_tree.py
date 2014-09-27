class Solution():
    def depth(self, root):
        if not root:
            return 0
        rd = self.depth(root.right)
        ld = self.depth(root.left)
        if ld < 0 or rd < 0 or abs(ld - rd) > 1:
            return -1
        else:
            return max(ld, rd) + 1

    def is_balance(self, root):
        return self.depth(root) >= 0

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

s = Solution()
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t1.left = t2
t1.left.left = t3
t1.right = t4
print s.is_balance(t1) == True
