class Solution:
    # def recurse
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        min_val = float('inf')

        for i in range(len(prices)):

            min_val = min(min_val, prices[i])

            profit = max(profit, prices[i] - min_val)

        return profit



