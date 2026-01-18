def is_abundant(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total > n


def is_abundant_fast(n):
    if n < 12:   # smallest abundant number is 12
        return False

    total = 1   # 1 is always a proper divisor
    i = 2

    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
        i += 1

    return total > n

print(is_abundant(12))  # True
print(is_abundant(10))  # False
print(is_abundant(18))  # True

print(is_abundant_fast(12))  # True
print(is_abundant_fast(10))  # False
print(is_abundant_fast(18))  # True