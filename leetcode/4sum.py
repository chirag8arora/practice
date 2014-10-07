# coding=utf-8
# AC Rate: 21.5%
# SOURCE URL: https://oj.leetcode.com/problems/4sum/
#
# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
# Note:
#
# Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
# The solution set must not contain duplicate quadruplets.
#
#
#
#     For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
#
#     A solution set is:
#     (-1,  0, 0, 1)
#     (-2, -1, 1, 2)
#     (-2,  0, 0, 2)
#
#


class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]

    def pairs(self, num, target):
        res = set()
        pairs = {}
        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                s = num[i] + num[j]
                if target - s in pairs:
                    for k in pairs[target - s]:
                        if i > k[1]:
                            res.add((num[k[0]], num[k[1]], num[i], num[j]))
                if s not in pairs:
                    pairs[s] = set()

                pairs[s].add((i, j))
        return [list(i) for i in res]

    def fourSum(self, num, target):
        num.sort()
        return self.pairs(num, target)
        # first thought is dfs with 4 n ** 4 which is stupid

s = Solution()
# print s.fourSum([-1, 0, 1], 0)
print s.fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0)
# print s.fourSum([1, 0, -1, 0, -2, 2], 0)
# print s.fourSum(range(-500, 500), 10)
