import functools
from operator import xor


def minOperations(nums, k):
    return functools.reduce(xor, nums + [k]).bit_count()


def minimumOperations(nums, k):
    current_xor = functools.reduce(xor, nums)
    req_xor = current_xor ^ k

    return bin(req_xor).count('1')


if __name__ == '__main__':
    nums = [2, 1, 3, 4]
    k = 1
    print(minOperations(nums, k))
    print(minimumOperations(nums, k))
