from math import isqrt


# https://leetcode.com/problems/perfect-squares/description/

def isPerfectSquare(x):
    s = isqrt(x)
    return s * s == x


def numSquares(n):
    if isPerfectSquare(n):
        return 1

    # Check if the number can be expressed as the sum of two squares
    for i in range(1, isqrt(n) + 1):
        if isPerfectSquare(n - i * i):
            return 2

    # Check if the number can be expressed as the sum of three squares
    while n % 4 == 0:
        n //= 4
    if n % 8 == 7:
        return 4

    return 3


# Example usage
if __name__ == '__main__':
    n = 15
    print(numSquares(n))  # Output: 2
