class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        
        vector<int> res;
        int n = nums.size();
        priority_queue<pair<int, int>> pq;

        for (int i = 0; i < k; i++)
            pq.push({nums[i], i});

        res.push_back(pq.top().first);

        for (int i = k; i < n; i++) {

            pq.push({nums[i], i});
            int curr_max = INT_MIN;

            while (!pq.empty()) {
                pair<int, int> p = pq.top();
                int num = p.first;
                int prev_i = p.second;

                // cout<<num << " "<< prev_i<<endl;

                if (prev_i <= i - k) {
                    cout<<"Removing prev_i "<<prev_i<<" for i "<<i<<endl;
                    pq.pop();
                }
                else {
                    break;
                }
            }

            if (pq.size() > 0) {
                curr_max = pq.top().first;
                // pq.pop();
            }
            res.push_back(curr_max);
        }

        return res;
    }
};
