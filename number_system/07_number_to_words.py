def number_to_words(n):
    mapping = {
        '0': "Zero", '1': "One", '2': "Two", '3': "Three", '4': "Four",
        '5': "Five", '6': "Six", '7': "Seven", '8': "Eight", '9': "Nine"
    }
    
    s = str(n)
    result = []
    
    for ch in s:
        result.append(mapping[ch])
    
    return " ".join(result)

print(number_to_words(123))   # One Two Three
print(number_to_words(507))   # Five Zero Seven