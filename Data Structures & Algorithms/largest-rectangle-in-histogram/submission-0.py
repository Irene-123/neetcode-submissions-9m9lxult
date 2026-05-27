class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left_boundary, right_boundary = [0]*n, [0]*n
        stack = []
        res = 0

        for index in range (n):
            while stack and heights[stack[-1]] >= heights[index]: # 2 >= 4
                stack.pop()  
            left_boundary[index] = -1 if len(stack) == 0 else stack[-1]
            stack.append(index) # stack = [1, 2]

        stack.clear()

        for index in range (n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[index]:
                stack.pop()
            right_boundary[index] = n if len(stack) == 0 else stack[-1]
            stack.append(index)
        
        for index, height in enumerate(heights):
            area = height*(right_boundary[index] - left_boundary[index] - 1)
            # print(left_boundary[index], right_boundary[index], height)
            res = max(res, area)

        return res

