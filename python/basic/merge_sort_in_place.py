#coding=utf-8

def merge(unsorted, start, mid, end):
    if unsorted[mid] <= unsorted[mid + 1]:
        return
    left, right = start, mid + 1
    while left <= mid and right <= end:
        if unsorted[left] > unsorted[right]:
            tmp = unsorted[right]
            unsorted[left+1: right+1] = unsorted[left: right]
            unsorted[left] = tmp
            left += 1
            right += 1
            mid += 1
        else:
            left += 1

def helper(unsorted, start, end):
    if end <= start:
        return
    mid = start + (end - start) / 2
    helper(unsorted, start, mid)
    helper(unsorted, mid+1, end)
    merge(unsorted, start, mid, end)

def merge_sort(unsorted):
    if unsorted:
        helper(unsorted, 0, len(unsorted) - 1)


if __name__ == '__main__':
    A = [1,3,5,2,4,6,2,1,3,5,61,2,3,5,6,3,2,23,3,45,5,66,99]
    merge_sort(A)
    print A
