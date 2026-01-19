def char_frequency(s):
    freq = {}
    
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
            
    return freq

print(char_frequency("aabbc"))
# {'a': 2, 'b': 2, 'c': 1}