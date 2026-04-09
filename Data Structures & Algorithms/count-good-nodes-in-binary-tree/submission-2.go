/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func goodNodes(root *TreeNode) int {

	count := 0 
	var dfs func(root *TreeNode, maxVal int)
	dfs = func(root *TreeNode, maxVal int) {

		if (root == nil) {
			return 
		}

		if root.Val >= maxVal {
			count++
			maxVal = root.Val
		}

		dfs(root.Left, maxVal)
		dfs(root.Right, maxVal)
	}

	dfs(root, root.Val)
	return count
}
