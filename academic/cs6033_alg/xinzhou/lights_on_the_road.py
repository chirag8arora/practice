# coding=utf-8

def main(S, K):
    lighted_area = []
    light_count = 0
    for i in S:
        if i not in lighted_area:
            lighted_area.extend(range(i, i + K + 1))
            light_count += 1
    return light_count

if __name__ == '__main__':
    print main([2, 4, 6, 7, 9], 3)
    print main([1, 2, 3, 8, 9], 2)
