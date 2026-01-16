def is_palindrome(number):
    original = number
    reversed_num =0
    
    while number>0:
        digit = number%10
        reversed_num=reversed_num*10+digit
        number=number//10
    
    return original == reversed_num

print(is_palindrome(121))   # True
print(is_palindrome(123))   # False