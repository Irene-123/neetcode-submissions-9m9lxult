# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lca(self, parent, proot, qroot, p, q):
        if proot.val == p.val and qroot.val == q.val:
            return parent
        
        if root.val > p.val:
            proot = root.left
        else:
            proot = root.right

        if root.val > q.val:
            qroot = root.left
        else:
            qroot = root.right

        return self.lca(parent, proot, qroot, p, q)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None 

        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
