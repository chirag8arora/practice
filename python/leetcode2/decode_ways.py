# coding=utf-8
# AC Rate: 16.0%
# SOURCE URL: https://oj.leetcode.com/problems/decode-ways/
# 
# 
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
# 
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# Given an encoded message containing digits, determine the total number of ways to decode it.
# 
# 
# For example,
# Given encoded message "12",
# it could be decoded as "AB" (1 2) or "L" (12).
# 
# 
# The number of ways decoding "12" is 2.
# 
# 


class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        