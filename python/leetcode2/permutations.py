# coding=utf-8
# AC Rate: 31.3%
# SOURCE URL: https://oj.leetcode.com/problems/permutations/
#
#
# Given a collection of numbers, return all possible permutations.
#
#
# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
#
#


class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, start, num):
        stack = [(start, num)]
        while stack:
            start, num = stack.pop()
            for i in range(start, len(num)):
                num[start], num[i] = num[i], num[start]
                stack.append((start + 1, list(num)))
                num[start], num[i] = num[i], num[start]

s = Solution()
print s.permute(0, [1,2,3])
