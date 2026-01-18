def prime_factors(n):
    result = []
    
    #divided by 2
    while n%2==0:
        result.append(2)
        n //= 2
    
    # divided by odd numbers
    i = 3
    while i*i<=n:
        while n % i == 0:
            result.append(i)
            n//=i
        i+=2
    
    # if remaining n is prime
    if n>1:
        result.append(n)
    
    return result


print(prime_factors(36))  # [2, 2, 3, 3]
print(prime_factors(60))  # [2, 2, 3, 5]
print(prime_factors(13))  # [13]