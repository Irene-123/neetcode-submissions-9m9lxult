class Solution:
    def recurse(self, s, n): # Top down approach
        if n < 0:
            return 1

        if self.dp[n] != -1:
            return self.dp[n]
        res = 0
        if int(s[n]) > 0:
            res = self.recurse(s, n-1)

        if n - 1 >=0 and int(s[n-1]) != 0 and int(s[n-1: n+1]) <= 26:
            res += self.recurse(s, n-2)
        
        self.dp[n] = res
        return res

    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+1)
        dp[0] = 1

        for i in range(1, n+1):
            if int(s[i-1]) > 0:
                dp[i] += dp[i-1]
            if i - 2 >= 0 and int(s[i-2]) != 0 and int(s[i-2: i]) <= 26:
                dp[i] += dp[i-2]
        # print(dp)
        return dp[n]
            
        