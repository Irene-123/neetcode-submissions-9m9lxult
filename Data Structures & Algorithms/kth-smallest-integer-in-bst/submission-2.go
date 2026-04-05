/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 func traverse(root *TreeNode, stack *[]int) {

    if root == nil {
        return
    }

    traverse(root.Left, stack)
    *stack = append(*stack, root.Val)
    traverse(root.Right, stack)
 }

func kthSmallest(root *TreeNode, k int) int {

    var stack []int
    
    traverse(root, &stack)

    return stack[k-1]

    
}
