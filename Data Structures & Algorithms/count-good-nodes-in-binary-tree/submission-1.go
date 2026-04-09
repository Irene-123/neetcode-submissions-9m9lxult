/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func goodNodes(root *TreeNode) int {

	
	var dfs func(root *TreeNode, maxVal int) int
	dfs = func(root *TreeNode, maxVal int) int {

		if (root == nil) {
			return 0
		}

		res := 0 

		if root.Val >= maxVal {
			res = 1 
			maxVal = root.Val
		}

		res += dfs(root.Left, maxVal)
		res += dfs(root.Right, maxVal)

		return res

	}

	return dfs(root, root.Val)
}
