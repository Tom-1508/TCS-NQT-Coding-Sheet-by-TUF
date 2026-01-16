def sort_by_frequency(arr):
    # Step 1: count frequencies
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # Step 2: sort by (-frequency, number)
    arr_sorted = sorted(arr, key=lambda x: (-freq[x], x))

    return arr_sorted

print(sort_by_frequency([2,3,2,4,5,12,2,3,3]))