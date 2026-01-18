def is_harshad(n):
    original = n
    total = 0 
    while n>0:
        digit = n % 10
        total = total + digit
        n = n // 10
    
    return original % total == 0

print(is_harshad(18))  # True
print(is_harshad(19))  # False
print(is_harshad(21))  # True