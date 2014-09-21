# coding=utf-8
# AC Rate: 19.5%
# SOURCE URL: https://oj.leetcode.com/problems/longest-valid-parentheses/
#
# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
#
#
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
#
#
# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
#
#


class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        openn, close, best, current = 0, 0, 0, 0
        for i in s:
            if i == '(':
                openn += 1
            elif i == ')':
                close += 1
            if openn == close:
                current = close
                best = max(best, current)
            elif openn > close:
                pass
            else:
                current = 0
                openn = 0
                close = 0
        # l = best
        #
        # openn, close, best, current = 0, 0, 0, 0
        # for i in s[::-1]:
        #     if i == '(':
        #         close += 1
        #     elif i == ')':
        #         openn += 1
        #     if openn >= close:
        #         current = close
        #         best = max(best, current)
        #     else:
        #         current = 0
        #         openn = 0
        #         close = 0
        return best * 2

s = Solution()
print s.longestValidParentheses('))))())()()(()')
print s.longestValidParentheses('()(()')
print s.longestValidParentheses('(()')
print s.longestValidParentheses('(()()')
print s.longestValidParentheses('()()()()()()()()()()(((()(()()())))))')
