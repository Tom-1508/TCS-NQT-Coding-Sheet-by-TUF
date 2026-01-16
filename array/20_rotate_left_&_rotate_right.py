def rotate_left(arr, k):
    n = len(arr)
    k = k % n
    return arr[k:] + arr[:k]

def rotate_right(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]

print(rotate_left([1,2,3,4,5], 2))   # [3,4,5,1,2]
print(rotate_right([1,2,3,4,5], 2))  # [4,5,1,2,3] 