# AC Rate: 23.5%
# SOURCE URL: https://oj.leetcode.com/problems/anagrams/
# 
# Given an array of strings, return all groups of strings that are anagrams.

# 
# Note: All inputs will be in lower-case.
# 


class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        anadic = {}
        anakey = None
        for i in strs:
            if i:
                if self.ana(i) in anadic:
                    anakey = self.ana(i)
                    anadic[self.ana(i)].append(i)
                else:
                    anadic[self.ana(i)] = [i]

        if anakey:
            return anadic[anakey]
        else:
            return []
    
    def ana(self, s):
        ana = 0
        for k, i in enumerate('abcdefghijklmnopqrstuvwxyz'):
            ana = ana * 26 + k * s.count(i)
        return ana
