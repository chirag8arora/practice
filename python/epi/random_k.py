import random

class Solution():

    def randomK(self, A, k):
        n = len(A) - 1
        flag = False
        if k > n/2:
            flag = True
            k = n - k + 1
        while k:
            i = random.randint(1, n)
            A[i], A[n] = A[n], A[i]
            n -= 1
            k -= 1
        return A[:n+1] if flag else A[n+1:]

s = Solution()
print s.randomK([1,2,3,4,5,6,7], 5)
