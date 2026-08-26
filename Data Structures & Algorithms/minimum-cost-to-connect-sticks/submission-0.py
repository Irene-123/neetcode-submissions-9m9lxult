import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks) 

        ans = 0

        while len(sticks) > 1:
            s1 = heapq.heappop(sticks)
            s2 = heapq.heappop(sticks)

            ans += (s1 + s2)

            heapq.heappush(sticks, s1+s2)


        return ans

