def remove_brackets(s):
    brackets = "[](){}"
    res = ""
    for ch in s:
        if ch not in brackets:
            res+=ch
            
    return res

print(remove_brackets("(a+b)*[c-d]"))  # a+b*c-d