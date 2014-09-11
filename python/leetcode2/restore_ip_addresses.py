# coding=utf-8
# AC Rate: 20.5%
# SOURCE URL: https://oj.leetcode.com/problems/restore-ip-addresses/
#
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# For example:
# Given "25525511135",
#
#
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
#
#


class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        res = []
        stack = [([], s)]
        while stack:
            comb, s = stack.pop()
            if not s:
                if len(comb) == 4:
                    res.append('.'.join(comb))
                continue
            # children
            if len(s) >= 1 and len(s) - 1 <= (4 - len(comb) - 1) * 3:
                stack.append((comb+[s[:1]], s[1:]))
            # if starts with 0 then no these
            if len(s) >= 2 and len(s) - 2 <= (4 - len(comb) - 1) * 3:
                if s[:2][0] != '0':
                    # cannot starts with 0
                    stack.append((comb+[s[:2]], s[2:]))
            if len(s) >= 3 and len(s) - 3 <= (4 - len(comb) - 1) * 3 and int(s[:3]) <= 255:
                if s[:3][0] != '0':
                    stack.append((comb+[s[:3]], s[3:]))
        return res


s = Solution()
print s.restoreIpAddresses('25525511135'):
print s.restoreIpAddresses('010010'):
