package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func evaluateBoolTree(root *TreeNode) bool {
	if root == nil {
		return false
	}

	if root.Left == nil && root.Right == nil {
		return root.Val == 1
	}

	leftVal := evaluateBoolTree(root.Left)
	rightVal := evaluateBoolTree(root.Right)

	if root.Val == 2 {
		return leftVal || rightVal
	} else if root.Val == 3 {
		return leftVal && rightVal
	}
	return false
}

func main() {
	// Constructing the tree for the example [2,1,3,null,null,0,1]
	root := &TreeNode{Val: 2}
	root.Left = &TreeNode{Val: 1}
	root.Right = &TreeNode{Val: 3}
	root.Right.Left = &TreeNode{Val: 0}
	root.Right.Right = &TreeNode{Val: 1}

	fmt.Println(evaluateBoolTree(root)) // Output: true
}
