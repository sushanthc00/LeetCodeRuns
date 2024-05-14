package main

import (
	"fmt"
	"sort"
)

func maxHappiness(happiness []int, k int) int {
	sort.Sort(sort.Reverse(sort.IntSlice(happiness)))
	ans := 0

	for i := 0; i < k; i++ {
		x := happiness[i] - i
		if x > 0 {
			ans += x
		}
	}
	return ans
}

func main() {
	happiness := []int{1, 2, 3}
	k := 2
	fmt.Println(maxHappiness(happiness, k))
}
