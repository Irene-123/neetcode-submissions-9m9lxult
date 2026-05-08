class Solution:
    def SatisfiesSums(self, nums, expected_sum, k):
        # For a given sum, how many subarrays do we need?
        # If > k, try a bigger sum value 
        # Else, we can try more minimised sum 

        subarrays_needed = 1
        curr_sum = 0 

        for num in nums:
            if curr_sum + num > expected_sum:
                subarrays_needed += 1
                curr_sum = num
            else:
                curr_sum += num 
        if subarrays_needed > k:
            return False
        return True 


    def splitArray(self, nums: List[int], k: int) -> int:
        start, end = max(nums), sum(nums)

        while start < end:
            mid = start + (end - start)//2 

            if self.SatisfiesSums(nums, mid, k):
                end = mid 
            else:
                start = mid + 1

        return start

        