class Solution:
    # @return a boolean
    """
    s1 = 'aabaac'
    s2 = 'aadaaeaaf'
    s3 = 'aadaaeaabaafaac'
    [,          a,          aa,         -1,             -1,             -1,             -1]
    [a,         aa,         -1,         -1,             -1,             -1,             -1]
    [aa,        -1,         -1,         -1,             -1,             -1,             -1]
    [aad,       aada,       aadaa,      -1,             -1,             -1,             -1]
    [aada,      aadaa,      -1,         -1,             -1,             -1,             -1]
    [aadaa,     -1,         -1,         -1,             -1,             -1,             -1]
    [aadaae,    aadaaea,    aadaaeaa,   aadaaeaab,      aadaaeaaba,     aadaaeaabaa,    -1]
    [aadaaea,   aadaaeaa,   -1,         aadaaeaaba,     aadaaeaabaa,    -1,             -1]
    [aadaaeaa,  -1,         -1,         aadaaeaabaa,    -1,             -1,             -1]
    [-1,        -1,         -1,         aadaaeaabaaf,   aadaaeaabaafa,  aadaaeaabaafaa, aadaaeaabaafaac]
    """

    def isInterleave(self, s1, s2, s3):
        if not len(s3) == len(s1) + len(s2):
            return False

        dp = [[None] * (len(s1) + 1) for i in range(len(s2) + 1)]

        # initial first row
        for i in range(len(s1) + 1):
            if s1[:i] == s3[:i]:
                dp[0][i] = (s1[:i], 0, i)
            else:
                for j in range(i, len(s1) + 1):
                    dp[0][j] = -1
                break

        # initial first col
        for i in range(len(s2) + 1):
            if s2[:i] == s3[:i]:
                dp[i][0] = (s2[:i], i, 0)
            else:
                for j in range(i, len(s2) + 1):
                    dp[j][0] = -1
                break

        # dp
        for i in range(1, len(s2) + 1):
            for j in range(1, len(s1) + 1):
                # print i, j
                if dp[i - 1][j] == -1 and dp[i][j - 1] == -1:
                    dp[i][j] = -1
                else:
                    if dp[i - 1][j] != -1:
                        tmp = dp[i - 1][j][0]
                        y = dp[i - 1][j][1]
                        x = dp[i - 1][j][2]
                        if tmp + s2[y] == s3[:len(tmp) + 1]:
                            dp[i][j] = (tmp + s2[y], y + 1, x)
                        else:
                            dp[i][j] = -1
                    if dp[i][j - 1] != -1:
                        tmp = dp[i][j - 1][0]
                        y = dp[i][j - 1][1]
                        x = dp[i][j - 1][2]
                        if tmp + s1[x] == s3[:len(tmp) + 1]:
                            dp[i][j] = (tmp + s1[x], y, x + 1)
                        else:
                            dp[i][j] = -1
        return dp[-1][-1] != -1


if __name__ == '__main__':
    s = Solution()
    # s1 = 'bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa'
    # s2 = 'babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab'
    # s3 = 'babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab'
    # s3 = 'aadbbbaccc'
    s1 = 'aabaac'
    s2 = 'aadaaeaaf'
    s3 = 'aadaaeaabaafaac'
    print s.isInterleave(s1, s2, s3)
