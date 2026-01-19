def sum_numbers_in_string(s):
    total = 0
    num = ""
    
    for ch in s:
        if ch.isdigit():
            num+=ch
        else:
            if num != "":
                total += int(num)
                num = ""
        
    # add last number if string ends with digits
    if num != "":
        total += int(num)
    
    return total


print(sum_numbers_in_string("a12b3c4"))   # 19
print(sum_numbers_in_string("100abc20"))  # 120