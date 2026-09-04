import collections
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        max_prob = [0]*n
        max_prob[start] = 1
        
        graph = collections.defaultdict(list)
        for edge, prob in zip(edges, succProb):
            graph[edge[0]].append((prob, edge[1]))
            graph[edge[1]].append((prob, edge[0]))

        # Graph 
        # 0 : (0.5, 1) , (0.2, 2)
        # 1: 2, 0
        # 2: 0, 1

        pq = []
        heapq.heappush(pq, (-1, start))

        while pq:
            curr_prob, node = heapq.heappop(pq)
            curr_prob = -curr_prob

            for prob, next in graph[node]:
                if max_prob[next] < prob*curr_prob:
                    max_prob[next] = prob*curr_prob
                    heapq.heappush(pq, (-max_prob[next], next))
                else:
                    continue 

        return max_prob[end]    