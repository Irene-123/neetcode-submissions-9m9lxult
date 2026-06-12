class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def recurse(i, total):
            if i >= len(nums):
                if total == target:
                    return 1
                return 0

            
            a = recurse(i+1, total + nums[i])
            b = recurse(i+1, total - nums[i])

            return a + b
        
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n+1)]

        # dp = [0 : {}, 1 : {}, 2 : {}]
        dp[0][0] = 1

        for i in range(n):
            for sum, count in dp[i].items():
                dp[i+1][sum + nums[i]] += count 
                dp[i+1][sum - nums[i]] += count

        return dp[n][target]












