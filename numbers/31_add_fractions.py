def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def add_fractions(a, b, c, d):
    num = a * d + c * b
    den = b * d

    g = gcd(num, den)

    num //= g
    den //= g

    return num, den


num, den = add_fractions(1, 2, 1, 3)
print(num, "/", den)   # 5 / 6