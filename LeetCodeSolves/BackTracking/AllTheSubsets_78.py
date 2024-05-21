# https://leetcode.com/problems/subsets/description/

def subsets(nums):
    def helper(start, path):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])

            helper(i + 1, path)
            path.pop()

    res = []
    helper(0, [])
    return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(subsets(nums))
