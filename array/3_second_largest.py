def second_largest(arr):
    # Step 1: find the largest
    largest = max(arr)

    # Step 2: find the largest number smaller than largest
    second = float('-inf')
    for num in arr:
        if second < num < largest:
            second = num

    return second if second != float('-inf') else None

print(second_largest([5, 2, 9, 1, 6]))