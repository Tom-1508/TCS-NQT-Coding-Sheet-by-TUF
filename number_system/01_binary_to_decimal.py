def binary_to_decimal(bin_str):
    decimal = 0
    power = 0
    reverse_bin_str = bin_str[::-1]
    
    for digit in reverse_bin_str:
        if digit == '1':
            decimal += 2 ** power
        power += 1
        
    return decimal

print(binary_to_decimal("1011"))  # 11
print(binary_to_decimal("1000"))  # 8