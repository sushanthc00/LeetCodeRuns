def soe(n):
    if n <= 2:
        return []

    prime = [True for _ in range(n)]
    p = 2
    while p*p < n:
        if prime[p]:
            for i in range( p*p, n, p):
                prime[i] = False
        p += 1

    primes = [p for p in range(2, n) if prime[p]]
    return primes


if __name__ == '__main__':
    n = 24
    print(soe(n))