class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(numbers):
            map[target-num] = i 

        for i, num in enumerate(numbers):
            if num in map:
                if map[num] < i:
                    return [map[num] + 1, i + 1]
        