class Solution():
    def helper(self, A, k, current):
        if k == 0:
            return [current]

        res = []
        for i in range(len(A)):
            res += self.helper(A[i+1:],
                          k - 1, current + [A[i]])
        return res

    def subset(self, n, k):
        A = range(1, n + 1)
        return self.helper(A, k, [])


s = Solution()
print s.subset(5, 3)
