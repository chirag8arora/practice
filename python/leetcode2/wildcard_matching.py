# coding=utf-8
# AC Rate: 13.7%
# SOURCE URL: https://oj.leetcode.com/problems/wildcard-matching/
#
# Implement wildcard pattern matching with support for '?' and '*'.
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
#
# The matching should cover the entire input string (not partial).
#
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
#
# Some examples:
# isMatch("aa","a") == False
# isMatch("aa","aa") == True
# isMatch("aaa","aa") == False
# isMatch("aa", "*") == True
# isMatch("aa", "a*") == True
# isMatch("ab", "?*") == True
# isMatch("aab", "c*a*b") == False
#
#


class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isStar(self, p):
        for i in p:
            if i != '*':
                return False
        return True

    def isMatch(self, s, p):
        if p is None or s is None:
            return False
        if not s:
            return (not p)
        if not p:
            return (not s)
        if (p and p[0] == '?') or (s[0] == p[0]):
            return self.isMatch(s[1:], p[1:])
        elif p and p[0] == '*':
            for k in range(len(p)):
                if p[k] != '*':
                    break
            p = p[k:]
            if p == "*":
                return True
            for i in range(len(s)):
                if i >= len(p):
                    return False
                if p[i] == '*':
                    break
                if s[i] == p[i] or p[i] == '?':
                    i += 1
            return self.isMatch(s[i:], p[i:])
        return False

s = Solution()
print s.isMatch("aa","a") == False
print s.isMatch("aa","aa") == True
print s.isMatch("aaa","aa") == False
print s.isMatch("aa", "*") == True
print s.isMatch("aa", "a*") == True
print s.isMatch("ab", "?*") == True
print s.isMatch("aab", "c*a*b") == False
print s.isMatch("aab", "c*a*b") == False
print s.isMatch("", "") == True
print s.isMatch(None, None) == False
print s.isMatch("aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", "a*******b") == False
print s.isMatch("abbaabbbbababaababababbabbbaaaabbbbaaabbbabaabbbbbabbbbabbabbaaabaaaabbbbbbaaabbabbbbababbbaaabbabbabb",
    "***b**a*a*b***b*a*b*bbb**baa*bba**b**bb***b*a*aab*a**") == True
