def islandPerimeter(grid):
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):

            if grid[row][col] == 1:
                perimeter += 4

                if row < rows - 1 and grid[row + 1][col] == 1:
                    perimeter -= 2
    
                if col < cols - 1 and grid[row][col + 1] == 1:
                    perimeter -= 2

    return perimeter


if __name__ == '__main__':
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    print(islandPerimeter(grid))
