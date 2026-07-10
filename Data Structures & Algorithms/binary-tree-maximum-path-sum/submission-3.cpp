/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int dfs(TreeNode* root, int &ans, int maxsum) {

        if (root == NULL) return 0;

        int leftsum = max(dfs(root->left, ans, maxsum), 0);
        int rightsum = max(dfs(root->right, ans, maxsum), 0);

        
        int throughRoot = root->val + leftsum + rightsum;
        ans = max(ans, throughRoot);

        maxsum = root->val + max(leftsum, rightsum);
        return maxsum;        
    }
    int maxPathSum(TreeNode* root) {

        if (root == NULL) return 0;

        int ans = INT_MIN;
        int maxsum = 0;

        dfs(root, ans, maxsum);

        return ans;
    }
};
