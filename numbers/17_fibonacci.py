def fibonacci(n):
    a = 0 
    b = 1
    
    for _ in range(n):
        print(a,end=' ')
        a, b = b, a+b
        

def fibonacci_list(n):
    a=0
    b=1
    res = []
    
    for _ in range(n):
        res.append(a)
        a, b = b, a+b
    
    return res
    
fibonacci(10)
print()
print(fibonacci_list(15))
