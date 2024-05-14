def findPivot(n):
    for i in range(1, n+1):
        left_sum = i * (i+1) // 2
        right_sum = (n * (n+1) // 2) - (i * (i-1) // 2)

        if left_sum == right_sum:
            return i
    return -1


if __name__ == '__main__':
    n = 8
    print(findPivot(n))

