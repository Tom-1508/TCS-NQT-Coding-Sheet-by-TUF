def smallest(arr):
    smallest = arr[0]
    for a in arr:
        if a<smallest:
            smallest=a
    return smallest

def largest(arr):
    largest = arr[0]
    for a in arr:
        if a>largest:
            largest=a
    return largest

def second_smallest(arr):
    smallest = min(arr)
    
    second = float('inf')
    for a in arr:
        if smallest<a<second:
            second=a
    return second if second != float('inf') else None
        

def second_largest(arr):
    largest = max(arr)
    
    second = float('-inf')
    for a in arr:
        if largest>a>second:
            second=a
    return second if second != float('-inf') else None

def reverse_array(arr):
    left = 0
    right = len(arr)-1
    
    while left<right:
        arr[left],arr[right] = arr[right], arr[left]
    
        left +=1
        right -= 1
    
    return arr

def frequency(arr):
    freq = {}
    for a in arr:
        if a in freq:
            freq[a] += 1
        else:
            freq[a] = 1
    return freq

def arr_inc_dec(arr):
    arr = sorted(arr)
    left = 0
    right = len(arr)-1
    res = []
    
    while left <= right:
        res.append(arr[left])
        left +=1
        if left <= right:
            res.append(arr[right])
            right -= 1
    
    return res
        

# print(smallest([5,2,9,1,6]))
# print(largest([5,2,9,1,6]))
# print(second_smallest([5, 2, 9, 1, 6]))
# print(second_largest([5, 2, 9, 1, 6]))
# print(reverse_array([1,2,3,4,5]))
print(frequency([1,2,2,3,3,3]))