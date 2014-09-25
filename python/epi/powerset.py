class PowerSet():
    def powerset(self, A):
        if A is None:
            return []
        if len(A) == 0:
            return [A]
        res = []
        ps = self.powerset(A[1:])
        for i in ps:
            res.append(i)
            res.append([A[0]] + i)
        return res

ps = PowerSet()
print ps.powerset([1,2,3])
