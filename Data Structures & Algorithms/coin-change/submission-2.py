class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # def dfs(amount):
        #     if amount == 0:
        #         return 0
        #     if dp[amount] != 1e9:
        #         return dp[amount]
        #     res = 1e9
        #     for coin in coins:
        #         if amount - coin >= 0:
        #             res = min(res, 1 + dfs(amount-coin))
        #     dp[amount] = res
        #     return res

        dp = [amount + 1]*(amount + 1)
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a-c] + 1)
                
        return dp[amount] if dp[amount] != (amount + 1) else -1

        













        