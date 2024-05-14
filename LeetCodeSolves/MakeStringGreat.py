def makeGood(s):
    stack = []
    for char in s:
        if stack and abs(ord(char) - ord(stack[-1])) == 32:
            stack.pop()
        else:
            stack.append(char)

    return ''.join(stack)


if __name__ == '__main__':
    s = "leEeetcode"
    print(makeGood(s))