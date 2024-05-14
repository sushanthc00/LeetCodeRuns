package main

import (
	"fmt"
	"strconv"
	"strings"
)

func compareVersions(version1 string, version2 string) int {
	nums1 := strings.Split(version1, ".")
	nums2 := strings.Split(version2, ".")
	max_len := len(nums1)

	if len(nums2) > max_len {
		max_len = len(nums2)
	}

	for i := 0; i < max_len; i++ {
		v1, v2 := 0, 0
		if i < len(nums1) {
			v1, _ = strconv.Atoi(nums1[i])
		}
		if i < len(nums2) {
			v2, _ = strconv.Atoi(nums2[i])
		}

		if v1 > v2 {
			return 1
		} else if v1 < v2 {
			return -1
		}
	}
	return 0
}

func main() {
	version1 := "1.01"
	version2 := "1.001"
	result := compareVersions(version1, version2)
	fmt.Printf("Comparison result of %s and %s is: %d\n", version1, version2, result)
}
