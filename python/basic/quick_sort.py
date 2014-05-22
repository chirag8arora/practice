#coding=utf-8
"""
quick sort algorithm:
O(logn) time complexity
should sort the list in place

fixed:
1. no absolute index in partition_inplace!!! never!!!
2. pivot swap with right pointer only when pivot is smaller
3. end - start == 1 then list length = 2 !!!!
"""

def quick_sort(unsorted):
    def partition_inplace(unsorted, start, end):
        if (end - start) <= 0:
            pass
        elif (end - start) == 1:
            if unsorted[start] > unsorted[end]:
                unsorted[start], unsorted[end] = unsorted[end], unsorted[start]
        else:
            pivot = unsorted[end]
            left_index = start
            right_index = end - 1
            while left_index < right_index:
                if unsorted[left_index] > pivot and  unsorted[right_index] <= pivot:
                    unsorted[left_index], unsorted[right_index] = unsorted[right_index], unsorted[left_index]
                elif unsorted[left_index] <= pivot:
                    left_index += 1
                elif unsorted[right_index] > pivot:
                    right_index -= 1
            if unsorted[end] <= unsorted[right_index]:
                unsorted[end], unsorted[right_index] = unsorted[right_index], unsorted[end]
            else:
                right_index = end
            if right_index-1 > start:
                partition_inplace(unsorted, start, right_index-1)
            if right_index+1 < end:
                partition_inplace(unsorted, right_index+1, end)

    partition_inplace(unsorted, 0, len(unsorted)-1 )

if __name__ == '__main__':
    unsorted = [9,8,7,6,5,4,3,2,1,0,5,6,7,8]
    print unsorted
    quick_sort(unsorted)
    print unsorted


