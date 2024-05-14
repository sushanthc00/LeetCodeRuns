import math


def numPrimeArrangements(n):
    def isPrime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def factorial(n):
        if n == 0:
            return 1
        return (n * factorial(n - 1)) % (10 ** 9 + 7)

    prime_count = sum(1 for i in range(1, n+1) if isPrime(i))
    non_prime_count = n - prime_count

    return (factorial(non_prime_count) * factorial(prime_count)) % (10**9 + 7)


if __name__ == '__main__':
    n = 8
    print(numPrimeArrangements(n))
