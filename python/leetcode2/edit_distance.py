# coding=utf-8
# AC Rate: 25.2%
# SOURCE URL: https://oj.leetcode.com/problems/edit-distance/
#
#
# Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)
#
#
# You have the following 3 operations permitted on a word:
#
#
# a) Insert a character
# b) Delete a character
# c) Replace a character
#
#


class Solution:
    dp = {}
    # @return an integer

    def minDistance(self, w1, w2):
        key = (w1, w2)
        if key in self.dp:
            return self.dp[key]

        if not w1 or not w2:
            return max(len(w1), len(w2))

        if w1[0] == w2[0]:
            self.dp[key] = self.minDistance(w1[1:], w2[1:])
        else:
            self.dp[key] = min(1 + self.minDistance(w1[1:], w2),
                               1 + self.minDistance(w1, w2[1:]),
                               1 + self.minDistance(w1[1:], w2[1:]))
        return self.dp[key]
