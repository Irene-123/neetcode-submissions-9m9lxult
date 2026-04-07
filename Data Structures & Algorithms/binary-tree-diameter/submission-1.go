/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func diameter(root *TreeNode, d *int) int{
	if root == nil{
		return 0
	}

	left := diameter(root.Left, d)
	right := diameter(root.Right, d)

	*d = max(*d, left+right) 

	return 1+ max(left, right)
}

func diameterOfBinaryTree(root *TreeNode) int {

	var d = 0

	diameter(root, &d)
	return d
    
}
