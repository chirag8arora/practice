import unittest


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
