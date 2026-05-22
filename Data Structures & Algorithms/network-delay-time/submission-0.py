class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list) 
        for u, v, w in times:
            adj[u].append([v, w])
        res = 0
        visit = set()
        minHeap = [(0, k)]

        while minHeap:
            w, v = heapq.heappop(minHeap)
            if v in visit:
                continue

            visit.add(v)
            res = w
            for v1, w1 in adj[v]:
                if v1 not in visit:
                    heapq.heappush(minHeap, (w1 + w, v1))      
        return res if len(visit) == n else -1

            
                


        