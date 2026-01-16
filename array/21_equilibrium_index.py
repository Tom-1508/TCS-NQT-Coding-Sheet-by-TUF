def equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    result = []

    for i in range(len(arr)):
        total_sum -= arr[i]   # now total_sum is right sum

        if left_sum == total_sum:
            result.append(i)

        left_sum += arr[i]

    return result

print(equilibrium_index([1, 3, 5, 2, 2]))