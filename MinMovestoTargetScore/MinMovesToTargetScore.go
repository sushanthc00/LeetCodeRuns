package main

import "fmt"

func minMoves(target int, maxDoubles int) int {
	count := 0

	for target > 1 && maxDoubles > 0 {
		if target%2 != 0 {
			count += 1
			target -= 1
		} else {
			target /= 2
			count += 1
			maxDoubles -= 1
		}
	}
	count += target - 1
	return count
}

func main() {
	target := 19
	maxDoubles := 2
	fmt.Println(minMoves(target, maxDoubles))
}
