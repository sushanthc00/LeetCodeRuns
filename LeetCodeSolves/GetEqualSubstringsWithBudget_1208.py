def equalSubstring(s, t, maxCost):
    n = len(s)
    left = 0
    cost = 0
    max_len = 0

    for right in range(n):
        cost += abs(ord(s[right]) - ord(t[right]))

        while cost > maxCost:
            cost -= abs(ord(s[left]) - ord(t[left]))
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == '__main__':
    s = "abcd"
    t = "bcdf"
    maxCost = 3
    print(equalSubstring(s, t, maxCost))