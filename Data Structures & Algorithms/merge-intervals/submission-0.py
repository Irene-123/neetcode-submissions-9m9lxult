class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals) 
        if n == 1:
            return intervals
        # [[1,5], [1,7]]
        # Recursion
        # [[1,3], [2,5], [1,7], [2,8], [8, 9]]
        # [[1, 7], [2, 8]]
        intervals.sort()
        res = [] 

        res.append(intervals[0])
        for i, interval in enumerate(intervals):
            lastEnd = res[-1][1]
            if interval[0] <= lastEnd:
                res[-1][1] = max(lastEnd, interval[1])
            else:
                res.append(interval)
        return res
