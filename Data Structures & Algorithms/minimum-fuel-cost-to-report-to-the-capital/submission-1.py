class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        graph = defaultdict(list) 
        indegree = [0]*n
        passengers = [1]*n
        fuel = 0

        for s, d in roads:
            graph[s].append(d)
            graph[d].append(s)
            indegree[s] += 1
            indegree[d] += 1
        
        q = deque()
        for i in range(1, n): # Put Leaf Nodes in the Queue
            if indegree[i] == 1:
                q.append(i)
        
        while q:
            node = q.popleft()
            fuel += math.ceil(passengers[node]/seats)

            for parent in graph[node]:
                indegree[parent] -= 1
                if indegree[parent] == 1 and parent != 0:
                    q.append(parent)
                passengers[parent] += passengers[node]

        return fuel               


