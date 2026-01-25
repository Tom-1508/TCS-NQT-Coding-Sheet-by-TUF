# def smallest(arr):
#     smallest = arr[0]
#     for a in arr:
#         if a<smallest:
#             smallest=a
#     return smallest

# def largest(arr):
#     largest = arr[0]
#     for a in arr:
#         if a>largest:
#             largest=a
#     return largest

# def second_smallest(arr):
#     smallest = min(arr)
    
#     second = float('inf')
#     for a in arr:
#         if smallest<a<second:
#             second=a
#     return second if second != float('inf') else None
        

# def second_largest(arr):
#     largest = max(arr)
    
#     second = float('-inf')
#     for a in arr:
#         if largest>a>second:
#             second=a
#     return second if second != float('-inf') else None

# def reverse_array(arr):
#     left = 0
#     right = len(arr)-1
    
#     while left<right:
#         arr[left],arr[right] = arr[right], arr[left]
    
#         left +=1
#         right -= 1
    
#     return arr

# def frequency(arr):
#     freq = {}
#     for a in arr:
#         if a in freq:
#             freq[a] += 1
#         else:
#             freq[a] = 1
#     return freq

# def arr_inc_dec(arr):
#     arr = sorted(arr)
#     left = 0
#     right = len(arr)-1
#     res = []
    
#     while left <= right:
#         res.append(arr[left])
#         left +=1
#         if left <= right:
#             res.append(arr[right])
#             right -= 1
    
#     return res
        

# print(smallest([5,2,9,1,6]))
# print(largest([5,2,9,1,6]))
# print(second_smallest([5, 2, 9, 1, 6]))
# print(second_largest([5, 2, 9, 1, 6]))
# print(reverse_array([1,2,3,4,5]))
# print(frequency([1,2,2,3,3,3]))

# def second_highest(arr):
#     highest = max(arr)
#     second = float('-inf')
    
#     for num in arr:
#         if second > num > highest:
#             second = num
    
#     return second if second != float('-inf') else None

# print(second_highest([5, 2, 9, 1, 6]))



# def reverse_array(arr):
#     left, right = 0, len(arr)-1
#     while left<=right:
#         arr[left], arr[right] = arr[right], arr[left]
#         left += 1
#         right -= 1
#     return arr

# print(reverse_array([9,6,45,34,2,5,1]))

# def freq(arr):
#     freq = {}
#     # for num in arr:
#     #     freq[num] = freq.get(num,0)+1
    
#     for num in arr:
#         if num in freq:
#             freq[num] += 1
#         else:
#             freq[num] = 1
    
#     return freq

# print(freq([1,4,4,5,5,2,2,10,45,67,45,89]))


# def rearrange_inc_dec(arr):
#     arr = sorted(arr)
#     left, right = 0,len(arr)-1
#     ans= []
    
#     while left<=right:
#         if left<=right:
#             ans.append(arr[left])
#             left+=1
#         if left<=right:
#             ans.append(arr[right])
#             right -= 1
#     return ans

# print(rearrange_inc_dec(arr=[1,2,3,4,5,6]))


# def sum_of_array(arr):
#     # total = 0
#     # for num in arr:
#     #     total += num
#     # return total
    
#     return sum(arr) if arr else 0

# print(sum_of_array([3,4,5,6]))
# print(sum_of_array([]))



class Car():
    title = "Majumdar"
    def __init__(self, name):
        self.name =name
        
    @classmethod
    def hello(cls):
        cls.title = "Bhattacharjee"
        
        
car1 = Car("maruti")
print(car1.name)
print(car1.title)
car1.hello()
print(car1.title)



# def merge_sort(arr):
#     if len(arr)<=1:
#         return arr
    
#     mid = len(arr)//2
#     left_half = merge_sort(arr[:mid])
#     right_half = merge_sort(arr[mid:])
    
#     return merge(left_half,right_half)

# def merge(left, right):
#     result = []
#     i=j=0
    
#     while i<len(left) and j<len(right):
#         if left[i] <= right[i]:
#             result.append(left[i])
#             i+=1
#         else:
#             result.append(right[i])
#             j+=1
            
#     result.extend(left[i:])
#     result.extend(right[j:])
    
#     return result



def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid = len(arr)//2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    res =[]
    i=j=0
    
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1