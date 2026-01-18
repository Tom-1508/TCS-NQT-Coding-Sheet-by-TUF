def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        
    return fact

def npr(n,r):
    if r>n:
        return 0
    
    return factorial(n) // factorial(n-r)


def npr_fast(n, r):
    if r > n:
        return 0

    result = 1
    for i in range(r):
        result *= (n - i)

    return result


print(npr(5, 3))  # 60
print(npr(10, 2)) # 90

print(npr_fast(5, 3))   # 60
print(npr_fast(10, 2))  # 90