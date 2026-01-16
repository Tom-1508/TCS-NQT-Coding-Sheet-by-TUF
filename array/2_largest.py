def largest(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

print(largest([5,2,9,1,6]))