def is_strong(n):
    original = n
    total = 0

    while n > 0:
        digit = n % 10

        # factorial of digit
        fact = 1
        for i in range(1, digit + 1):
            fact *= i

        total += fact
        n //= 10

    return total == original

print(is_strong(145))  # True
print(is_strong(2))    # True  (2! = 2)
print(is_strong(123))  # False