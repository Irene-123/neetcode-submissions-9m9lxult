from collections import deque

class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n, m = len(grid), len(grid[0])

        inf = 2147483647
        dir = [[0,1], [1, 0], [0, -1], [-1, 0]]
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            for k in range(4):
                dx, dy = i + dir[k][0], j + dir[k][1]
                if dx >=0 and dy >= 0 and dx < len(grid) and dy < len(grid[0]):
                    if grid[dx][dy] == inf:
                        grid[dx][dy] = grid[i][j] + 1
                        q.append((dx, dy))

        return
                    

                        


























        