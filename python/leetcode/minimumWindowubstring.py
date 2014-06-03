"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".


Without Heap Still TLE
With Heap Is Compile Error
But I DONT WANNA WRITE A HEAP MYSELF
WTF DAY
"""
import heapq

class Solution:
    # @return a string

    def minWindow(self, S, T):
        heap = []
        c = set([i for i in T])
        fd = {}
        for i in T:
            if i in fd:
                fd[i] += 1
            else:
                fd[i] = 1

        found = {}

        best_length = float('inf')
        result = ''

        for k, v in enumerate(S):
            if v in c:
                max_index = k
                if not fd:
                    heapq.heappush(heap, k)
                    heap.pop(0)
                else:
                    heapq.heappush(heap, k)
                min_index = heap[0]
                if (max_index - min_index) < best_length:
                    result = S[min_index: max_index + 1]
            if v in fd:
                if fd[v] <= 1:
                    del fd[v]
                else:
                    fd[v] -= 1
        return result


if __name__ == '__main__':
    # S = "ADOBECODEBANC"
    # T = "ABC"
    S = "aa"z
    T = "aa"
    s = Solution()
    print s.minWindow(S, T)
