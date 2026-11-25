class Solution:
    def dfs(self, node):

        self.visited.add(node)
        total_nodes, degree_sum = 1, len(self.graph[node])

        for nei in self.graph[node]:
            if nei not in self.visited:
                n, d = self.dfs(nei)
                total_nodes += n
                degree_sum += d

        return total_nodes, degree_sum


    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        self.graph = defaultdict(list)
        self.visited = set()
        count = 0

        for i in range(n):
            self.graph[i] = []

        for s, d in edges:
            self.graph[s].append(d)
            self.graph[d].append(s)

        for i in range(n):
            if i not in self.visited:
                nodes, degree_sum = self.dfs(i)
                if nodes*(nodes-1) == degree_sum:
                    count += 1

        return count

        
        
        