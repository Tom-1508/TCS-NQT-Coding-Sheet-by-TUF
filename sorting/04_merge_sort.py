def merge_sort(arr):
    n = len(arr)
    
    if n<=1:
        return arr
    
    mid = n//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    i = j = 0
    result = []
    
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
        
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


print(merge_sort([5, 2, 4, 6, 1, 3]))