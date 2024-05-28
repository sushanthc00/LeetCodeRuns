package main

import (
	"fmt"
	"math"
)

func equalSubstring(s string, t string, maxCost int) int {
	left := 0
	cost := 0
	maxLen := 0
	n := len(s)

	for right := 0; right < n; right++ {
		cost += int(math.Abs(float64(s[right]) - float64(t[right])))

		for cost > maxCost {
			cost -= int(math.Abs(float64(s[left]) - float64(t[left])))
			left++
		}
		if right-left+1 > maxLen {
			maxLen = right - left + 1
		}
	}
	return maxLen
}

func main() {
	s := "abcd"
	t := "bcdf"
	maxCost := 3
	fmt.Println(equalSubstring(s, t, maxCost))

}
