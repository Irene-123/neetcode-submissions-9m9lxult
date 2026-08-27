import heapq

class Solution:
    def findMaximizedCapital(self, k: int, initial_capital: int, profits: List[int], capital: List[int]) -> int:
        # 1, 4, 2, 3
        # 0, 3, 1, 1

        # (0,1), (1,2), (1,3), (4,3)

        # 2,3,1,5,3
        # 4,4,2,3,3

        # (2,1), (3,5), (3,3), (4,2), (4,3)

        projects = []
        h = []
        ans = 0

        for profit, cap in zip(profits, capital):
            projects.append((cap, profit))

        projects.sort()
        index = 0

        while k > 0:
            while index < len(projects):
                if projects[index][0] <= initial_capital:
                    heapq.heappush(h, -projects[index][1])
                    index+=1
                else:
                    break
            
            # print(h, "at initial_capital", initial_capital)
            if not h:
                break

            max_profit = -heapq.heappop(h)
            # print(max_profit)
            initial_capital += max_profit 
            ans += max_profit 
            k-=1

        return initial_capital

        