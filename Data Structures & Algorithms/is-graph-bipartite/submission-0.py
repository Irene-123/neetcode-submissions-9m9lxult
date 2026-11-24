class Solution:
    def dfs(self, node, flag):
        self.group[node] = flag

        flag = not flag

        for nei in self.graph[node]:
            if self.group[nei] != -1:
                if self.group[nei] != flag:
                    return False
                continue
            
            self.group[nei] = flag 
            self.dfs(nei, flag)
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        # Divide the graph in 2 groups, such that each edge's both endpoints are in different groups 
        n = len(graph)
        self.group = [-1]*n
        self.graph = graph
        flag = 0
        
        for node in range(n):
            if self.group[node] == -1:
                if not self.dfs(node, flag):
                    return False

        return True



