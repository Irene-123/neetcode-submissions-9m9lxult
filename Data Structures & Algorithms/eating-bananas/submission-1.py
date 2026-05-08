class Solution:
    def canEat(self, piles, mid, h):
        curr_hours = 0 
        for pile in piles:
            curr_hours += (pile + mid - 1)//mid
        return curr_hours <= h


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles) 
        start, end = 1, max(piles) 

        while start < end:
            mid = start + (end - start)//2

            if self.canEat(piles, mid, h):
                end = mid
            else:
                start = mid + 1 
        return start
        