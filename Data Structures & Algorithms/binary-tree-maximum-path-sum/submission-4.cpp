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
    int dfs(TreeNode* root, int &maxsum) {

        if (!root) return 0;

        int leftsum = max(0, dfs(root->left, maxsum));
        int rightsum = max(0, dfs(root->right, maxsum));

        int pathsum = leftsum + root->val + rightsum;

        maxsum = max(maxsum, pathsum);

        return root->val + max(leftsum, rightsum); 
    }
    int maxPathSum(TreeNode* root) {
        
        int maxsum = INT_MIN;
        int pathsum = INT_MIN;

        if (!root) return 0;

        dfs(root, maxsum);

        return maxsum;
    }
};
