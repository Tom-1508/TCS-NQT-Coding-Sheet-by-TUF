def frequency(arr):
    freq = {}  # dictionary to store count

    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    return freq

print(frequency([1,2,2,3,3,3]))