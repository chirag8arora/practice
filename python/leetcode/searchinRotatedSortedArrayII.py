"""
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?
Would this affect the run-time complexity? How and why?
Write a function to determine if a given target is in the array.
"""


class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean

    def search(self, A, target):

        def find_offset_bs(A):
            for i, v in enumerate(A):
                if v < A[i - 1]:
                    return i
            return 0

        def bs_withoffset(A, start, end, offset, target):
            if end < start:
                return False
            length = len(A)
            if start == end and not A[(start + offset) % length] == target:
                return False
            mid = start + (end - start) / 2
            actual_mid = (mid + offset) % length
            # print start, end, actual_mid
            if A[actual_mid] == target:
                return True
            elif A[actual_mid] > target:
                return bs_withoffset(A, start, mid - 1, offset, target)
            elif A[actual_mid] < target:
                return bs_withoffset(A, mid + 1, end, offset, target)
        offset = find_offset_bs(A)
        return bs_withoffset(A, 0, len(A) - 1, offset, target)

if __name__ == '__main__':
    s = Solution()
    print s.search([1], 0)
