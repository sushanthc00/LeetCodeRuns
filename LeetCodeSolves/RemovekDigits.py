def removeKdigits(num, k):
    if k == 0:
        return num

    arr = list(map(int, num))

    arr.sort()
    if k < len(num):
        arr = arr[:-k]
    else:
        []

    string = list(map(str, arr))
    result = ''.join(string)

    return result


if __name__ == '__main__':
    num = "1432219"
    k = 3
    print(removeKdigits(num, k))
