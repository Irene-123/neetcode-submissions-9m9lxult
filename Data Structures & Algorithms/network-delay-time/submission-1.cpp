class Solution {
public:
    unordered_map<int, vector<pair<int, int>>> adj;
    vector<int> ans;
    priority_queue<pair<int, int>, vector<pair<int, int>>,greater<pair<int, int>>> pq;

    int networkDelayTime(vector<vector<int>>& times, int n, int k) {

        ans.assign(n+1, INT_MAX);
        

        for (const auto &time: times) {

            int u = time[0], v = time[1], t = time[2];
            adj[u].push_back({v, t});
        }

        ans[k] = 0;
        ans[0] = 0;
        pq.push({0, k});

        while (!pq.empty()) {

            auto p = pq.top();
            int i_reached_here_at = p.first, curr = p.second;
            pq.pop();

            if (i_reached_here_at > ans[curr]) continue;

            for (const auto &nextnode : adj[curr]) {

                int v1 = nextnode.first, t1 = nextnode.second;

                if (ans[v1] > t1 + i_reached_here_at) {
                    ans[v1] = t1 + i_reached_here_at;
                    pq.push({t1 + i_reached_here_at, v1});
                }
                
            }
        }

        int res = INT_MIN;

        for (const auto&a: ans) {
            if (a == INT_MAX) return -1;

            res = max(res, a);
        }
        return res;



    }
};
