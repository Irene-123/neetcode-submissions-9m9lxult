class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()
        dp = [[float('inf')]*(p+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 0
        
        for i in range(n-2, -1, -1):
            for j in range(1, p+1):
                # print(i, j)
                take = max(nums[i+1] - nums[i], dp[i+2][j-1])
                skip = dp[i+1][j]
                dp[i][j] = min(take, skip)
        # print(dp)
        return dp[0][p]
