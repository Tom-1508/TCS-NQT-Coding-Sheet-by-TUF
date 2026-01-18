def is_automorphic(n):
    sq = n * n
    return str(sq).endswith(str(n))

print(is_automorphic(5))    # True
print(is_automorphic(6))    # True
print(is_automorphic(25))   # True
print(is_automorphic(7))    # False