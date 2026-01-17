def is_armstrong(n):
    original = n
    digits = len(str(n))   # count digits
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** digits
        n = n // 10

    return total == original


print(is_armstrong(371))