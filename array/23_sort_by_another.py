def sort_by_another(arr, order):
    # Step 1: frequency map
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    result = []

    # Step 2: process elements in 'order'
    for val in order:
        if val in freq:
            result.extend([val] * freq[val])
            del freq[val]  # remove processed element

    # Step 3: process remaining items sorted
    remaining = []
    for val, count in freq.items():
        remaining.extend([val] * count)

    result.extend(sorted(remaining))
    return result

print(sort_by_another(
    [2,1,2,5,7,1,9,3],
    [2,1,8,3]
))