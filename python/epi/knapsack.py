# 65, 20
# 35, 8
# 245, 60
# 195, 55
# 65, 40
# 150, 70
# 275, 85
# 155, 25
import unittest


class Solution1:
    # time complexity
    # for each clock there is two situation
    # look at dp really! it's nw
    # n is the clocks number
    # w is the weight
    # because it's int, which won't be a lot
    # if without this dp, it could be 2**n

    def find_way(self, clocks, capacity):
        self.dp = {}
        self.clocks = clocks
        return self.helper(0, capacity)


    def helper(self, start, capacity):
        # so choose 20, then capacity - 20,
        # then find_way(clocks[1:], capacity - 20)
        # base case
        if capacity < 0:
            return float('-inf')
        if start >= len(self.clocks):
            return 0

        if (start, capacity) not in self.dp:
            without_start = self.helper(start+1, capacity)
            with_start = self.helper(start+1,
                capacity-self.clocks[start][1]) + self.clocks[start][0]
            self.dp[(start, capacity)] = max(without_start, with_start)
        return self.dp[(start, capacity)]


# this is a problem
# class Solution2:
#     # now let's improve it saving some dp space
#     def find_way(self, clocks, capacity):
#         # first still use dp
#         dp = {}
#         for k, v in enumerate(clocks):
#             dp[(k, )]

class Test(unittest.TestCase):

    def test(self):
        s = Solution1()
        clocks1 = [(55, 10), (25, 10), (65,20), (75, 20)]
        self.assertEqual(s.find_way(clocks1, 30), 130)

    def test1(self):
        s = Solution1()
        clocks = ((65, 20), (35, 8), (245, 60), (195, 55),
                (65, 40), (150, 70), (275, 85), (155, 25),
                (120, 30), (320, 65), (75, 75), (40, 10),
                (200, 95), (100, 50), (220, 40), (99, 10))
        self.assertEqual(s.find_way(clocks, 130), 695)


if __name__ == '__main__':
    unittest.main()
