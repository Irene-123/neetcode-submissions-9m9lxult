from collections import defaultdict
from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b, 1))  # a -> b points away from 0, needs flip
            graph[b].append((a, 0))  # walking b -> a against original edge, already fine

        count = 0
        stack = [(0, -1)]
        while stack:
            node, parent = stack.pop()
            for nei, cost in graph[node]:
                if nei != parent:
                    count += cost
                    stack.append((nei, node))
        return count