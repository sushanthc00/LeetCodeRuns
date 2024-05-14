char = 'z'
diff = (ord(char) - ord('a'))
total = 0
total ^= 1 << diff

print(diff)
print(total)
