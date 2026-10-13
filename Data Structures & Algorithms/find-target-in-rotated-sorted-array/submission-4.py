class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        n = len(nums)

        while low < high:
            mid = low + (high - low)//2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        pivot = low
        # 0, 5 -> 2
        # 3, 5 -> 4 
        # 3, 4 -> 3

        if target <= nums[n-1] and target >= nums[pivot]:
            low, high = pivot, n - 1
        else:
            low, high = 0, pivot - 1

        while low <= high:
            mid = low + (high-low)//2 

            if nums[mid] == target:
                return mid 

            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1
