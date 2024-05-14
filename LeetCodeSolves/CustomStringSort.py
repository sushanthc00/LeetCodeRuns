def customStringSort(order, s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    sorted_s = ""
    for char in order:
        if char in char_count:
            sorted_s += char_count[char] * char
            del char_count[char]

    for char in char_count:
        sorted_s += char * char_count[char]

    return sorted_s

if __name__ == '__main__':

    order = "dbac"
    s = "adddbanmaw"
    print(customStringSort(order,s))