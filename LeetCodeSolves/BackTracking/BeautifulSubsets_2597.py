from collections import Counter


def beautifulSubsetsFail(nums, k):
    def backtrack(start, path):
        if path:
            beautiful_subsets.append(path[:])

        for i in range(start, len(nums)):
            if not path or abs(path[-1] - nums[i]) != k:
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

    nums.sort()
    beautiful_subsets = []
    backtrack(0, [])
    return len(beautiful_subsets)


def beautifulSubsets(nums, k):
    def dfs(index):
        nonlocal beautiful_count
        if index >= len(nums):
            beautiful_count += 1
            return

        dfs(index + 1)

        if count[nums[index] + k] == 0 and count[nums[index] - k] == 0:
            count[nums[index]] += 1
            dfs(index + 1)
            count[nums[index]] -= 1

    beautiful_count = -1
    count = Counter()

    dfs(0)
    return beautiful_count


if __name__ == '__main__':
    nums = [10, 4, 5, 7, 2, 1]
    k = 3
    print(beautifulSubsets(nums, k))
