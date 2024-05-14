from collections import deque


def maxSlidingWindow(nums, k):
    deq = deque()
    maxima = []

    for i in range(len(nums)):
        if deq and deq[0] < i - k + 1:
            deq.popleft()

        while deq and nums[deq[-1]] <= nums[i]:
            deq.pop()

        deq.append(i)

        if i >= k - 1:
            maxima.append(nums[deq[0]])

    return maxima


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(maxSlidingWindow(nums, k))
