class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer

    def subsetsWithDup(self, S):
        S.sort()
        def get_bit(byteval, idx):
            return ((byteval & (1 << idx)) != 0)
        m = 2 ** len(S)
        hashset = set()
        result = []
        for i in range(m):
            e = []
            for j in range(len(S)):
                if get_bit(i, j):
                    e.append(S[j])
            hashvalue = ''.join([str(j) for j in e])
            if hashvalue not in hashset:
                hashset.add(hashvalue)
                result.append(e)
        return result


if __name__ == '__main__':
    s = Solution()
    print s.subsetsWithDup([4, 1, 0])
