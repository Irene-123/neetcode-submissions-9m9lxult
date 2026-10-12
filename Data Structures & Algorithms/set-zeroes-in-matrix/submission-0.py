from collections import deque

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        q = deque()
        visited = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]== 0:
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            visited.add((i,j))

            # print("Horizontal change")
            for index in range(len(matrix[0])):
                matrix[i][index] = 0

            for index in range(len(matrix)):
                matrix[index][j] = 0

        return

        