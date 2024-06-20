package main

import (
	"fmt"
	"sort"
)

func maxDistance(position []int, m int) int {
	sort.Ints(position)

	last := position[len(position)-1]
	left, right := 1, last-position[0]
	for left <= right {
		mid := left + (right-left)/2
		if canPlaceBalls(position, mid, m) {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return right
}

func canPlaceBalls(position []int, minDist int, m int) bool {
	count := 1
	lastPosition := position[0]

	for i := 1; i < len(position); i++ {
		if position[i]-lastPosition >= minDist {
			count += 1
			lastPosition = position[i]
			if count == m {
				return true
			}
		}
	}
	return false
}

func main() {
	position := []int{1, 4, 2, 3, 7}
	m := 3
	fmt.Println(maxDistance(position, m))
}
