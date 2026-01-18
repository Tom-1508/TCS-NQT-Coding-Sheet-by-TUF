import math

def quadratic_roots(a, b, c):
    D = b*b - 4*a*c

    if D > 0:
        root1 = (-b + math.sqrt(D)) / (2*a)
        root2 = (-b - math.sqrt(D)) / (2*a)
        return root1, root2

    elif D == 0:
        root = -b / (2*a)
        return root, root

    else:
        real = -b / (2*a)
        imag = math.sqrt(-D) / (2*a)
        return (real, imag), (real, -imag)
    
    
print(quadratic_roots(1, -3, 2))   # (2.0, 1.0)
print(quadratic_roots(1, 2, 1))    # (-1.0, -1.0)
print(quadratic_roots(1, 2, 5))    # complex roots