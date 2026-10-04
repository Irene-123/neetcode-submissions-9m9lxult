/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func dfs(root *TreeNode, maxpath *int) (int, int) {

    if root == nil {
        return 0, 0 
    }

    inc, dec := 1, 1

    leftInc, leftDec := dfs(root.Left,  maxpath)
    rightInc, rightDec := dfs(root.Right, maxpath)

    if root.Left != nil {
        
        if root.Left.Val == root.Val + 1 {
            inc = max(inc, leftInc + 1)
        }
        if root.Left.Val == root.Val - 1{
            dec = max(dec, leftDec + 1)
        }

    }
    if root.Right != nil {
        
        if root.Right.Val == root.Val + 1{
            inc = max(inc, rightInc + 1)
        }
        if root.Right.Val == root.Val - 1 {
            dec = max(dec, rightDec + 1)
        }
    }
    path := inc + dec - 1

    if path > *maxpath {
        *maxpath = path
    }

    return inc, dec
}

func longestConsecutive(root *TreeNode) int {

    if root == nil {
        return 0
    }
    maxpath := 1
    dfs(root, &maxpath)
    return maxpath
}
