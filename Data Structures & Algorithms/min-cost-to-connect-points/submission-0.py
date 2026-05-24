class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = collections.defaultdict(list)
        visit = set()
        res = 0

        for i in range(n):
            for j in range(i+1, n):
                xi, yi, xj, yj = points[i][0], points[i][1], points[j][0], points[j][1]

                manhattan = abs(xi-xj) + abs(yi - yj)
                adj[i].append([j, manhattan])
                adj[j].append([i, manhattan])

        minHeap = [(0, 0)]
        
        while len(visit) < n:
            curr_dist, node = heapq.heappop(minHeap) 
            if node in visit: # tells that this node is now connected
                continue
            res += curr_dist
            visit.add(node)

            # print(adj[node])
            # print(visit)

            for nextNode, dist in adj[node]:
                if nextNode not in visit:
                    heapq.heappush(minHeap, (dist, nextNode))


        return res
        