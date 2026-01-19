def remove_vowels(s):
    vowels = "aeiouAEIOU"
    res = ""
    
    for ch in s:
        if ch not in vowels:
            res += ch
            
    return res

print(remove_vowels("Hello World"))  # Hll Wrld