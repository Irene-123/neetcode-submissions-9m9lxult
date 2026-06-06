class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        maxproduct = nums[0]

        for i in range(len(nums)):
            maxproduct = nums[i]
            res = max(res, maxproduct)
            for j in range(i+1, len(nums)):
                maxproduct *= nums[j]
                res = max(res, maxproduct)

                
            

        return res


