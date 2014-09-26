class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        best = A[0]
        positive = max(A[0], 1)
        negtive = min(A[0], 0)
        for i in A[1:]:
            p, n = positive, negtive
            if i > 0:
                best = max(best, p * i)
                positive = max(i, p * i, 1)
                negtive = n * i
            else:
                best = max(best, n * i)
                positive = max(n * i, 1)
                negtive = min(i, p * i)
        return best


s = Solution()
print s.maxProduct([-2, 2, -2])
print s.maxProduct([0, -2, 4])
print s.maxProduct([0, -2, -2, 4])
print s.maxProduct([1, -2, 2, 2, 4])
