def maskPii(s):
    if '@' in s:
        first, last = s.split('@')
        first = first.lower()
        last = last.lower()
        masked_email = first[0] + '*****' + first[-1] + '@' + last
        return masked_email

    else:
        digits = ''.join(filter(str.isdigit, s))
        local = digits[-10:]
        country_code = digits[:-10]
        print(local)
        print(country_code)

        if len(country_code) == 0:
            return '***-***-' + local[-4:]
        elif len(country_code) == 1:
            return '+*-***-***-' + local[-4:]
        if len(country_code) == 2:
            return '+**-***-***-' + local[-4:]
        if len(country_code) == 3:
            return '+***-***-***-' + local[-4:]


if __name__ == '__main__':
    s = "121(234)567-890"
    print(maskPii(s))
