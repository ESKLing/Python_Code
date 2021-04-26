def isValid(s):
    char_count = {}
    for char in list(s):
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    allowance = 1
    for char in char_count:
        if char_count[char] != char_count[list(s)[0]] and allowance != 0:
            if char_count[char] > char_count[list(s)[0]]:
                char_count[char] -= 1
                allowance -= 1
            else:
                char_count[list(s)[0]] -= 1
                allowance -= 1

    for char in char_count:
        if char_count[char] != char_count[list(s)[0]]:
            return False

    return True
