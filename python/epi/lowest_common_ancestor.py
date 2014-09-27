class LCA():
    def get_depth(self, node):
        d = 0
        while node.parent:
            d += 1
            node = node.parent
        return d

    def get_lca(self, n1, n2):
        n1_depth = self.get_depth(n1)
        n2_depth = self.get_depth(n2)
        if n1_depth > n2_depth:
            for i in range(n1_depth - n2_depth):
                n1 = n1.parent
        else:
            for i in range(n2_depth - n1_depth):
                n2 = n2.parent


        while n1.parent and n2.parent:
            if n1 == n2:
                return n1
            else:
                n1 = n1.prent
                n2 = n2.parent
        return None
