class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)

        res, subset = [], []

        def dfs(i):
            if i >= len(nums):
                if sum(subset) == target:
                    res.append(subset.copy())
                return
            
            if sum(subset) > target:
                return

            # Include nums[i]
            subset.append(nums[i])
            dfs(i)
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res  
        