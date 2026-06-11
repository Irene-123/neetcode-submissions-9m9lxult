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
        
        # dp = [[0]*(total + 1) for i in range(len(nums))]
        return recurse(0,0)