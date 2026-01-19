def cap_first_last(s):
    words = s.split()
    result = []
    
    for w in words:
        if len(w)==1:
            result.append(w.upper())
        else:
            new_word = w[0].upper() + w[1:-1] + w[-1].upper()
            result.append(new_word)
    
    return " ".join(result)

print(cap_first_last("hello world"))   # HellO WorlD
print(cap_first_last("i am tamal"))    # I AM TamaL