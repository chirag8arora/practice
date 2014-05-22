class Solution:
    # @param A, a list of integers
    # @return an integer

    def trap(self, A):


if __name__ == '__main__':
    A = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print A
    print  [i - 1 for i in A]
    print  [i - 2 for i in A]
    print  [i - 3 for i in A]
    # [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # [0, 0, 0, 1, 0, 0, 0, 2, 1, 0, 1, 0]
    # [0, 0, 0, 1, 0, 0, 0, 2, 1, 0, 1, 0]
    # [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    s = Solution()
    print s.trap(A)
