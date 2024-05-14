package main

import (
	"fmt"
)

func maxSubArrays(nums []int) int {
	currentAnd := -1
	ans := 0

	for _, num := range nums {
		if currentAnd == -1 {
			currentAnd = num
		} else {
			currentAnd &= num
		}

		if currentAnd == 0 {
			ans++
			currentAnd = -1
		}
	}

	if ans == 0 {
		return 1
	}
	return ans
}

func main() {
	nums1 := []int{1, 0, 2, 0, 1, 2}
	nums2 := []int{5, 7, 1, 3}
	fmt.Println(maxSubArrays(nums1)) // Output: 3
	fmt.Println(maxSubArrays(nums2)) // Output: 1
}
