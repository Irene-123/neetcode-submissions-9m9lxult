class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        self.indegree = [0]*n
        vertices = []

        for s, d in edges:
            self.indegree[d] += 1

        for i in range(n):
            if self.indegree[i] == 0:
                vertices.append(i)

        return vertices

        

        