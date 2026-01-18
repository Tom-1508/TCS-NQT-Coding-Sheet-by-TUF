def power(a,b):
    res = 1
    
    for _ in range(b):
        res = res * a
        
    return res

print(power(2, 5))  # 32
print(power(3, 4))  # 81