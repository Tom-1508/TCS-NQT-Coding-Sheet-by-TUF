def remove_chars(s1, s2):
    remove_set = set(s2)
    result = ""
    
    for ch in s1:
        if ch not in remove_set:
            result += ch
            
    return result

print(remove_chars("abcdef", "bd"))     # acef
print(remove_chars("tamal", "am"))      # tl