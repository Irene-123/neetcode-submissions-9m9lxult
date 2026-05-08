class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        s = set(nums) 
        lcs = 0
        res = 0
        for num in nums:
            curr = num 
            lcs = 0
            while curr in s:
                curr += 1 
                lcs += 1 
            res = max(lcs, res) 
        return res


        