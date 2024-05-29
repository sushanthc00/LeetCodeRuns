def numSteps(s):
    steps = 0
    carry = 0

    for i in reversed(range(1, len(s))):
        digit = (int(s[i]) + carry) % 2

        if digit == 0:
            steps += 1
        elif digit == 1:
            carry = 1
            steps += 2

    return steps + carry


if __name__ == '__main__':
    s = "100100001000"
    print(numSteps(s))