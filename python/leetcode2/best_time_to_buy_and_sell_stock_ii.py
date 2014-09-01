# coding=utf-8
# AC Rate: 36.8%
# SOURCE URL: https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
#
# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#


class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0
        for k, i in enumerate(prices):
            if k >= 1:
                if i - prices[k - 1] > 0:
                    profit += i - prices[k - 1]
        return profit


