def factorial(n):
    fact = 1
    
    for i in range(1, n+1):
        fact = fact * i
    return fact

print(factorial(5))  # 120
print(factorial(0))  # 1