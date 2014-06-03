"""
could be better
"""
import json


class Solution:
    # @return a string

    def longestCommonPrefix(self, strs):
        # edges
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        str0 = strs.pop()
        # prefix tree (actually hash table)
        dic = {}
        tmp = dic
        for char in str0:
            tmp[char] = {}
            tmp = tmp[char]

        min_length = float('inf')
        for string in strs:
            current = 0
            tmp = dic
            for char in string:
                if char in tmp:
                    current += 1
                    tmp = tmp[char]
                else:
                    break
            min_length = min(min_length, current)
        return str0[:min_length]

if __name__ == '__main__':
    s = Solution()
    print s.longestCommonPrefix(['aa', 'aa', 'ab'])
