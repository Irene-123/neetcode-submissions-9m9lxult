class Solution:
    def recurse(self, t1, t2, i, j):
        if i >= len(t1) or j >= len(t2):
            return 0

        if t1[i] == t2[j]:
            return 1 + self.recurse(t1, t2, i+1, j+1)
        else:
            return max(self.recurse(t1, t2, i, j+1), self.recurse(t1, t2, i+1, j))


    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        
        n, m = len(t1), len(t2)
        dp = [[0]*(m+1) for i in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                # print(t1[i-1], t2[j-1], i, j)
                if t1[i-1] == t2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n][m]










