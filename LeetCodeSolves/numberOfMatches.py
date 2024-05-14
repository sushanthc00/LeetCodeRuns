def numOfMatches(n):
    num = 0
    while n != 1:
        if n % 2 == 0:
            num += n / 2
            n = n / 2

        else:
            num += (n - 1) / 2
            n = (n - 1) / 2 + 1

    return int(num)


if __name__ == '__main__':
    n = 200
    print(numOfMatches(n))
