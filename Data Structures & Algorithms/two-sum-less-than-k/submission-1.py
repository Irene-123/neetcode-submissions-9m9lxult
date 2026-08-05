class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # 1 8 23 24 33 34 58 75

        nums.sort()
        ans = -1
        i, j = 0, len(nums)-1

        while i < j:
            temp = nums[i] + nums[j]

            if temp < k:
                i += 1
                ans = temp
            elif temp > k:
                j -= 1
            else:
                break
            

        return ans
        
