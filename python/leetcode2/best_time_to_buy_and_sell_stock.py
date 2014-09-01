# coding=utf-8
# AC Rate: 31.0%
# SOURCE URL: https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock/
#
# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#


class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        diff = [0]
        for i in range(1, len(prices)):
            diff.append(prices[i] - prices[i-1])

        best = 0
        current = 0
        for i in diff:
            current += i
            if best < current:
                best = current
            if current < 0:
                current = 0
        return best

