class Solution {
public:
    vector<bool> visit;
    vector<vector<int>> adj;
    unordered_set<int> cycle;
    int cyclestart;
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        
        int n = edges.size();
        adj.resize(n+1);

        for (const auto& edge: edges){
            int u = edge[0], v = edge[1];

            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        visit.resize(n+1, false);
        cyclestart = -1;
        dfs(1, -1);

        for (int i = n - 1; i >= 0; i--) {
            int u = edges[i][0], v = edges[i][1];

            if (cycle.count(u) && cycle.count(v)) {
                return {u, v};
            }
        }
        return {};
    }
private:
    bool dfs(int node, int parent) {
        
        if (visit[node]) {
            cyclestart = node;
            return true;
        }
        visit[node] = true;

        for (const auto& nextnode : adj[node]) {

            if (nextnode == parent) continue;

            if (dfs(nextnode, node)) {

                if (cyclestart != -1) cycle.insert(node);
                if (cyclestart == node) {
                    cyclestart = -1;
                }
                return true;

            }
        }
        return false;
    }
};

