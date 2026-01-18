def is_prime(x):
    if x<=1:
        return False
    
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return False
    
    return True

def can_be_sum_of_two_primes(n):
    for p in range(2,n):
        if is_prime(p) and is_prime(n-p):
            return True
    return False

print(can_be_sum_of_two_primes(10))  # True  (3+7)
print(can_be_sum_of_two_primes(11))  # False