class Solution {
public:
    vector<vector<int>> dp;
    int burst(vector<int>&nums, int l, int r) {

        int ans = 0;

        if (dp[l][r] != -1) return dp[l][r];
        
        for (int i = l+1; i < r; i++) {
            int temp = nums[l]*nums[i]*nums[r] + burst(nums, l, i) + burst(nums, i, r);
            ans = max(ans, temp);
        }
        
        return dp[l][r] = ans;    
    }
    int maxCoins(vector<int>& nums) {
        
        nums.insert(nums.begin(), 1);
        int n = nums.size();
        nums.push_back(1);
        dp.resize(n+2, vector<int>(n+2, -1));
        return burst(nums, 0, nums.size()-1);
    }
};
