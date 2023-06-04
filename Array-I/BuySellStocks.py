
#   ***  Stock Buy And Sell
# Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


# Brute Approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxPro = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] < prices[j]:
                    maxPro = max(maxPro, prices[j] - prices[i])

        return maxPro


# Optimal

import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxPro = 0
        minPrice = math.inf

        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            maxPro = max(maxPro, prices[i] - minPrice)

        return maxPro 