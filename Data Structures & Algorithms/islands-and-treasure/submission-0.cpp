class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {

        queue<pair<int, int>> q; 
        int dRow[] = { -1, 1, 0, 0 }; 
        int dCol[] = { 0, 0, -1, 1 };
        int n = grid.size();
        int m = grid[0].size();
        

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 0){
                    q.push({i,j});
                }
            }
        }

        while (!q.empty()) {

            auto curr = q.front(); 
            q.pop();
            int x= curr.first;
            int y = curr.second;

            for (int i = 0; i < 4; i++) {
                int dx = x + dRow[i];
                int dy = y + dCol[i];

                if (dx < 0 or dy < 0 or dx >= n or dy >= m or grid[dx][dy] != INT_MAX) 
                    continue;

                grid[dx][dy] = grid[x][y]+1;
                q.push({dx,dy});
                
            }
        }
        
    }

};
