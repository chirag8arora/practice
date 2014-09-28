import unittest

class Solution():
    def is_palindrome(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if self.is_char(s[i]) == -1:
                i += 1
            elif self.is_char(s[j]) == -1:
                j -= 1
            elif self.is_char(s[i]) != self.is_char(s[j]):
                return False
            else:
                i += 1
                j -= 1
        return True


    def is_char(self, c):
        to_a = ord(c) - ord('a')
        to_A = ord(c) - ord('A')
        if to_a >= 0 and to_a <=25:
            return to_a
        if to_A >= 0 and to_A <= 25:
            return to_A
        return -1

class Test(unittest.TestCase):
    s = Solution()

    def test_true(self):
        tcases = ['A man, a plan, a canal, Panama', 'ABA', 'CC', '', '&*(&*(&*(a#^&!c&*(&*(a@*&(!&(&$*@^&#*(@)))']
        for i in tcases:
            self.assertEqual(self.s.is_palindrome(i),
                             True, i)

    def test_false(self):
        tcases = ['Ray a Ray', '&*(&*(&*(ac@*&(!&(&$*@^&#*(@)))']
        for i in tcases:
            self.assertEqual(self.s.is_palindrome(i),
                             False, i)

if __name__ == '__main__':
    unittest.main()
