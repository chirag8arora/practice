# coding=utf-8
# AC Rate: 26.5%
# SOURCE URL: https://oj.leetcode.com/problems/combination-sum/
#
#

# Given a set of candidate numbers (C) and a target number (T), find all
# unique combinations in C where the candidate numbers sums to T.

#
# The same repeated number may be chosen from C unlimited number of times.

#
# Note:
#
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
# The solution set must not contain duplicate combinations.
#
#
#

# For example, given candidate set 2,3,6,7 and target 7,

# A solution set is:
# [7]
# [2, 2, 3]
#
#
#
import copy


class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers

    def combinationSum(self, candidates, target):
        # native
        # todo it returns non-unique
        # todo [2], 6
        res = []
        if target == 0:
            return [[], ]
        while candidates:
            i = candidates.pop()
            k = 1
            while target >= i * k:
                cc = copy.deepcopy(candidates)
                for j in self.combinationSum(cc, target - i * k):
                    j.extend([i] * k)
                    # sort for leetcode judge, which is a bug I think
                    j.sort()
                    res.append(j)
                k += 1
        return res

if __name__ == '__main__':
    s = Solution()
    print s.combinationSum([8,7,4,3], 11)
