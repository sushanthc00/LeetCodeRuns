package main

import "fmt"

func subsetXORSum(nums []int) int {
	bitOr := 0

	for _, num := range nums {
		bitOr |= num
	}
	return bitOr * 1 << (len(nums) - 1)
}

func main() {
	nums := []int{5, 1, 6}
	fmt.Println(subsetXORSum(nums))
}
