class Solution:
    def findMin(self, nums: List[int]) -> int:
        curr = nums[0] 

        for num in nums[1:]:
            if num < curr:
                return num

        return curr
        