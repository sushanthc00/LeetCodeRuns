package main

import "fmt"

func countTriplets(arr []int) int {
	N := len(arr)
	res := 0
	for i := 0; i < N-1; i++ {
		currXor := arr[i]
		for k := i + 1; k < N; k++ {
			currXor ^= arr[k]
			if currXor == 0 {
				res += k - i
			}
		}
	}
	return res
}

func main() {
	arr := []int{1, 1, 1, 1, 1}
	fmt.Println(countTriplets(arr))
}
