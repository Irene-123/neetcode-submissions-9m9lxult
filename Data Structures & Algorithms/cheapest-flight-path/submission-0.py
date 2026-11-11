import heapq as hq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        cheapest_price = [[float('inf')] * (k + 2) for _ in range(n)]

        for flight in flights:
            s, d, cost = flight[0], flight[1], flight[2]
            graph[s].append((d, cost))

        pq = [(0, src, 0)]
        cheapest_price[src][0] = 0
        
        while pq:
            curr_cost, s, flights_taken = hq.heappop(pq)
            if s == dst:
                return curr_cost

            for node in graph[s]:
                next_dst, dst_cost = node[0], node[1]
                next_flights = flights_taken + 1
                next_cost = curr_cost + dst_cost    
                
                if next_flights <= k+1 and next_cost < cheapest_price[next_dst][next_flights]:
                    cheapest_price[next_dst][next_flights] = next_cost
                    hq.heappush(pq, (next_cost, next_dst, next_flights))

        if all(price == float('inf') for price in cheapest_price[dst]):
            return -1
        return min(cheapest_price[dst])


        

        
        