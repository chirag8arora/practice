class Solution():

    def convert(self, s, b1, b2):
        r = self.stoi(s, b1)
        return self.itos(r, b2)

    def ctoi(self, c):
        o = ord(c)
        if o >= 65 and ord(c) <= 70:
            return o - 65 + 10
        elif o >= 48 and o <= 57:
            return o - 48

    def stoi(self, s, b1):
        r = 0
        for i in s:
            r = r * b1 + self.ctoi(i)
        return r

    def itos(self, r, b2):
        res = []
        while r:
            res.append(str(r % b2))
            r /= b2
        return ''.join(res[::-1])

s = Solution()
print s.convert('1AC', 15, 10)
# r = 1, 10 16 + 10 =26
# 0, 13, 1, 6, 0, 3, 1, 1
# 0 1 0 1 1 # '11010'
