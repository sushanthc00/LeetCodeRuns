def romanToInt(italy):
    roman = {'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000}

    res = 0

    for i in range(len(italy)):
        if i + 1 < len(italy) and roman[italy[i]] < roman[italy[i + 1]]:
            res -= roman[italy[i]]
        else:
            res += roman[italy[i]]
    return res

def romanToInteger(s):
    r = {'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000}
    res = 0
    i = 0

    while i < len(s):
        current_value = r[s[i]]
        if i+1 < len(s) and r[s[i]] < r[s[i + 1]]:
            res -= current_value
        else:
            res += current_value
        i += 1
    return res


if __name__ == '__main__':
    italy = "XIX"
    s = "MCIX"
    # print(romanToInt(italy))
    print(romanToInteger(s))