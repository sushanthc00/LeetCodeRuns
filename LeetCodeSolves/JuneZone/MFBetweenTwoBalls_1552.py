def maxDistance(position, m):
    position.sort()

    def canPlaceBalls(min_dist):
        count = 1
        last_position = position[0]

        for i in range(1, len(position)):
            if position[i] - last_position >= min_dist:
                count += 1
                last_position = position[i]
                if count == m:
                    return True

        return False

    left, right = 1, position[-1] - position[0]
    while left <= right:
        mid = (left + right) // 2
        if canPlaceBalls(mid):
            left = mid + 1
        else:
            right = mid - 1

    return right


if __name__ == '__main__':
    position = [1, 2, 3, 4, 7]
    m = 3
    print(maxDistance(position, m))
