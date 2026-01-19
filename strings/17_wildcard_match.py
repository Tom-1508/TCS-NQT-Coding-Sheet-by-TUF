def wildcard_match(text, pattern):
    i = 0  # text pointer
    j = 0  # pattern pointer
    star_idx = -1
    match_idx = 0

    while i < len(text):

        # Case 1: match or '?'
        if j < len(pattern) and (pattern[j] == text[i] or pattern[j] == '?'):
            i += 1
            j += 1

        # Case 2: '*'
        elif j < len(pattern) and pattern[j] == '*':
            star_idx = j
            match_idx = i
            j += 1

        # Case 3: mismatch but we had a previous '*'
        elif star_idx != -1:
            j = star_idx + 1
            match_idx += 1
            i = match_idx

        # Case 4: mismatch and no '*'
        else:
            return False

    # skip remaining '*' in pattern
    while j < len(pattern) and pattern[j] == '*':
        j += 1

    return j == len(pattern)


print(wildcard_match("abcd", "a?cd"))  # True
print(wildcard_match("abcd", "a*d"))   # True
print(wildcard_match("abcd", "a*c"))   # False
print(wildcard_match("aa", "*"))       # True
print(wildcard_match("aa", "a"))       # False
print(wildcard_match("aa", "a*"))      # True