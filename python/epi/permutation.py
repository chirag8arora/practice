import unittest

# permutations
class Permutations:
    def permutation(self, A):
        start = sorted(A)
        return [i for i in self.helper(A)]

    def helper(self, A):
        if len(A) <= 1:
            return [A]
        res = []
        for k in range(len(A)):
            rest = A[:k] + A[k+1:]
            for i in self.helper(rest):
                i.insert(0, A[k])
                res.append(i)
        return res


class Test(unittest.TestCase):
    def test(self):
        p = Permutations()
        print p.permutation([2,3,4,7])


if __name__ == '__main__':
    unittest.main()
