def remove_duplicates_sorted(arr):
    if len(arr) == 0:
        return []

    i = 1  # write pointer

    for j in range(1, len(arr)):
        if arr[j] != arr[j - 1]:
            arr[i] = arr[j]
            i += 1

    return arr[:i]   # only unique part

print(remove_duplicates_sorted([1,1,2,2,3,4,4,4,5]))