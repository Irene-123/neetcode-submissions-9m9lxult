/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// func merge(root1* TreeNode, root2 *TreeNode, root *TreeNode, dir int) {

// 	leftval := 0
// 	rightval := 0

// 	if root1 != nil {
// 		leftval = root1.Val
// 	}
// 	if root2 != nil {
// 		rightval = root2.Val
// 	}
// 	newNode := &TreeNode{Val: leftval + rightval}
// 	if dir == 0{
// 		root.Left = newNode
// 	} else {
// 		root.Right = newNode
// 	}

// 	merge(root1.Left, root2.Left, newNode, 0)
// 	merge(root1.Right, root2.Right, newNode ,1)

// }

func mergeTrees(root1 *TreeNode, root2 *TreeNode) *TreeNode {
	
	if root1 == nil {
		return root2
	}
	if root2 == nil {
		return root1
	}

	root1.Val += root2.Val
	root1.Left = mergeTrees(root1.Left, root2.Left)
	root1.Right = mergeTrees(root1.Right, root2.Right) 

	return root1

}
