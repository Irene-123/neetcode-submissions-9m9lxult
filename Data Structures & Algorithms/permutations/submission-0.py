class Solution:
    def recurse(self, nums, perm, picked):
        if len(nums) == len(perm):
            self.res.append(perm.copy())
            return 

        for index in range(len(nums)):
            if not picked[index]:
                picked[index] = True 
                perm.append(nums[index])
                self.recurse(nums, perm, picked)
                perm.pop()
                picked[index] = False


    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        self.recurse(nums, [], [False]*len(nums))
        return self.res