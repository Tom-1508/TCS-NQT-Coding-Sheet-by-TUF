def is_subset(arrA, arrB):
    setA = set(arrA)

    for num in arrB:
        if num not in setA:
            return False
    return True

print(is_subset([1,2,3,4,5], [2,3,5]))  # True
print(is_subset([1,2,3,4,5], [2,6]))    # False