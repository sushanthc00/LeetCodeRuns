def minSumFallingPath(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]

    for i in range(n - 2, -1, -1):
        for j in range(n):
            down = matrix[i + 1][j]
            down_left = matrix[i + 1][j - 1] if j - 1 >= 0 else float('inf')
            down_right = matrix[i + 1][j + 1] if j + 1 < n else float('inf')

            matrix[i][j] += min(down, down_right, down_left)

    return min(matrix[0])


if __name__ == '__main__':
    matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
    print(minSumFallingPath(matrix))
