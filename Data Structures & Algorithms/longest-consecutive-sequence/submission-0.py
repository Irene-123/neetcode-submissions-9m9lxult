class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0 
        s = set(nums)

        

        for num in s:
            if num-1 not in s:
                lcs = 1
                while num + lcs in s:
                    lcs+=1
                res = max(res, lcs) 

        return res
        