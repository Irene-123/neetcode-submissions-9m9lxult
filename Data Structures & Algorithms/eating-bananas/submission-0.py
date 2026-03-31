class Solution:
    def caneatbananas(self, k, piles, h):
        hours = 0 

        for pile in piles:
            hours += pile//k 
            hours += 1 if pile%k else 0

        if hours <= h:
            return True
        else:
            return False 

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s = sum(piles) 
        l, r = 1, s
        k = max(piles)

        if len(piles) > h:
            return k

        while l < r:
            k = (l+r)//2 
            print("k", k)
            if self.caneatbananas(k, piles, h):
                r = k 
                print("Can eat r:", r)
            else: 
                l = k + 1 
                print("Cant eat l:", l)
        return r
        