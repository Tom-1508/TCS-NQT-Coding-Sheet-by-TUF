def remove_duplicates_unsorted(arr):
    seen = set()
    result = []

    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result

print(remove_duplicates_unsorted([4, 2, 4, 5, 2, 3, 1]))