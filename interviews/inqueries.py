'''
A host got a set of back to back inquiries (reservation requests) for stays of different lengths. The information about them is stored in an array nights[], where nights[i] is the length of a proposed stay number i in nights. Because inquiries stand next to each other (i+1 starts right after i ends) and the host wants to have time to prepare the listing for the next guest, she doesn't want to accept inquiries that are adjacent to each other (if she decides to accept an inquiry number i, she can't also accept i-1 or i+1).

What is the maximum number of nights that the host can accept under this condition?

Useful examples:
[5, 1, 2, 5] = 10
[4, 9, 6] = 10
[4, 11, 6] = 11
[4, 10, 3, 1, 5] = 15


The first example could represent the following set of inquiries:
July 1 - July 6
July 6 - July 7
July 7 - July 9
July 9 - July 14
'''
import unittest


class Solution:

    def find_best(self, inqueries):
        a, b = 0, 0
        for v in inqueries:
            a, b = b, max(v + a, b)
        return b

# def dfs(inqueries):
#     if not inqueries:
#         return 0
#     best = 0
#     stack = []
#     stack.append([1])
#     stack.append([0]) # [1]
#     while stack:
#         node = stack.pop() # [1, 0]
#         if len(node) == len(inqueries):
#             # todo sum
#             sum = 0
#             for k, v in enumerate(node):
#                 if v == 1:
#                     sum += inqueries[k]
#             best = max(best, sum) # 9
#         else:
#             if node[-1] == 1:
#                 stack.append(node + [0])
#             else:
#                 stack.append(node + [0]) # [1] [0, 0]
#                 stack.append(node + [1]) # [1]
#     return best


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.find_best(range(1000)), 250000)
        self.assertEqual(s.find_best(range(10)), 25)
        self.assertEqual(s.find_best([5]), 5)
        self.assertEqual(s.find_best([5, 5, 5, 5, 5]), 15)
        self.assertEqual(s.find_best([4, 9, 6]), 10)
        self.assertEqual(s.find_best([4, 11, 6]), 11)
        self.assertEqual(s.find_best([4, 10, 3, 1, 5]), 15)



if __name__ == "__main__":
    unittest.main()
