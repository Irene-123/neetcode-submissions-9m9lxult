# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recurse(self,root):
        if not root:
            return True, 0, float('inf'), float('-inf')
        
        lbst, lsize, lmin, lmax = self.recurse(root.left)
        rbst, rsize, rmin, rmax = self.recurse(root.right)

        if lbst and rbst and lmax < root.val < rmin:
            minimum = min(root.val, lmin)
            maximum = max(root.val, rmax)
            self.ans = max(self.ans, lsize + rsize + 1)
            return True, lsize + rsize + 1, minimum, maximum
        
        self.ans = max(self.ans, lsize, rsize)

        return False, 0, 0, 0


    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.recurse(root)
        return self.ans

