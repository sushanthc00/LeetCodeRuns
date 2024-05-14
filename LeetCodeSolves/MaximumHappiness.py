def maximum_happiness(happiness, k):
    happiness.sort(reverse=True)
    ans = 0

    for i, x in enumerate(happiness[:k]):
        x -= i
        ans += max(x, 0)

    return ans


if __name__ == '__main__':
    happiness = [1, 2, 3, 7, 0, 12, 3, 4, 9]
    k = 5
    print(maximum_happiness(happiness, k))
