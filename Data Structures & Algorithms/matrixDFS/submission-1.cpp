class Solution {
public:
    int n, m;
    vector<vector<int>> visited;
    int dir[4][2] = {
        {0, 1},   
        {1, 0},   
        {0, -1},  
        {-1, 0} 
    };
    int valid(int i, int j) {
        return (i >= 0 && j >= 0 && i < n && j < m);
    }
    int dfs(vector<vector<int>>& grid, int i, int j){

        if (i == n-1 and j == m-1) return 1;

        visited[i][j] = 1;
        int paths = 0;

        for (int k = 0; k < 4; k++) {

            int dx = dir[k][0] + i, dy = dir[k][1] + j;

            if (valid(dx, dy) and !visited[dx][dy] and grid[dx][dy] != 1) {
                paths += dfs(grid, dx, dy);
                visited[dx][dy] = 0;
            }  
        }
        
        return paths;
    }
    int countPaths(vector<vector<int>>& grid) {
        n = grid.size();
        m = grid[0].size();

        visited.resize(n, vector<int>(m,0));

        if (grid[0][0] == 1) return 0;

        return dfs(grid, 0,0);
    }
};
