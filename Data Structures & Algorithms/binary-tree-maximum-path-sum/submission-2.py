# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recurse(self, root):
        if root == None:
            return 0

        leftsum = max(self.recurse(root.left), 0)
        rightsum = max(self.recurse(root.right), 0)

        total = leftsum + rightsum
        # print("At root ", root.val)
        # print("LEFTSUM ", leftsum)
        # print("RIGHTSUM ", rightsum)
        
        self.max_sum = max(self.max_sum, total + root.val)

        return root.val + max(leftsum, rightsum)
        

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf') 
        self.recurse(root)
        return self.max_sum
        
        