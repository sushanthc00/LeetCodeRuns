package main

import (
	"fmt"
	"sort"
)

func specialArrays(nums []int) int {
	sort.Ints(nums)
	n := len(nums)

	for x := 1; x <= n; x++ {
		index := sort.SearchInts(nums, x)

		count := n - index

		if count == x {
			return x
		}
	}
	return -1
}

func main() {
	nums := []int{7, 6, 3}
	fmt.Println(specialArrays(nums))
}
