def palindrome_in_range(start, end):
    result = []
    
    for num in range(start, end+1):
        temp = num
        reverse = 0
        
        while temp>0:
            digit = temp%10
            reverse = reverse*10+digit
            temp=temp//10
            
        if num==reverse:
            result.append(num)
    return result

print(palindrome_in_range(10, 200))