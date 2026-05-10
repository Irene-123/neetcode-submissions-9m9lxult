from collections import defaultdict
from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)
    
    def atMostK(self, nums: List[int], k: int) -> int:
        if k <= 0:
            return 0
            
        freq = defaultdict(int)
        left = 0
        count = 0
        distinct = 0
        
        for right in range(len(nums)):
            # Add current element
            freq[nums[right]] += 1
            if freq[nums[right]] == 1:
                distinct += 1
            
            # If we have more than k distinct, shrink window from left
            while distinct > k and left <= right:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    distinct -= 1
                left += 1
            
            # All subarrays ending at 'right' with at most k distinct
            # are valid → there are (right - left + 1) such subarrays
            count += (right - left + 1)
        
        return count