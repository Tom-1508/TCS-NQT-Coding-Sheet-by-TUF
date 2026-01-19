def non_repeating_chars(s):
    freq={}
    
    for ch in s:
        freq[ch] = freq.get(ch,0)+1
        
    result = []
    for ch in s:
        if freq[ch] == 1:
            result.append(ch)
    
    return result


print(non_repeating_chars("aabbcdde"))  # ['c', 'e']