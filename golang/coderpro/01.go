/*
Validate a Binary Search Tree
*/

package main

import "fmt"
import "math"

type Node struct {
	value int
	left  *Node
	right *Node
}

func isValidBST(node *Node, low, high int) bool {
	if node == nil {
		return true
	}

	return (node.value > low && node.value < high) && isValidBST(node.left, low, node.value) && isValidBST(node.right, node.value, high)
}

func main() {
	root := Node{4, nil, nil}
	root.left = &Node{3, nil, nil}
	root.right = &Node{5, nil, nil}

	if isValidBST(&root, math.MinInt64, math.MaxInt64) {
		fmt.Println("Valid")
	} else {
		fmt.Println("Invalid")
	}

}
