package main

import (
	"fmt"
	"sort"
)

func numRescueBoats(people []int, limit int) int {
	sort.Ints(people)
	left, right := 0, len(people)-1
	boats := 0

	for left <= right {
		if people[left]+people[right] <= limit {
			left += 1
		}
		right -= 1
		boats += 1
	}
	return boats
}

func main() {
	people := []int{1, 2}
	limit := 3
	fmt.Println(numRescueBoats(people, limit))

}
