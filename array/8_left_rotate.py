def left_rotate(arr, k):
    n = len(arr)
    
    k = k % n  # handle large k

    return arr[k:] + arr[:k]

print(left_rotate([1,2,3,4,5], 2))