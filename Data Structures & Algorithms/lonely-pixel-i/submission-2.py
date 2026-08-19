class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        # (0,2), (1,1), (2,0)
        row_count, col_count = [], []
        ans = 0
        m, n = len(picture), len(picture[0])
        for row in picture:
            row_count.append(row.count('B'))
        
        for j in range(n):
            col = 0
            for i in range(m):
                if picture[i][j] == 'B':
                    col += 1
            col_count.append(col)
        
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B' and row_count[i] == 1 and col_count[j] == 1:
                    ans += 1

        return ans