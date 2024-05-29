def minMoves(target, maxDoubles):
    count = 0

    while maxDoubles != 0 and target != 1:
        if target % 2 == 0:
            target = target // 2
            count += 1
            maxDoubles -= 1
        else:
            target -= 1
            count += 1

    if target != 1:
        count += target - 1

    return count


if __name__ == '__main__':
    target = 19
    maxDoubles = 2
    print(minMoves(target, maxDoubles))
