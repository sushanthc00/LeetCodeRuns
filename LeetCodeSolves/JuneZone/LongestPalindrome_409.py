from collections import Counter

def longestPalindrome(s):
    count = Counter(s)
    ans = 0
    for val in count.values():
        ans += val - (val & 1)
        ans += (ans & 1 ^ 1) and (val & 1)
    return ans


if __name__ == '__main__':
    s = "abccccdd"
    print(longestPalindrome(s))