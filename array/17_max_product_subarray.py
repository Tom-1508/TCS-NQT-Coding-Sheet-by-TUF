def max_product_subarray(arr):
    max_here = arr[0]
    min_here = arr[0]
    result = arr[0]

    for num in arr[1:]:
        # if num is negative, swap
        if num < 0:
            max_here, min_here = min_here, max_here

        max_here = max(num, max_here * num)
        min_here = min(num, min_here * num)

        result = max(result, max_here)

    return result

print(max_product_subarray([2,3,-2,4]))      # 6
print(max_product_subarray([-2,0,-1]))        # 0
print(max_product_subarray([-2,-3,4]))        # 24