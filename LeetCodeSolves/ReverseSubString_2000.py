def reverseSubstring(word, ch):
    idx = word.find(ch)

    if idx == -1:
        return word

    return word[:idx + 1][::-1] + word[idx + 1:]


if __name__ == '__main__':
    word = "abcdefd"
    ch = "d"
    print(reverseSubstring(word, ch))
