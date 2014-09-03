# coding=utf-8
# AC Rate: 22.3%
# SOURCE URL: https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/
#
# Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
#


class Solution:
    # @return an integer

    def lengthOfLongestSubstring(self, s):
        i, j, maximum = 0, 0, 0
        latest = [False] * 256
        while i < len(s):
            if latest[ord(s[i])]:
                maximum = max(maximum, i - j)
                while not s[j] == s[i]:
                    latest[ord(s[j])] = False
                    j += 1
                j+=1
            else:
                latest[ord(s[i])] = True
            i += 1
        maximum = max(maximum, len(s) - j)
        return maximum


s = Solution()
print s.lengthOfLongestSubstring('bbb') == 1
# print s.lengthOfLongestSubstring('abcabcbb') == 3
# print
# s.lengthOfLongestSubstring('wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco')
# == 12
print s.lengthOfLongestSubstring('qopubjguxhxdipfzwswybgfylqvjzhar') == 12
print s.lengthOfLongestSubstring('hnwnkuewhsqmgbbuqcljjivswmdkqtbxixmvtrrbljptnsnfwzqfjmafadrrwsofsbcnuvqhffbsaqxwpqcac') == 12
