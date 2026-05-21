class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algo - Discard a -ve subarray 
        
        currsum = 0 
        maxsum = nums[0] 

        for n in nums:
            currsum = max(currsum, 0) 
            currsum += n 

            maxsum = max(maxsum, currsum) 

        return maxsum

        
        