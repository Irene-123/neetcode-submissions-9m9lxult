class Solution:
    def recurse(self, nums, index):
        if index >= len(nums):
            return 0

        return max(nums[index] + self.recurse(nums, index + 2),
                    self.recurse(nums, index+1))

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        if n == 1:
            return nums[0]
        dp[0]= nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[n-1]

        