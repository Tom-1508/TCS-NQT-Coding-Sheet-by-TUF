def binary_to_octal(binary_str):
    # make len multiple of 3 by adding leading zeroes
    while len(binary_str)%3 != 0:
        binary_str = "0" + binary_str
    
    octal = ""
    
    for i in range(0, len(binary_str), 3):
        group = binary_str[i:i+3]
        value = int(group, 2) # convert 3-bit group to decimal
        octal += str(value)
    
    return octal.lstrip("0") or "0"

print(binary_to_octal("110101"))  # 65
print(binary_to_octal("1011"))    # 13