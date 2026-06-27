# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, left_boundary, right_boundary):
        if root == None:
            return True

        left_valid, right_valid = True, True 

        if root.left:
            if left_boundary < root.left.val < root.val:
                left_valid = self.dfs(root.left, left_boundary, root.val)
            else:
                left_valid = False

        if root.right:
            if root.val < root.right.val < right_boundary:
                right_valid = self.dfs(root.right, root.val, right_boundary)
            else:
                right_valid = False

        return left_valid and right_valid


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, -1001, 1002 )