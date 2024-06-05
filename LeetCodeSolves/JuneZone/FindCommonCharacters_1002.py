from collections import Counter


def commonChars(words):
    count = Counter(words[0])

    for word in words:
        current_word = Counter(word)

        for char in list(count):
            count[char] = min(count[char], current_word[char])

    common_char = []
    for char, count in count.items():
        common_char.extend([char] * count)
    return common_char


if __name__ == '__main__':
    words = ["bella", "label", "roller"]
    print(commonChars(words))
