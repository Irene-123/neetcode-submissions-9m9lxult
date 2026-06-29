# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def max_depth(self, root):
        if root == None:
            return 0

        height = 1 + max(self.max_depth(root.left), self.max_depth(root.right))
        return height

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        left_depth = self.max_depth(root.left) 
        right_depth = self.max_depth(root.right)

        if abs(left_depth - right_depth) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)




