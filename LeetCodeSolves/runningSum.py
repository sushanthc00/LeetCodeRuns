def runningSum(nums):
    n = len(nums)
    res = [nums[0]]

    for i in range(1, n):
        res.append(nums[i] + res[i - 1])
    return res


def updateArray(nums):
    n = len(nums)

    for i in range(1, n):
        nums[i] += nums[i - 1]
    return nums


if __name__ == "__main__":
    nums = [1, 5, 67, 44, 22, 3, 0, 12]
    # print(runningSum(nums))
    print(updateArray(nums))
