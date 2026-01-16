def smallest(arr):
    smallest = arr[0]        # assume 1st element is smallest
    for num in arr:          # go through each number
        if num < smallest:   # check if smaller
            smallest = num   # update
    return smallest

print(smallest([5,2,9,1,6]))