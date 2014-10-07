# coding=utf-8
# AC Rate: 27.1%
# SOURCE URL: https://oj.leetcode.com/problems/3sum-closest/
#
# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#     For example, given array S = {-1 2 1 -4}, and target = 1.
#
#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
#


class Solution:
    # @return an integer
    def threeSumClosestNOtGoingToWork(self, num, target):
        # Sorted array, duplicated shouldn't try again
        # O(n**3)
        num.sort()
        # Greedy search
        # Each number only used once
        stack = [(0, 0, 0)] # num, start, depth, sum result
        minimal, best = float('inf'), None
        while stack:
            start, depth, res = stack.pop()
            if depth == 3:
                if abs(res - target) < minimal:
                    best = res
                    minimal = abs(res-target)
            for k in range(start, len(num)):
                if num[k] != num[k-1] or k == start:
                    stack.append((k + 1, depth + 1, res + num[k]))
        return best

    def threeSumClosest(self, num, target):
        # O(n**2)
        best, minimal = None, float('inf')
        num.sort()
        k = 0
        while k < len(num):
            i,j = 0, len(num)-1
            while i < k and j > k:
                s = sum([num[i], num[k], num[j]])
                if s > target:
                    j -= 1
                elif s < target:
                    i += 1
                else:
                    return target

                if abs(target - s) < minimal:
                    minimal = abs(target - s)
                    best = s
            k += 1
        # print minimal
        return best

# -3,0,1,2,

s = Solution()
print s.threeSumClosest([0,2,1,-3], 1)
print s.threeSumClosest([-4,-7,-2,2,5,-2,1,9,3,9,4,9,-9,-3,7,4,1,0,8,5,-7,-7], 29)
print s.threeSumClosest([13,2,0,-14,-20,19,8,-5,-13,-3,20,15,20,5,13,14,-17,-7,12,-6,0,20,-19,-1,-15,-2,8,-2,-9,13,0,-3,-18,-9,-9,-19,17,-14,-19,-4,-16,2,0,9,5,-7,-4,20,18,9,0,12,-1,10,-17,-11,16,-13,-14,-3,0,2,-18,2,8,20,-15,3,-13,-12,-2,-19,11,11,-10,1,1,-10,-2,12,0,17,-19,-7,8,-19,-17,5,-5,-10,8,0,-12,4,19,2,0,12,14,-9,15,7,0,-16,-5,16,-12,0,2,-16,14,18,12,13,5,0,5,6], -59)

# TLE
