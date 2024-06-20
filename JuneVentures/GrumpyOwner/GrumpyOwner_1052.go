package main

import "fmt"

func maxSatisfied(customers []int, grumpy []int, minutes int) any {
	n := len(customers)
	totalSatisfied := 0
	currentAdditional := 0
	maxAdditional := 0

	for i := 0; i < n; i++ {
		if grumpy[i] == 0 {
			totalSatisfied += customers[i]
		}
	}

	for i := 0; i < n; i++ {
		currentAdditional += customers[i] * grumpy[i]
		if i >= minutes {
			currentAdditional -= customers[i-minutes] * grumpy[i-minutes]
		}
		if maxAdditional < currentAdditional {
			maxAdditional = currentAdditional
		}
	}
	return maxAdditional + totalSatisfied
}

func main() {
	customers := []int{1, 0, 1, 2, 1, 1, 7, 5}
	grumpy := []int{0, 1, 0, 1, 0, 1, 0, 1}
	minutes := 3
	fmt.Println(maxSatisfied(customers, grumpy, minutes))
}
