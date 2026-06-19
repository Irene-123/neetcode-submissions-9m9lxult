class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min1, min2 = float('inf'), float('inf')
        max1, max2 = float('-inf'), float('-inf')
        min_index, max_index = 0, 0

        for i, arr in enumerate(arrays):
            if min1 > arr[0]:
                min2 = min1
                min1 = arr[0]
                min_index = i

            if min2 > arr[0] and i != min_index:
                min2 = arr[0]

            if max1 < arr[-1]:
                max2 = max1
                max1 = arr[-1]
                max_index = i

            if max2 < arr[-1] and i != max_index:
                max2 = arr[-1]


        if min_index != max_index:
            print("here")
            return abs(max1 - min1)
        else:
            print(max1, min1)
            print(max2, min2)
            return max(abs(max1 - min2), abs(max2 - min1))