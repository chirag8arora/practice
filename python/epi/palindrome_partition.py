# palindrome decomposition
import unittest


class Solution:
    dp = {}
    def decomposition(self, s):
        self.dp = {}
        return self.helper(s)

    def helper(self, s):
        if len(s) == 0:
            return [[]]
        if len(s) == 1:
            return [[s]]
        if s not in self.dp:
            res = []
            for i in range(1, len(s) + 1):
                if self.is_palindrome(s[:i]):
                    for j in self.helper(s[i:]):
                        res.append([s[:i]] + j)
            self.dp[s] = res
        return self.dp[s]

    def is_palindrome(self, s):
        for i in range(len(s)/2):
            if not s[i] == s[-i-1]:
                return False
        return True


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.decomposition('aab'),
            [['a', 'a', 'b'], ['aa', 'b']])
        self.assertEqual(s.decomposition('aabb'),
                [['a', 'a', 'b', 'b'],['a', 'a', 'bb'],
                 ['aa', 'b', 'b'],
                 ['aa', 'bb'], ])


if __name__ == '__main__':
    unittest.main()
