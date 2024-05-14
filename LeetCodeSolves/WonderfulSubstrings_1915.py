def wonderfulSubstrings(word):

    if len(word) == 1:
        return word
    
    # Initialize a counter for the mask state, starting with the 0 state seen once
    mask_count = {0: 1}

    # Initialize answer and mask state
    wonderful_count = 0
    current_mask = 0

    # Iterate over the characters in the word
    for char in word:
        # Toggle the bit for the current character in the mask state
        current_mask ^= 1 << (ord(char) - ord('a'))

        # Add to the wonderful string count the number of times this mask state has been seen
        # This covers the case where the substring has an even count of all characters
        wonderful_count += mask_count.get(current_mask, 0)

        # Check all masks that differ by one bit, which correspond to having
        # exactly one character with an odd count
        for i in range(10):
            # Toggle the i-th bit to check for a previous state that would
            # complement the current state to make a wonderful substring
            wonderful_count += mask_count.get(current_mask ^ (1 << i), 0)

        # Increment the count for the current mask state
        mask_count[current_mask] = mask_count.get(current_mask, 0) + 1

    # Return the total count of wonderful substrings
    return wonderful_count


if __name__ == '__main__':
    word = "aba"
    print(wonderfulSubstrings(word))