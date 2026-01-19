def print_duplicates(s):
    freq={}
    for ch in s:
        freq[ch] = freq.get(ch,0)+1
        
    result = []
    for ch, count in freq.items():
        if count > 1:
            result.append(ch)
    return result


print(print_duplicates("aabbcdd"))   # ['a', 'b', 'd']
print(print_duplicates("abcd"))      # []