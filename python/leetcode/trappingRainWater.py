class Solution:
    # @param A, a list of integers
    # @return an integer

    def trap(self, A):
        start = 0
        total = 0
        trapped = 0
        total = 0
        start_index = -1
        for k, i in enumerate(A):
            if i >= start:
                total += trapped
                trapped = 0
                start = i
                start_index = k
            else:
                trapped += start - i
        if trapped != 0:
            next = [max(A[start_index + 1:])]
            next.extend(A[start_index + 1:])
            total += self.trap(next)
        return total


if __name__ == '__main__':
    A = [4, 2, 3]
    s = Solution()
    print s.trap(A)
