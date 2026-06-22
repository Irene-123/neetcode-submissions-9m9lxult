class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        i = 1
        jump = nums[0]

        while i < n:
            if i <= jump:
                jump = max(jump, i + nums[i])
            else:
                return False
            i+=1

        return True 
            