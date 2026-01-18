def max_min_digit(n):
    maxi = 0
    mini = 9
    
    while n>0:
        digit = n%10
        
        if digit > maxi:
            maxi = digit
        if digit < mini:
            mini = digit
            
        n = n // 10
    return maxi, mini

print(max_min_digit(472951))  # (9, 1)
print(max_min_digit(1005))    # (5, 0)