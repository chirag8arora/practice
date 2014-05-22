#coding=utf-8

def insertion_sort(unsorted_list):
    for i in range(1, len(unsorted_list)):
        sub = i
        for j in range(i, 0, -1):
            if unsorted_list[j] <= unsorted_list[i]:
                if sub < i:
                    tmp = unsorted_list[i]
                    unsorted_list[sub+1:i+1] = unsorted_list[sub:i]
                    unsorted_list[sub] = tmp
            else:
                sub = j


if __name__ == '__main__':
    unsorted_list = [1,2,4,6,3,5]
    insertion_sort(unsorted_list)
    print unsorted_list

