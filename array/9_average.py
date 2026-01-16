def average(arr):
    if len(arr) == 0:
        return None   # avoid division by zero
    
    total = 0
    for num in arr:
        total += num

    return total / len(arr)

print(average([2,4,6,8]))