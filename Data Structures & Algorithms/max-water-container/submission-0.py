class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0 
        n = len(heights)
        # find left max 
        # find right max 
        # Compute max iteratively 

        i,j = 0, n-1
        while i < j:
            area = (j-i)*min(heights[i], heights[j])
            res = max(area, res)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return res

        
        