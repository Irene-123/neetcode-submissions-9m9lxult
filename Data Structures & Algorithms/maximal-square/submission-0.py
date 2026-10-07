class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        area = 1
        n, m = len(matrix), len(matrix[0])
        dp = [[0]*m for _ in range(n)]

        maxSide = 0

        for i in range(n):
            if matrix[i][0] == "1":
                dp[i][0] = 1 
                maxSide = 1
                
        for i in range(m):
            if matrix[0][i] == "1":
                dp[0][i] = 1
                maxSide = 1

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == "1":
                    dp[i][j] = 1 + min (
                        dp[i-1][j], 
                        dp[i][j-1],
                        dp[i-1][j-1]
                    )
                maxSide = max(maxSide, dp[i][j])
        return maxSide*maxSide






