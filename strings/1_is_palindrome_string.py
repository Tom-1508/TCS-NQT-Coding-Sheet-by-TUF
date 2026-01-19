def is_palindrome_string(s):
    return s == s[::-1]

print(is_palindrome_string("madam"))  # True
print(is_palindrome_string("hello"))  # False

