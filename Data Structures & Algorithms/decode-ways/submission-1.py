class Solution:
    def recurse(self, s, index):
        if index >= len(s):
            return 0

        res1, res2 = 0, 0

        if int(s[index]) + 64 <= 90:
            res1 = 1 + self.recurse(s, index + 1) 
        if index + 1 < len(s) and int(s[index : index + 1]) + 64 <= 90:
            res2 = 1 + self.recurse(s, index + 2) 
        
        return max(res1, res2)
        


    def numDecodings(self, s: str) -> int:
        # A to Z == 65 to 90
        n = len(s)
        dp = {n : 1}

        for i in range(n-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0 # No. of ways to decode s[i:]
            else:
                dp[i] = dp[i+1]

            if i + 1 < n and ((s[i] == "1") or (s[i] == "2" and s[i+1] in "0123456")):
                dp[i] += dp[i+2]

        return dp[0]


        