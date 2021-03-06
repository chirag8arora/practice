# coding=utf-8
# AC Rate: 28.7%
# SOURCE URL: https://oj.leetcode.com/problems/trapping-rain-water/
#
#
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
#
#
# For example,
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
#
#
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
#


class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        # first solution is find the maximum first
        # for its left side we do ->
        # for its right side we do <-
        # for its left side
        # then we don't have to worry if right side is high enough
        # same with its right side
        maximum, maximum_idx = A[0], 0
        for i in range(len(A)):
            if
