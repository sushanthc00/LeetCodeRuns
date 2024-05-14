package main

import "fmt"

func getMaximumGold(grid [][]int) int {
	rows := len(grid)
	if rows == 0 {
		return 0
	}
	cols := len(grid[0])
	maxGold := 0

	var dfs func(row, col, currGold int)
	dfs = func(row, col, currGold int) {
		if row < 0 || row >= rows || col < 0 || col >= cols || grid[row][col] == 0 {
			if currGold > maxGold {
				maxGold = currGold
			}
			return
		}

		gold := grid[row][col]
		grid[row][col] = 0

		directions := [][]int{{0, 1}, {0, -1}, {-1, 0}, {1, 0}}

		for _, dir := range directions {
			newRow, newCol := row+dir[0], col+dir[1]
			dfs(newRow, newCol, currGold+gold)
		}

		grid[row][col] = gold

	}

	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if grid[i][j] != 0 {
				dfs(i, j, 0)
			}
		}
	}
	return maxGold
}

func main() {
	grid := [][]int{
		{0, 6, 0},
		{5, 8, 7},
		{0, 9, 0},
	}
	fmt.Println("Maximum Gold Collected:", getMaximumGold(grid))
}
