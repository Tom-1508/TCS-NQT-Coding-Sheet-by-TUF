def circular_rotate_right(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]

def circular_rotate_left(arr, k):
    n = len(arr)
    k = k % n
    return arr[k:] + arr[:k]

print(circular_rotate_right([1,2,3,4,5], 2))
print(circular_rotate_left([1,2,3,4,5], 2))