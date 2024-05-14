def numSubarrayWithSum(nums, goal):
    count = 0
    current_sum = 0
    prefix_sum_count = {0: 1}

    for num in nums:
        current_sum += num
        if current_sum - goal in prefix_sum_count:
            count += prefix_sum_count[current_sum - goal]
        if current_sum in prefix_sum_count:
            prefix_sum_count[current_sum] += 1
        else:
            prefix_sum_count[current_sum] = 1

    return count

if __name__ == '__main__':
    nums = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    goal = 0
    print(numSubarrayWithSum(nums, goal))
