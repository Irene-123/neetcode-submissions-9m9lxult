class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = {}
        for c in s1:
            d[c] = d.get(c, 0) + 1 
        n = len(s2)
        curr = {}

        for i in range(0, n):
            c = s2[i]
            curr[c] = curr.get(c, 0) + 1 

            if i >= len(s1):
                left = s2[i - len(s1)]
                if curr[left] == 1:
                    del curr[left]
                else:
                    curr[left] -= 1

            if curr == d:
                return True
                
                

        return False
                



            
        