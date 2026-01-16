def repeating_elements(arr):
    freq = {}
    result = []

    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for num, count in freq.items():
        if count > 1:
            result.append(num)

    return result