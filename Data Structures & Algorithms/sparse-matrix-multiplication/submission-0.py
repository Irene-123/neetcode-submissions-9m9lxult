class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, n = len(mat1), len(mat2[0])
        final = [[0]*n for _ in range(m)]
        k = len(mat1[0])

        for row in range(m):
            for col in range(n):
                for i in range(k):
                    final[row][col] += mat1[row][i] * mat2[i][col]
        return final


                
                