class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        pivot = -1 
        n = len(nums)

        for i in range(n-2, -1, -1):
            if nums[i+1] > nums[i]:
                pivot = i 
                break
        if pivot == -1:
            nums.reverse()
            return 
        # print(pivot)

        # Increase pivot to get the next permutation ==> Core Idea 
        # 3, 1, 2, 4
        # 3, 1, 4, 2 
        # 3, 2, 4, 1
        # Find the next smallest element 
        # Else 
        # Sort from the pivot 
        smallest = float('inf')
        smallest_index = -1
        for i in range(pivot + 1, n):
            if nums[i] < smallest and nums[i] > nums[pivot]:
                smallest = nums[i]
                smallest_index = i

        nums[pivot], nums[smallest_index] = nums[smallest_index], nums[pivot]
        nums[pivot+1: n] = nums[pivot+1: n][::-1]

            

        # 2, 1, 3
        # 2, 3, 1 
        
        # [ prefix | pivot | suffix ]
        #     ↓
        # make pivot bigger
        #     ↓
# [ prefix | slightly bigger | smallest possible suffix ]

