import unittest

class Solution():
    def reverseHelper(self, s, start, end):
        while end > start:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    def reverse(self, s):
        s = list(s)
        self.reverseHelper(s, 0, len(s)-1)
        last_space = 0
        for k,v in enumerate(s):
            if v == ' ':
                self.reverseHelper(s, last_space, k-1)
                last_space = k + 1
        self.reverseHelper(s, last_space, len(s) -1)

        return ''.join(s)

class Test(unittest.TestCase):

    def test(self):
        s = Solution()

        self.assertEqual(
            s.reverse('Hello world'), 'world Hello')
        self.assertEqual(
            s.reverse('I love you'), 'you love I')

if __name__ == '__main__':
    unittest.main()
