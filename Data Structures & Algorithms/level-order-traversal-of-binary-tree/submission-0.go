/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func levelOrder(root *TreeNode) [][]int {
    
    res := [][]int{}

    if root == nil {
        return res
    }
    q := []*TreeNode{root}

    for len(q) > 0{

        level := []int{}
        n := len(q)

        for i := 0; i < n; i++{

            node := q[i]
            level = append(level, node.Val)

            if node.Left != nil {
                q = append(q, node.Left)
            }
            if node.Right != nil {
                q = append(q, node.Right)
            }
        }
        q = q[n:]
        res = append(res, level)

        
    }

    return res
}
