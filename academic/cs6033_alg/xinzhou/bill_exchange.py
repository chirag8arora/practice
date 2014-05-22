# coding=utf-8
import copy
"""
What is the optimal solution for 379 dollars on {1;5;10;20;50;100}
3 * 100 + 50 + 20 + 5 + 4 * 1

What if it's [1, 5, 10, 20, 50, 94, 100]
We got 3 * 100 + 50 + 20 + 5 + 4 * 1 by alg
But actually should be 4 * 94 + 3 * 1


"""


def bill_exchange(target, S):
    result = []
    for i in sorted(S)[::-1]:
        result.append((target / i, i))
        target = target % i
    return result


def revised_bill_exchange(target, S):
    dp = [(float('inf'), [])] * (target + 1)
    for j in range(1, target + 1):
        for i in sorted(S)[::-1]:
            if j == i:
                dp[j] = (1, [i])
                break
            if j > i:
                if dp[j][0] > dp[j - i][0] + 1:
                    tmp = copy.deepcopy(dp[j - i][1])
                    tmp.append(i)
                    dp[j] = (dp[j - i][0] + 1, tmp)
    return dp[target]

if __name__ == '__main__':
    print bill_exchange(379, [1, 5, 10, 20, 50, 100])
    print revised_bill_exchange(17, [1, 4, 5, 9, 10, 20, 50, 94, 100])
