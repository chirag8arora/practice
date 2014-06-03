
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer

    def search(self, A, target):

        def find_offset_bs(A, start, end):
            if end < start:
                raise ValueError
            if end == start:
                return start
            mid = start + (end - start) / 2

            if A[mid] >= A[start] and A[mid] > A[end]:
                return find_offset_bs(A, mid + 1, end)
            else:
                return find_offset_bs(A, start, mid)

        def bs_withoffset(A, start, end, offset, target):
            if end < start:
                return -1
            length = len(A)
            if start == end and not A[(start + offset) % length] == target:
                return -1
            mid = start + (end - start) / 2
            actual_mid = (mid + offset) % length
            # print start, end, actual_mid
            if A[actual_mid] == target:
                return actual_mid
            elif A[actual_mid] > target:
                return bs_withoffset(A, start, mid - 1, offset, target)
            elif A[actual_mid] < target:
                return bs_withoffset(A, mid + 1, end, offset, target)
        offset = find_offset_bs(A, 0, len(A) - 1)
        return bs_withoffset(A, 0, len(A) - 1, offset, target)

if __name__ == '__main__':
    s = Solution()
    print s.search([4, 5, 6, 7, 0, 1, 2, 3, 3, 3, 3], 3)
