"""
Project Euler Problem 2
=======================

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:

                  1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not
exceed four million.
"""

def helper():
    dp = [1, 2]
    last, res = 0, 0
    while True:
        last = dp[-1] + dp[-2]
        if last > 4000000:
            break

        if last % 2 == 0:
            res += last

        dp.append(last)
    return res + 2

print helper()
