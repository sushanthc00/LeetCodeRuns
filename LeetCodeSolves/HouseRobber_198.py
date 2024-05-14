def robHouse(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

    return dp[-1]


def rob(nums):
    def rob_linear(houses):
        prev, curr = 0, 0
        for amount in houses:
            prev, curr = curr, max(prev + amount, curr)
        return curr

    if len(nums) <= 1:
        return nums[0] if nums else 0
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


if __name__ == '__main__':
    nums = [2, 1, 1, 2]
    print(robHouse(nums))
    print(rob(nums))
