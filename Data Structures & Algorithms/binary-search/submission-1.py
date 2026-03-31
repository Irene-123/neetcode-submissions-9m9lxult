class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:

            mid = (left + right) // 2
            midnum = nums[mid]

            if midnum < target:
                left = mid + 1 
            elif midnum > target:
                right = mid 
            else:
                return mid
        
        return -1
