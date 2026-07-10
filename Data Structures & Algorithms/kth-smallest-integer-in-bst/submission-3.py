# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def InOrder(self, root, k):
        if root == None:
            return

        self.InOrder(root.left, k)

        self.count+= 1
        if self.count == k:
            self.kthvalue = root.val
            return
        
        self.InOrder(root.right, k)

        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.count = 0
        self.InOrder(root, k)
        return self.kthvalue

