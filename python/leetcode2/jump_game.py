# coding=utf-8
# AC Rate: 27.2%
# SOURCE URL: https://oj.leetcode.com/problems/jump-game/
#
#
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
#
# Each element in the array represents your maximum jump length at that position.
#
#
# Determine if you are able to reach the last index.
#
#
# For example:
# A = [2,3,1,1,4], return true.
#
#
# A = [3,2,1,0,4], return false.
#
#


class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        canReach = 0
        for k, v in enumerate(A):
            if canReach >= k:
                canReach = max(k + v, canReach)
                if canReach >= len(A) - 1:
                    return True
            else:
                return False

