class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [[1]]

        # ans = []

        for r in range(1, rowIndex+1):
            new_row = [1]*(r+1)

            for i in range(1,r):
                new_row[i] = row[-1][i-1] + row[-1][i]
            row.append(new_row)

        return row[-1]





        