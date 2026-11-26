class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        self.graph = defaultdict(list)
        self.indegree = [0]*n
        vertices = []

        for i in range(n):
            self.graph[i] = []

        for s, d in edges:
            self.graph[s].append(d)
            self.indegree[d] += 1

        for i in range(n):
            if self.indegree[i] == 0:
                vertices.append(i)

        return vertices

        

        