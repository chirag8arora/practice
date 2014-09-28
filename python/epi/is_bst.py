# test binary search tree
class Solution():
    def isValidBST(self, root):
        return self.is_bst(root)[0]

    def is_bst(self, root):
        flag, lmin, rmax = True, root.val, root.val
        if root.left:
            lres = self.is_bst(root.left)
            if not lres[0]:
                return False, lmin, rmax
            elif lres[2] > root.val:
                return False, lmin, rmax
            else:
                lmin = lres[1]
        if root.right:
            rres = self.is_bst(root.right)
            if not rres[0]:
                return False, lmin, rmax
            elif rres[1] < root.val:
                return False, lmin, rmax
            else:
                rmax = rres[2]
        return flag, lmin, rmax
