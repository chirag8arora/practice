# 5.16
# left -> right, top += 1, change dir
# top -> bottom, right -= 1, change dir
# right -> left, bottom -= 1
# bottom -> top  left += 1
# l 0, r 2, t 0, b 2
# t->1 r -> 1 b -> 1 l -> 1

class Solution():
    def print2d(self, A):
        if not A:
            return []
        left, top, result, direction = 0, 0, [], 0
        right, bottom = len(A[0]) - 1, len(A) - 1
        while left <= right and top <= bottom:
            if direction == 0:
                for i in range(left, right+1):
                    result.append(A[top][i])
                direction, top = 1, top + 1
            elif direction == 1:
                for i in range(top, bottom+1):
                    result.append(A[i][right])
                direction, right = 2, right - 1
            elif direction == 2:
                for i in range(left, right + 1)[::-1]:
                    result.append(A[bottom][i])
                direction, bottom = 3, bottom - 1
            elif direction == 3:
                for i in range(top, bottom + 1)[::-1]:
                    result.append(A[i][left])
                direction, left = 0, left + 1
        return result

A = [
    [1,2,3,5],
    [4,5,6,6],
    [7,8,9,7]
]
B = [[1,2,3,4]]
C = [
    [1],
    [2],
    [3]
]
s = Solution()
print s.print2d(A) == [1,2,3,5,6,7,9,8,7,4,5,6]
print s.print2d(B) == [1,2,3,4]
print s.print2d(C) == [1,2,3]
