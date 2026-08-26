class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # 1 4 8 13 

        max_freq = 1
        nums.sort() 
        left = 0
        sum = 0 

        for right in range(len(nums)):

            sum += nums[right]
            target = nums[right]

            cost = target*(right - left + 1) - sum

            while cost > k:
                sum -= nums[left]
                left += 1
                cost = nums[right] * (right - left + 1) - sum

            max_freq = max(right-left + 1, max_freq)
            

        return max_freq

        


        

        
