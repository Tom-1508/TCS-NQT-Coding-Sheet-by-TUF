def second_smallest(arr):
    # Step 1: find the smallest
    smallest = min(arr)

    # Step 2: find the smallest number greater than smallest
    second = float('inf')
    for num in arr:
        if smallest < num < second:
            second = num

    return second if second != float('inf') else None

print(second_smallest([5, 2, 9, 1, 6]))