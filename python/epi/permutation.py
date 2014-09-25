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


p = Permutations()
print p.permutation([2,3,4,7])

# k = 0
#     rest = [3, 5]
#         k = 0
#             rest = [5]
#         [3, 5]
#     [2, 3, 5]
#         k = 1
#             rest = [3]
#         [5, 3]
#     [2, 3, 5]

k = 1
k = 2


# 1, 2, 3, 4
# 1, 2, 4, 3
# 1, 3, 2, 4
# 1, 3, 4, 2
# 1, 4, 2, 3
# 1, 4, 3, 2
# 1 -> [2, 3, 4]
# 2 -> [1, 3, 4]
# 3 -> [1, 2, 4]
# 4 -> [1, 2, 3]
