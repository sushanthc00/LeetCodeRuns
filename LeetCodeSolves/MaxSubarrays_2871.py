def maxSubarrays(nums):
    currentAnd = -1
    ans = 0

    for num in nums:
        if currentAnd == -1:
            currentAnd = num
        else:
            currentAnd &= num

        if currentAnd == 0:
            ans += 1
            currentAnd -= 1

    return max(1, ans)


if __name__ == '__main__':
    nums = [5, 7, 1, 3]
    print(maxSubarrays(nums))