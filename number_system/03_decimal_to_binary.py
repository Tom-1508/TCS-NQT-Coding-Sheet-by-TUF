def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    bin = ""
    while n>0:
        rem = n % 2
        bin = str(rem) + bin
        n = n // 2
    
    return bin


print(decimal_to_binary(13))  # 1101
print(decimal_to_binary(0))   # 0
print(decimal_to_binary(8))   # 1000