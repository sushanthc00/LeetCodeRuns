package main

import "fmt"

func subsets(nums []int) [][]int {
	n := len(nums)
	total := 1 << n
	result := make([][]int, total)

	for i := 0; i < total; i++ {
		var subset []int
		for j := 0; j < n; j++ {
			if i&(1<<j) != 0 {
				subset = append(subset, nums[j])
			}
		}
		result[i] = subset
	}
	return result
}

func main() {
	nums := []int{1, 2, 3}
	fmt.Println(subsets(nums))
}
