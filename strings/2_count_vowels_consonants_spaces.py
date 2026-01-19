def count_vowels_consonants_spaces(s):
    s = s.lower()
    vowels = 0
    consonants = 0
    spaces = 0
    
    for ch in s:
        if ch in 'aeiou':
            vowels += 1
        
        elif ch.isalpha():
            consonants+=1
        elif ch == " ":
            spaces += 1
    
    return vowels, consonants, spaces

print(count_vowels_consonants_spaces("hi tamal"))  
# (2, 5, 1)