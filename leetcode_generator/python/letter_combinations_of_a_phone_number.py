# AC Rate: 26.2%
# SOURCE URL: https://oj.leetcode.com/problems/letter-combinations-of-a-phone-number/
# 
# Given a digit string, return all possible letter combinations that the number could represent.
# 
# 
# A mapping of digit to letters (just like on the telephone buttons) is given below.
# 
# 
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# 
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.
# 
# 


class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        