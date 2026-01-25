def octal_to_decimal(octal_str):
    decimal = 0
    
    for ch in octal_str:
        decimal = decimal * 8 + int(ch)
    
    return decimal

print(octal_to_decimal("123"))  # 83
print(octal_to_decimal("10"))   # 8