class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        queue<pair<int, int>> q;
        int minutes = 0;
        int rows = grid.size();
        int cols = grid[0].size();
        int fresh_fruits = 0;
        int dRow[] = { -1, 1, 0, 0 }; 
        int dCol[] = { 0, 0, -1, 1 };

        // Count fresh fruits and add rotten to queue
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 2) {
                    q.push({i, j});
                }
                else if (grid[i][j] == 1) fresh_fruits++;
            }
        }
        
        if (fresh_fruits == 0) return 0;  // No fresh fruits, return 0

        // BFS level by level
        while (!q.empty() && fresh_fruits > 0) {
            int size = q.size();  // Process all currently rotten fruits
            for (int k = 0; k < size; k++) {
                auto curr = q.front(); 
                q.pop();
                int x = curr.first;
                int y = curr.second;

                for (int i = 0; i < 4; i++) {
                    int dx = x + dRow[i];
                    int dy = y + dCol[i];

                    if (dx < 0 || dy < 0 || dx >= rows || dy >= cols || 
                        grid[dx][dy] != 1) 
                        continue;
                    
                    grid[dx][dy] = 2;  // Mark as rotten
                    fresh_fruits--;
                    q.push({dx, dy});
                }
            }
            minutes++;  // Increment after processing a level
        }

        return fresh_fruits == 0 ? minutes : -1;
    }
};