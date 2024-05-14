def isPalindrome(x: int) -> bool:

    if x < 0:
        return False

    original_x = x
    reversed_x = 0

    while x > 0:
        reminder = x % 10
        reversed_x = reversed_x * 10 + reminder
        x = x // 10

    return original_x == reversed_x


if __name__ == '__main__':
    x = 115225110
    print(isPalindrome(x))
