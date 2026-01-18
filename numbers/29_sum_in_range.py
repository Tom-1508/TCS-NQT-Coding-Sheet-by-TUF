def sum_in_range(start, end):
    total = 0

    for num in range(start, end + 1):
        total += num

    return total


def sum_in_range_fast(start, end):
    def sum_n(n):
        return n * (n + 1) // 2

    return sum_n(end) - sum_n(start - 1)

print(sum_in_range(5, 10))         # 45
print(sum_in_range_fast(5, 10))    # 45