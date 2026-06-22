class Solution {
public:
    vector<vector<int>> dp;
    vector<vector<bool>> visit;
    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
    int n;
    int dir[4][2] = {{0,1}, {1, 0}, {-1, 0}, {0, -1}};

    bool valid(int i, int j) {
        if (i < 0 or j < 0 or i >=n or j >=n) 
            return false;
        return true;
    }

    int swimInWater(vector<vector<int>>& grid) {
        
        n = grid.size();

        pq.push({0, 0, 0});
        visit.resize(n, vector<bool>(n, false));
        dp.resize(n, vector<int>(n, INT_MAX));

        while (!pq.empty()) {
            int min_elevation = INT_MAX;

            auto p = pq.top();
            pq.pop();
            int current_elevation = p[0], i = p[1], j = p[2];
            visit[i][j] = true;
    
            for (int k =0; k < 4; k++) {
                int di = i + dir[k][0];
                int dj = j + dir[k][1];

                if (!valid(di, dj))
                    continue;

                if (!visit[di][dj])
                    pq.push({grid[di][dj], di, dj});
                min_elevation = min(min_elevation, dp[di][dj]);
                
            } 
            // cout<<min_elevation<<endl;
            dp[i][j] = max(min_elevation, current_elevation);
            if (i == 0 and j == 0){
                dp[i][j] = grid[i][j];
            }
        }

        return dp[n-1][n-1];
    }
};
