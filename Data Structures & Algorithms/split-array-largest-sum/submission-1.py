class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def backtrack(start: int, parts_left: int) -> int:
            if parts_left == 1:
                return sum(nums[start:])
            
            min_largest = float('inf')
            curr_sum = 0
            if dp[start][parts_left] != -1:
                return dp[start][parts_left]
            
            for i in range(start, len(nums) - parts_left + 1):
                curr_sum += nums[i]
                cost = max(curr_sum, backtrack(i+1, parts_left-1))
                min_largest = min(min_largest, cost)
            
            dp[start][parts_left] = min_largest
            return min_largest

        dp = [[-1]*(k+1) for _ in range(len(nums) + 1)]
        return backtrack(0, k)