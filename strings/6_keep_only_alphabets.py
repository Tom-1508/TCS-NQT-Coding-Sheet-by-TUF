def keep_only_alphabets(s):
    res = ""
    for ch in s:
        if ch.isalpha():
            res+=ch
    return res

print(keep_only_alphabets("Tamal@123!!"))  # Tamal