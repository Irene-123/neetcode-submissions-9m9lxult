class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                index = stack[-1][1]
                ans[index] = i - index
                stack.pop()
            stack.append([temp, i])
        return ans

            
        