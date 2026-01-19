def remove_duplicates(s):
    seen = set()
    result = ""
    
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result += ch
    return result

print(remove_duplicates("aabbccdd"))     # abcd
print(remove_duplicates("programming"))  # progamin