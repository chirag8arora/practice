class Solution:
    # @return a string

    def countAndSay(self, n):
        # base case
        if n <= 1:
            return '1'
        t = self.countAndSay(n - 1)
        return self.reader(str(t))

    def reader(self, k):
        res, lenk, i = [], len(k), 0
        while i < lenk:
            if i == lenk - 1:
                res.extend(['1', k[i]])
                break
            else:
                j = i + 1
                while j <= lenk - 1 and k[i] == k[j]:
                    j += 1
                res.extend([str(j - i), k[i]])
                i = j
        return ''.join(res)


if __name__ == '__main__':
    s = Solution()
    print s.countAndSay(2)
