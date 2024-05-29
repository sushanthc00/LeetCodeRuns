package main

import "fmt"

func numSteps(s string) int {
	n := len(s)
	steps := 0
	carry := 0

	for i := n - 1; i > 0; i-- {
		digit := (int(s[i]) + carry) % 2

		if digit == 0 {
			steps += 1
		} else {
			carry = 1
			steps += 2
		}
	}
	return steps + carry
}

func main() {
	s := "100100001000"
	fmt.Println(numSteps(s))
}
