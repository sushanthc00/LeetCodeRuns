# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

def countTriplets(arr):
    N = len(arr)
    res = 0
    for i in range(N - 1):
        curr_xor = arr[i]
        for k in range(i + 1, N):
            curr_xor ^= arr[k]
            if curr_xor == 0:
                res += (k - i)
    return res


if __name__ == '__main__':
    arr = [1, 1, 1, 1, 1]
    print(countTriplets(arr))
