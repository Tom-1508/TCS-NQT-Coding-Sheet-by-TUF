def max_occurring_char(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch,0)+1
        
    max_ch = s[0]
    max_count = freq[max_ch]
    
    for ch in s:
        if freq[ch] > max_count:
            max_count = freq[ch]
            max_ch = ch
            
    return max_ch

print(max_occurring_char("aabbbcc"))  # b
print(max_occurring_char("tamal"))    # a (appears 2 times)