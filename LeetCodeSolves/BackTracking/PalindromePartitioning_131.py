#https://leetcode.com/problems/palindrome-partitioning/description/

def partition(s):
    def is_palindrome(val):
        return val == val[::-1]

    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            if is_palindrome(s[start:end]):
                path.append(s[start:end])
                backtrack(end, path)
                path.pop()

    result = []
    backtrack(0, [])
    return result


if __name__ == '__main__':
    s = "abba"
    print(partition(s))
