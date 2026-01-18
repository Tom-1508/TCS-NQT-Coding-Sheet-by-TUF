def factors(n):
    result = []

    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)

    return result


def factors_sqrt(n):
    result = []

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            result.append(i)

            if i != n // i:      # avoid duplicate for perfect squares
                result.append(n // i)

    return sorted(result)

print(factors(12))  # [1, 2, 3, 4, 6, 12]
print(factors_sqrt(12))  # [1, 2, 3, 4, 6, 12]