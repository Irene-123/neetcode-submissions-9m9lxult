class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []

        def recurse(i):
            if i >= len(nums):
                res.append(subset.copy())
                return 

            subset.append(nums[i])
            recurse(i+1)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            recurse(i+1)

        nums.sort()
        recurse(0)
        return res