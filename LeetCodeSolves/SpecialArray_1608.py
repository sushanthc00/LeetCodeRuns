from bisect import bisect_left


def specialArray(nums):
    nums.sort()
    n = len(nums)

    for x in range(1, n + 1):
        count = n - bisect_left(nums, x)

        if count == x:
            return x

    return -1


if __name__ == '__main__':
    nums = [6, 7, 4]
    print(specialArray(nums))
