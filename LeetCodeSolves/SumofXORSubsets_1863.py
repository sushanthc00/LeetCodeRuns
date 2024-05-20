def subsetXORSum(nums):
    # https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/

    bit_or = 0

    for num in nums:
        bit_or |= num

    return bit_or * (1 << len(nums) - 1)


if __name__ == '__main__':
    nums = [3, 4, 5, 6, 7, 8]
    print(subsetXORSum(nums))
