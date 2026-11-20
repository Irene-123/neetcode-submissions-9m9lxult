class Solution:
    def traverse(self, node, n): 
        # Find the distance to all nodes from node
        d = [-1]*n
        next = node 
        distance = 0

        while next != -1 and d[next] == -1:
            d[next] = distance 
            distance += 1
            next = self.edges[next]

        return d


    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        self.edges = edges
        distance = float('inf')
        closest_node = -1
        
        d1 = self.traverse(node1, n)
        d2 = self.traverse(node2, n)

        for i in range(n):
            if d1[i] != -1 and d2[i] != -1:
                if distance > max(d1[i], d2[i]):
                    distance = max(d1[i], d2[i])
                    closest_node = i
        
        return closest_node


