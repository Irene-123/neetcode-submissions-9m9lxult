class Solution:
    def recurse(self, s, n):
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
        self.dp = [-1]*(n+1)

        return self.recurse(s, n-1)
        