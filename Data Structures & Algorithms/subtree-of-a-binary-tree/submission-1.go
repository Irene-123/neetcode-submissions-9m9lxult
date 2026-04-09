/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func dfs(root *TreeNode, subRoot *TreeNode) bool {

    if (root == nil && subRoot == nil) {
        return true
    }

    if (root == nil || subRoot == nil) {
        return false
    }

    if (root.Val != subRoot.Val){
        return false
    } 

    return dfs(root.Left, subRoot.Left) && dfs(root.Right, subRoot.Right)
}

func isSubtree(root *TreeNode, subRoot *TreeNode) bool {

    if (subRoot == nil){
        return true
    }

    if (root == nil) {
        return false
    }

    if (dfs(root, subRoot)) {
        return true
    }


    return isSubtree(root.Left, subRoot) || isSubtree(root.Right, subRoot)
    
}
