package main

import (
	"fmt"
)

func relativeArraySort(arr1 []int, arr2 []int) any {
	maxElement := 0
	for _, num := range arr1 {
		if num > maxElement {
			maxElement = num
		}
	}
	count := make([]int, maxElement+1)

	for _, element := range arr1 {
		count[element]++
	}

	result := make([]int, 0, len(arr1))
	for _, value := range arr2 {
		for count[value] > 0 {
			result = append(result, value)
			count[value]--
		}
	}

	for num := 0; num < len(count); num++ {
		for count[num] > 0 {
			result = append(result, num)
			count[num]--
		}
	}
	return result
}

func main() {
	arr1 := []int{2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19}
	arr2 := []int{2, 1, 4, 3, 9, 6}
	fmt.Println(relativeArraySort(arr1, arr2))
}
