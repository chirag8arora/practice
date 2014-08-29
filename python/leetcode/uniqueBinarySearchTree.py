class Solution:
    # @return an integer
    dic = {0: 1, 1: 1, 2: 2}

    def numTrees(self, n):
        if n not in self.dic:
            res = 0
            for i in range(n):
                res += self.numTrees(i) * self.numTrees(n - i - 1)
            self.dic[n] = res
        return self.dic[n]


if __name__ == '__main__':
    s = Solution()
    print s.numTrees(14)
