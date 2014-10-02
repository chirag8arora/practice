import unittest


class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        # subproblem maxProduct(A[n-1])
        # optimal substructrure
        # dp is applicable
        m, n = 0, None
        for i in A:
            if i > 0:
                m = max(m, m * i, i)
                if n:
                    n = min(n, n * i)
            else:
                if n:
                    m = max(m, n * i)
                    n = min(n, m * i)
                else:
                    n = i
        return m



class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.maxProduct([0.1, 0.1, 2]), 2)
        self.assertEqual(s.maxProduct([-2, 2, -2]), 8)
        self.assertEqual(s.maxProduct([0, -2, 4]), 4)
        self.assertEqual(s.maxProduct([0, -2, -2, 4]), 16)
        self.assertEqual(s.maxProduct([1, -2, 2, 2, 4]), 16)


if __name__ == '__main__':
    unittest.main()
