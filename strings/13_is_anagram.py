def is_anagram_sort(s1, s2):
    return sorted(s1) == sorted(s2)

def is_anagram_optimal(s1,s2):
    if len(s1) != len(s2):
        return False
    
    freq = {}
    
    for ch in s1:
        freq[ch] = freq.get(ch,0)+1
        
    for ch in s2:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False
    
    return True
        

print(is_anagram_sort("listen", "silent"))       # True
print(is_anagram_optimal("listen", "silent"))    # True
print(is_anagram_optimal("hello", "world"))      # False