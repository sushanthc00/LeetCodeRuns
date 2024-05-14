def deleteSimilarStrings(s):
    char = 0
    left, right = 0, len(s) - 1

    while left < right and s[left] == s[right]:
        char = s[left]
        while left <= right and s[left] == char:
            left += 1
        while left <= right and s[right] == char:
            right -= 1

    final_length = right - left + 1
    print(final_length)
    return final_length


if __name__ == "__main__":
    s = "beerb"
    deleteSimilarStrings(s)
