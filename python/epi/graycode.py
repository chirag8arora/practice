# gray code
class Solution():

    def graycode(self, n):
        node = [0] * n
        visited = [0]
        return self.dfshelper(node, visited)

    def dfshelper(self, node, visited):
        if len(visited) == 2 ** len(node):
            return visited

        for i in range(len(node)):
            self.flip(node, i)
            nn = self.numberfy(node)
            if nn not in visited:
                visited.append(nn)
                res = self.dfshelper(node, visited)
                if res:
                    return res
                visited.pop()
            self.flip(node, i)

    def numberfy(self, i):
        r = 0
        for j in i:
            r = r * 2 + j
        return r

    def flip(self, node, i):
        node[i] = 1 if node[i] == 0 else 0

s = Solution()
print s.graycode(3)
