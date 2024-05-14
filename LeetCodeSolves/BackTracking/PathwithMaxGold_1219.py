def getMaximumGold(grid):
    rows, cols = len(grid), len(grid[0])
    max_gold = 0

    def dfs(x, y, curr_gold):
        nonlocal max_gold
        if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == 0:
            max_gold = max(max_gold, curr_gold)
            return

        original_grid = grid[x][y]
        grid[x][y] = 0
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for dx, dy in directions:
            dfs(x + dx, y + dy, original_grid + curr_gold)
        grid[x][y] = original_grid

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0:
                dfs(i, j, 0)

    return max_gold


if __name__ == '__main__':
    grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
    print(getMaximumGold(grid))
