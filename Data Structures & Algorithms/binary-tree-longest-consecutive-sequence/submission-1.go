/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func dfs(root *TreeNode, path int, prev int, maxpath *int) {

	if root.Val == prev + 1 {
		path += 1
		*maxpath = max(path, *maxpath)
	} else {
		path = 1
	}

	if root.Left != nil {
		dfs(root.Left, path, root.Val, maxpath)
	}
	if root.Right != nil {
		dfs(root.Right, path, root.Val, maxpath)
	}
}

func longestConsecutive(root *TreeNode) int {

	path := 1
	maxpath := 1

	dfs(root, path, root.Val, &maxpath)

	return maxpath
}
