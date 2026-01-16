def rearrange_inc_dec(arr):
    arr = sorted(arr)           # step 1: sort
    left = 0
    right = len(arr) - 1
    result = []

    while left <= right:
        result.append(arr[left])   # smallest
        left += 1
        if left <= right:
            result.append(arr[right])  # largest
            right -= 1

    return result

print(rearrange_inc_dec([1,2,3,4,5,6]))