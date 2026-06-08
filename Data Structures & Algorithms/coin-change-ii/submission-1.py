class Solution:
    def recurse(self, amount, coins, index):
        if amount == 0:
            return 1 
        if amount < 0 or index >= len(coins):
            return 0 

        return self.recurse(amount - coins[index], coins, index+1) + \
        self.recurse(amount - coins[index], coins, index)
        
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [[0]*(len(coins)) for i in range(amount+1)]

        for i in range(len(coins)):
            dp[0][i] = 1

        for i in range(1, amount+1):
            for j in range(len(coins)):
                if j > 0:
                    dp[i][j] = dp[i][j-1]
                if i - coins[j] >= 0:
                    dp[i][j] += dp[i - coins[j]][j] 

        # print(dp)
        return dp[amount][len(coins)-1]