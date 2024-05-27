package main

import (
	"fmt"
	"sort"
)

func assignCookies(g []int, s []int) int {
	sort.Ints(g)
	sort.Ints(s)
	child, cookie := 0, 0

	for child < len(g) && cookie < len(s) {
		if s[cookie] >= g[child] {
			child++
		}
		cookie++
	}
	return child
}

func main() {
	g := []int{1, 2, 3}
	s := []int{1, 1}
	fmt.Println(assignCookies(g, s))
}
