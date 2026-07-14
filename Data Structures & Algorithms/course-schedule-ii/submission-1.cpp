class Solution {
public:
    vector<int>ans;
    vector<bool> visited;
    vector<bool>path;
    unordered_map<int, vector<int>> courseMap;

    bool dfs(int i) {

        path[i] = true;
        visited[i] = true;

        for (const auto& course: courseMap[i]) {

            if (path[course])
                return false;

            if (visited[course]) 
                continue;


            if (!dfs(course))
                return false;
        }

        ans.push_back(i);
        path[i] = false;
        return true;
    }
    vector<int> findOrder(int n, vector<vector<int>>& prerequisites) {
        visited.resize(n, false);
        path.resize(n, false);

        for (const auto& pre: prerequisites) {

            courseMap[pre[0]].push_back(pre[1]);
        }

        for (int i = 0; i < n; i++) {

            if (!visited[i] and !dfs(i))
                return vector<int> {};
            
        }
        return ans;
    }
};
