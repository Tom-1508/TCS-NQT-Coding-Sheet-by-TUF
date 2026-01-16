def find_median(arr):
    arr = sorted(arr)
    n = len(arr)
    mid = n // 2

    if n % 2 != 0:  
        # odd length
        return arr[mid]
    else:
        # even length = average of middle two
        return (arr[mid - 1] + arr[mid]) / 2
    
print(find_median([3,1,5]))
print(find_median([4,2,9,6]))