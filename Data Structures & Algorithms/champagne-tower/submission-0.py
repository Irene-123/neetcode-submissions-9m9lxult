class Solution:
    # def recurse(self, row, glass):
    #     if row < 0 or glass < 0 or glass > row:
    #         return 0
    #     if row == 0 and glass == 0:
    #         return self.poured
        
    #     total = 0

    #     # Compute the overflow from left parent, and right parent
    #     # Each gives 0.5 of excess

    #     left = max(0, self.recurse(row-1, glass-1) - 1)
    #     right = max(0, self.recurse(row - 1, glass) - 1)

    #     return (left + right)/2

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0]*(i+1) for i in range(query_row + 2)]
        dp[0][0] += poured 

        for row in range(min(99, query_row + 1)):
            for glass in range(row+1):
                excess = (dp[row][glass] - 1.0)/2.0
                if excess > 0:
                    dp[row+1][glass] += excess
                    dp[row+1][glass + 1] += excess

        return min(1.0, dp[query_row][query_glass])


