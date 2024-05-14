def productExceptSelf(nums):
    n = len(nums)

    result = [0] * n

    result[0] = 1
    for i in range(1, n):
        result[i] = result[i-1] * nums[i - 1]

    rightProduct = 1
    for i in range(n-1, -1, -1):
        result[i] *= rightProduct
        rightProduct *= nums[i]

    return result


if __name__ == '__main__':
    nums = [1,2,3,4]
    print(productExceptSelf(nums))