class Solution:
    # @return a boolean

    def isInterleave(self, s1, s2, s3):
        if not len(s3) == len(s1) + len(s2):
            return False
        if s3:
            if s3 and s1 and s3[0] == s1[0]:
                if self.isInterleave(s1[1:], s2, s3[1:]):
                    return True
            if s3 and s2 and s3[0] == s2[0]:
                return self.isInterleave(s1, s2[1:], s3[1:])
            return False
        else:
            return True


if __name__ == '__main__':
    s = Solution()
    s1 = 'bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa'
    s2 = 'babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab'
    s3 = 'babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab'
    # s3 = 'aadbbbaccc'
    print s.isInterleave(s1, s2, s3)
