def findLongestss(s, k):
    dp = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

    for char in s:
        max_length = 0

        for i in range(max(ord(char) - k, ord('a')), min(ord(char) + k + 1, ord('z') + 1)):
            prev_char = chr(i)
            max_length = max(max_length, dp[prev_char])

        dp[char] = max_length + 1
    return max(dp.values())


if __name__ == '__main__':
    s = "acfgbd"
    k = 2
    print(findLongestss(s, k))
