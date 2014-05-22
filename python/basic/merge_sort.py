#coding=utf-8


def merge(sorted1, sorted2):
    res = []
    while sorted1 and sorted2:
        if sorted1[0] < sorted2[0]:
            res.append(sorted1.pop(0))
        else:
            res.append(sorted2.pop(0))
    res.extend(sorted1)
    res.extend(sorted2)
    return res

def merge_sort(unsorted):
    length = len(unsorted)
    if length == 1:
        return unsorted
    else:
        mid = length/2
        s1 = merge_sort(unsorted[:mid])
        s2 = merge_sort(unsorted[mid:])
        return merge(s1, s2)


if __name__ == '__main__':
    print merge_sort([1,3,5,2,2,5,6,84,3,7,9,0,34,2])
