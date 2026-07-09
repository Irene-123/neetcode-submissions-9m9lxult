class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        
        int ans = 0;
        int cycle = n + 1;
        priority_queue<int> pq;
        vector<int>count(26, 0);

        for (char task: tasks) {
            count[task - 'A']++;
        }

        for (int cnt: count) {
            if (cnt > 0) {
                pq.push(cnt);
            }
        }
        

        while (!pq.empty()) {

            int time = 0;
            vector<int> tmp;

            for (int i = 0; i < cycle and !pq.empty(); i++) {
                int curr = pq.top();
                time++;
                pq.pop();
                if (curr - 1 > 0)
                    tmp.push_back(curr-1);
            }

            for (auto t: tmp) {
                pq.push(t);
            }
            ans += (pq.empty()) ? time : cycle;
        }
        return ans;

    }
};