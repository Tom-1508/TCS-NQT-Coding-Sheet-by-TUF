def greatest_of_three(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
    
print(greatest_of_three(10, 25, 15))  # 25
print(greatest_of_three(50, 20, 60))  # 60