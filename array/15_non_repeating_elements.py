def non_repeating_elements(arr):
    freq = {}
    result = []

    # Count occurrences
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Collect only elements that appear once
    for num, count in freq.items():
        if count == 1:
            result.append(num)

    return result

print(non_repeating_elements([1,2,2,3,4,4,5]))