# 🔢 **NUMBERS — Problem 1**

## **1) Check if a Number is Palindrome or Not**

### 💡 **What is a Palindrome Number?**

A number is **palindrome** if it reads the same **forward and backward**.

Examples:

* `121` → ✅ Palindrome
* `123` → ❌ Not palindrome
* `1221` → ✅ Palindrome

---

## 🧠 **Simple Idea**

1. Store the original number
2. Reverse the number
3. Compare reversed number with original

If both are same → Palindrome.

---

## ✔️ **Step-by-step Code**

```python
def is_palindrome(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10          # get last digit
        reverse = reverse * 10 + digit
        n = n // 10             # remove last digit

    return original == reverse
```

---

## ⏱ **Time Complexity (TC)**

O(D)
(D = number of digits)

---

## 📦 **Space Complexity (SC)**

O(1)
(Only variables used, no extra memory)

---

## ⭐ Try It

```python
print(is_palindrome(121))   # True
print(is_palindrome(123))   # False
```

---




# 🔢 **NUMBERS — Problem 2**

## **2) Find All Palindrome Numbers in a Given Range**

### 💡 **Meaning**

You are given a range:

```
start = 10
end   = 200
```

You must print all numbers between this range that are **palindromes**.

---

## 🧠 **Simple Logic**

1. Loop from `start` to `end`
2. For each number:

   * Reverse it
   * Check if original == reversed
3. If yes → add to result

We will **reuse** the palindrome logic.

---

## ✔️ **Code (Very Simple)**

```python
def palindrome_in_range(start, end):
    result = []

    for num in range(start, end + 1):
        temp = num
        reverse = 0

        while temp > 0:
            digit = temp % 10
            reverse = reverse * 10 + digit
            temp = temp // 10

        if num == reverse:
            result.append(num)

    return result
```

---

## ⏱ **Time Complexity (TC)**

O(N × D)

* N = numbers in range
* D = digits in number

---

## 📦 **Space Complexity (SC)**

O(P)
(P = number of palindrome numbers stored)

---

## ⭐ Try It

```python
print(palindrome_in_range(10, 200))
```

Expected output:

```
[11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]
```

---


# 🔢 **NUMBERS — Problem 3**

## **3) Check if a Number is Prime or Not**

### 💡 What is a Prime Number?

A number is **prime** if it has **only 2 factors**:

✅ 1 and itself

Examples:

* 2 ✅ prime
* 3 ✅ prime
* 4 ❌ not prime (2×2)
* 5 ✅ prime
* 6 ❌ not prime (2×3)

---

## 🧠 Simple Logic

To check prime:

1. If number ≤ 1 → not prime
2. Check divisibility from **2 to √n**

   * If divisible by any → not prime
3. Otherwise → prime

Why √n?
Because if `n = a × b`, one of them must be ≤ √n.

---

## ✔️ Code (Simple + Efficient)

```python
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True
```

---

## ⏱ Time Complexity (TC)

O(√N)

---

## 📦 Space Complexity (SC)

O(1)

---

## ⭐ Try It

```python
print(is_prime(2))   # True
print(is_prime(7))   # True
print(is_prime(10))  # False
```

---

# 🔢 **NUMBERS — Problem 4**

## **4) Prime Numbers in a Given Range**

### 💡 Meaning

If range is:

```
start = 10
end = 50
```

We print all primes between them:
✅ `11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47`

---

## 🧠 Simple Logic

1. Loop from `start` to `end`
2. Check each number is prime using `is_prime()`
3. If prime → add to result

---

## ✔️ Code

```python
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def primes_in_range(start, end):
    result = []

    for num in range(start, end + 1):
        if is_prime(num):
            result.append(num)

    return result
```

---

## ⏱ Time Complexity (TC)

For each number → O(√N)
Total → **O((end-start) × √end)**

---

## 📦 Space Complexity (SC)

O(P) (P = number of primes stored)

---

## ⭐ Try It

```python
print(primes_in_range(10, 50))
```

Expected:

```
[11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

---

# 🔢 NUMBERS — Check if a Number is Armstrong or Not

## ✅ What is an Armstrong Number?

A number is called **Armstrong** if:

> sum of each digit raised to the power of number of digits
> = the original number

### Example: `153`

Digits = 1, 5, 3
Number of digits = 3

So:

```
1³ + 5³ + 3³
= 1 + 125 + 27
= 153 ✅ Armstrong
```

---

## 🧠 Simple Steps

1. Store the original number
2. Count number of digits
3. Extract each digit and calculate `digit^digits`
4. Add them
5. If final sum == original → Armstrong ✅

---

## ✅ Python Code

```python
def is_armstrong(n):
    original = n
    digits = len(str(n))   # count digits
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** digits
        n = n // 10

    return total == original
```

---

## ⏱ Time Complexity (TC)

**O(D)**
(D = number of digits)

---

## 📦 Space Complexity (SC)

**O(1)**

---

## ✅ Test It

```python
print(is_armstrong(153))  # True
print(is_armstrong(370))  # True
print(is_armstrong(123))  # False
```

---


Perfect, Tamal! 🔥✅
Next one:

---

# 🔢 **NUMBERS — Problem**

## ✅ Check if a Number is a Perfect Number

### 💡 What is a Perfect Number?

A number is **perfect** if:

✅ sum of its **proper divisors** (excluding itself) = number

Example: `28`
Divisors of 28 (excluding 28): `1, 2, 4, 7, 14`
Sum = `1+2+4+7+14 = 28` ✅ Perfect

---

## 🧠 Simple Steps

1. Start sum = 0
2. Loop from 1 to n-1
3. If i divides n → add i
4. Check sum == n

---

## ✅ Code

```python
def is_perfect(n):
    if n <= 1:
        return False

    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n
```

---

## ⏱ Time Complexity (TC)

**O(N)**

## 📦 Space Complexity (SC)

**O(1)**

---

## ⭐ Test

```python
print(is_perfect(28))  # True
print(is_perfect(12))  # False
```

---

# 🔢 **NUMBERS — Problem**

## ✅ Even or Odd

### 💡 Simple Rule

* If `n % 2 == 0` → **Even**
* Else → **Odd**

---

## ✅ Code

```python
def is_even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
```

---

## ⏱ Time Complexity (TC)

**O(1)**

## 📦 Space Complexity (SC)

**O(1)**

---

## ⭐ Test

```python
print(is_even_or_odd(10))  # Even
print(is_even_or_odd(7))   # Odd
```

---

# 🔢 **NUMBERS — Problem**

## ✅ Check Whether a Number is Positive or Negative

### 💡 Simple Rule

* `n > 0` → Positive
* `n < 0` → Negative
* `n == 0` → Zero

---

## ✅ Code

```python
def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"
```

---

## ⏱ Time Complexity (TC)

**O(1)**

## 📦 Space Complexity (SC)

**O(1)**

---

## ⭐ Test

```python
print(check_number(10))   # Positive
print(check_number(-5))   # Negative
print(check_number(0))    # Zero
```

---

# 🔢 **NUMBERS — Problem**

## ✅ Sum of First N Natural Numbers

### 💡 Meaning

If `N = 5`
Sum = `1 + 2 + 3 + 4 + 5 = 15`

---

## ✅ Method 1 (Best) — Formula

### 🧠 Logic

Sum of first N numbers:
[
sum = N(N+1)/2
]

---

### ✅ Code

```python
def sum_n(n):
    return n * (n + 1) // 2
```

---

## ⏱ Time Complexity (TC)

**O(1)**

## 📦 Space Complexity (SC)

**O(1)**

---

## ⭐ Test

```python
print(sum_n(5))   # 15
print(sum_n(10))  # 55
```

---

# 🔢 **NUMBERS — Find Sum of AP Series**

---

## ✅ What is AP?

**AP (Arithmetic Progression)** means numbers increase by a fixed difference.

Example:
`2, 5, 8, 11, 14 ...`

Here:

* First term `a = 2`
* Common difference `d = 3`
* Number of terms `n`

---

## ✅ Formula (Most Important)

### **Nth term**

[
T_n = a + (n-1)d
]

### **Sum of AP**

[
S = (n/2)*(2a+(n-1)*d)
]

---

# ✅ Python Code (Very Simple)

```python
def sum_ap(a, d, n):
    return (n * (2*a + (n-1)*d)) // 2
```

---

## ⏱ Time Complexity (TC)

**O(1)**

## 📦 Space Complexity (SC)

**O(1)**

---

## ⭐ Example Test

```python
# AP: 2, 5, 8, 11, 14  (a=2, d=3, n=5)
print(sum_ap(2, 3, 5))  # 40
```

✅ Because: `2+5+8+11+14 = 40`

---

# 🔢 **NUMBERS — Problem**

## ✅ Program to Find Sum of GP Series

### 💡 What is GP?

**GP (Geometric Progression)** means numbers multiply by a fixed ratio.

Example:
`2, 4, 8, 16, 32 ...`

Here:

* First term `a = 2`
* Common ratio `r = 2`
* Number of terms `n`

---

## ✅ Formula (Most Important)

### ✅ If `r != 1`

[
S = (a *((r**n) - )) // (r-1)
]

### ✅ If `r == 1`

[
S = a * n
]

---

# ✅ Python Code (Simple)

```python
def sum_gp(a, r, n):
    if r == 1:
        return a * n
    return a * (r**n - 1) // (r - 1)
```

---

## ⏱ Time Complexity (TC)

**O(1)**

## 📦 Space Complexity (SC)

**O(1)**

---

## ⭐ Example Test

```python
# GP: 2, 4, 8, 16, 32  (a=2, r=2, n=5)
print(sum_gp(2, 2, 5))  # 62
```

✅ Because: `2+4+8+16+32 = 62`

---

# 🔢 **NUMBERS — Problem**

## ✅ Greatest of Two Numbers

### 💡 Simple Meaning

Given 2 numbers, print the bigger one.

Example:
`a = 10, b = 25` → greatest = **25**

---

## ✅ Code

```python
def greatest_of_two(a, b):
    if a > b:
        return a
    else:
        return b
```

---

## ⏱ Time Complexity (TC)

**O(1)**

## 📦 Space Complexity (SC)

**O(1)**

---

## ⭐ Test

```python
print(greatest_of_two(10, 25))  # 25
print(greatest_of_two(50, 20))  # 50
```

---

# 🔢 **NUMBERS — Problem**

## ✅ Greatest of Three Numbers

### 💡 Meaning

Given 3 numbers, return the biggest one.

Example:
`a=10, b=25, c=15` → greatest = **25**

---

## ✅ Code

```python
def greatest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
```

---

## ⏱ Time Complexity (TC)

**O(1)**

## 📦 Space Complexity (SC)

**O(1)**

---

## ⭐ Test

```python
print(greatest_of_three(10, 25, 15))  # 25
print(greatest_of_three(50, 20, 60))  # 60
```

---

# 🔢 **NUMBERS — Problem**

## ✅ Leap Year or Not

### 💡 What is a Leap Year?

A year is **leap year** if:

✅ divisible by 400
OR
✅ divisible by 4 but NOT divisible by 100

---

## ✅ Rules (Super Simple)

1. If year % 400 == 0 → Leap ✅
2. Else if year % 100 == 0 → Not Leap ❌
3. Else if year % 4 == 0 → Leap ✅
4. Else → Not Leap ❌

---

## ✅ Code

```python
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
```

---

## ⏱ Time Complexity (TC)

**O(1)**

## 📦 Space Complexity (SC)

**O(1)**

---

## ⭐ Test

```python
print(is_leap_year(2024))  # True
print(is_leap_year(1900))  # False
print(is_leap_year(2000))  # True
```

---

# 🔢 **NUMBERS — Problem**

## ✅ Reverse Digits of a Number

### 💡 Meaning

Input: `1234`
Output: `4321`

---

## 🧠 Simple Steps

1. Take last digit using `% 10`
2. Add it to reverse number
3. Remove last digit using `// 10`
4. Repeat until number becomes 0

---

## ✅ Code

```python
def reverse_number(n):
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    return rev
```

---

## ⏱ Time Complexity (TC)

**O(D)** (D = number of digits)

## 📦 Space Complexity (SC)

**O(1)**

---

## ⭐ Test

```python
print(reverse_number(1234))  # 4321
print(reverse_number(100))   # 1
```

---


# 🔢 **NUMBERS — Maximum and Minimum Digit in a Number**

### 💡 Meaning

Input: `472951`
✅ Maximum digit = `9`
✅ Minimum digit = `1`

---

## 🧠 Simple Steps

1. Take last digit using `% 10`
2. Compare it with current `maxi` and `mini`
3. Update max / min
4. Remove last digit using `// 10`
5. Repeat until number becomes 0

---

## ✅ Code (Simple)

```python
def max_min_digit(n):
    maxi = 0
    mini = 9

    while n > 0:
        digit = n % 10

        if digit > maxi:
            maxi = digit
        if digit < mini:
            mini = digit

        n = n // 10

    return maxi, mini
```

---

## ⏱ Time Complexity (TC)

**O(D)** (D = number of digits)

## 📦 Space Complexity (SC)

**O(1)**

---

## ⭐ Test

```python
print(max_min_digit(472951))  # (9, 1)
print(max_min_digit(1005))    # (5, 0)
```

---

# 🔢 **NUMBERS — Print Fibonacci upto Nth Term**

### 💡 Fibonacci Series

Each number = sum of previous two

Example:
`0 1 1 2 3 5 8 13 ...`

---

## 🧠 Simple Logic

Start:

* `a = 0`
* `b = 1`

Repeat `n` times:

* print `a`
* update: `a = b`, `b = a+b`

---

# ✅ Code (Print first N terms)

```python
def fibonacci(n):
    a = 0
    b = 1

    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
```

---

## ⏱ Time Complexity (TC)

**O(N)**

## 📦 Space Complexity (SC)

**O(1)**

---

## ⭐ Test

```python
fibonacci(10)
```

Output:

```
0 1 1 2 3 5 8 13 21 34
```

---

If you want **return as list** (sometimes asked):

```python
def fibonacci_list(n):
    a, b = 0, 1
    res = []

    for _ in range(n):
        res.append(a)
        a, b = b, a + b

    return res
```

---

# 🔢 **NUMBERS — Factorial of a Number**

### 💡 Meaning

Factorial of `n` is:

[
n! = n * (n-1) * (n-2) * ... * 1
]

Example:

* `5! = 5×4×3×2×1 = 120`
* `0! = 1`

---

## 🧠 Simple Logic

1. Start `fact = 1`
2. Multiply from `1` to `n`
3. Return fact

---

# ✅ Code

```python
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact
```

---

## ⏱ Time Complexity (TC)

**O(N)**

## 📦 Space Complexity (SC)

**O(1)**

---

## ⭐ Test

```python
print(factorial(5))  # 120
print(factorial(0))  # 1
```

---

Sure ✅ Tamal!

---

# 🔢 **NUMBERS — Power of a Number (a^b)**

### 💡 Meaning

We calculate:

[
a^b = a* a* a* ... (b times)
]

Example:

* `2^5 = 32`
* `3^4 = 81`

---

## 🧠 Simple Logic

1. Start `result = 1`
2. Multiply `a` exactly `b` times

---

# ✅ Code (Loop Method)

```python
def power(a, b):
    result = 1

    for _ in range(b):
        result *= a

    return result
```

---

## ⏱ Time Complexity (TC)

**O(B)**

## 📦 Space Complexity (SC)

**O(1)**

---

## ⭐ Test

```python
print(power(2, 5))  # 32
print(power(3, 4))  # 81
```

---

✅ **Note:** In Python you can also do `a**b`, but in exams they prefer logic.


Sure ✅ Tamal! This one is very common.

---

# 🔢 **NUMBERS — Factors of a Given Number**

### 💡 Meaning

Factors are numbers that divide `n` completely (remainder 0).

Example: `n = 12`
Factors: `1, 2, 3, 4, 6, 12`

---

## 🧠 Simple Logic

1. Loop from `1` to `n`
2. If `n % i == 0` → `i` is a factor

---

# ✅ Code (Simple)

```python
def factors(n):
    result = []

    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)

    return result
```

---

## ⏱ Time Complexity (TC)

**O(N)**

## 📦 Space Complexity (SC)

**O(F)**
(F = number of factors stored)

---

## ⭐ Test

```python
print(factors(12))  # [1, 2, 3, 4, 6, 12]
```

---

✅ If you want faster method later, I’ll teach √n approach too.

# ✅ Faster Method: Factors using √n

## 💡 Why faster?

Instead of checking from **1 to n**, we check only till **√n**.

Because factors always come in pairs:

If `i` divides `n`, then `n//i` is also a factor.

Example: `36`

* 1 × 36
* 2 × 18
* 3 × 12
* 4 × 9
* 6 × 6  ← stop around √36 = 6

---

# ✅ Code (Efficient)

```python
def factors_sqrt(n):
    result = []

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            result.append(i)

            if i != n // i:      # avoid duplicate for perfect squares
                result.append(n // i)

    return sorted(result)
```

---

## ⏱ Time Complexity (TC)

✅ **O(√N)**

## 📦 Space Complexity (SC)

✅ **O(F)** (storing factors)

---

## ⭐ Test

```python
print(factors_sqrt(36))  # [1, 2, 3, 4, 6, 9, 12, 18, 36]
print(factors_sqrt(12))  # [1, 2, 3, 4, 6, 12]
```

---

Sure ✅ Tamal! Let’s do **Prime Factors** in the simplest + fastest way.

---

# 🔢 **NUMBERS — Print All Prime Factors of a Number**

### 💡 Meaning

Prime factors are the **prime numbers** that multiply to give `n`.

Example:
`n = 36`
Prime factors = `2, 2, 3, 3`
(because `36 = 2 × 2 × 3 × 3`)

---

## 🧠 Simple Logic (Efficient)

1. Divide by **2** as long as possible
2. Then check odd numbers from **3 to √n**
3. If `n` becomes > 1 at the end → it is also a prime factor

---

# ✅ Code

```python
def prime_factors(n):
    result = []

    # divide by 2
    while n % 2 == 0:
        result.append(2)
        n //= 2

    # divide by odd numbers
    i = 3
    while i * i <= n:
        while n % i == 0:
            result.append(i)
            n //= i
        i += 2

    # if remaining n is prime
    if n > 1:
        result.append(n)

    return result
```

---

## ⏱ Time Complexity (TC)

✅ **O(√N)**

## 📦 Space Complexity (SC)

✅ **O(P)**
(P = number of prime factors stored)

---

## ⭐ Test

```python
print(prime_factors(36))  # [2, 2, 3, 3]
print(prime_factors(60))  # [2, 2, 3, 5]
print(prime_factors(13))  # [13]
```

---

# 🔢 **NUMBERS — Check if a Number is a Strong Number or Not**

## ✅ What is a Strong Number?

A number is **Strong** if:

> Sum of factorial of each digit = original number

### Example: `145`

Digits: 1, 4, 5
Factorials:

* 1! = 1
* 4! = 24
* 5! = 120

Sum = `1 + 24 + 120 = 145` ✅ Strong Number

---

## 🧠 Simple Steps

1. Store original number
2. Extract each digit
3. Find factorial of that digit
4. Add them
5. Compare sum with original

---

# ✅ Code (Simple)

```python
def is_strong(n):
    original = n
    total = 0

    while n > 0:
        digit = n % 10

        # factorial of digit
        fact = 1
        for i in range(1, digit + 1):
            fact *= i

        total += fact
        n //= 10

    return total == original
```

---

## ⏱ Time Complexity (TC)

O(D * 10) → simplified as **O(D)**
(D = number of digits, factorial loop max 9)

## 📦 Space Complexity (SC)

**O(1)**

---

## ⭐ Test

```python
print(is_strong(145))  # True
print(is_strong(2))    # True  (2! = 2)
print(is_strong(123))  # False
```

---

# 🔢 **NUMBERS — Check if a Number is Automorphic**

## ✅ What is an Automorphic Number?

A number is **Automorphic** if its **square ends with the same number**.

### Examples:

✅ `5` → 5² = 25 → ends with **5** ✅
✅ `6` → 6² = 36 → ends with **6** ✅
✅ `25` → 25² = 625 → ends with **25** ✅
❌ `7` → 7² = 49 → not ending with 7 ❌

---

## 🧠 Simple Logic

1. Compute square: `sq = n * n`
2. Convert both to string
3. Check if square ends with number

---

# ✅ Code (Very Simple)

```python
def is_automorphic(n):
    sq = n * n
    return str(sq).endswith(str(n))
```

---

## ⏱ Time Complexity (TC)

O(D) (D = digits, due to string check)

## 📦 Space Complexity (SC)

O(D) (string conversion)

---

## ⭐ Test

```python
print(is_automorphic(5))    # True
print(is_automorphic(6))    # True
print(is_automorphic(25))   # True
print(is_automorphic(7))    # False
```

---

# 🔢 **NUMBERS — GCD of Two Numbers**

## ✅ What is GCD?

**GCD (Greatest Common Divisor)** = the biggest number that divides both numbers.

Example:
`a = 12, b = 18`
Common divisors: `1,2,3,6`
✅ GCD = **6**

---

## 🧠 Best Logic: Euclidean Algorithm

Rule:
[
gcd(a,b) = gcd(b, a % b)
]
Keep doing this until `b` becomes 0.

---

# ✅ Code (Fastest)

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

---

## ⏱ Time Complexity (TC)

✅ **O(log(min(a,b)))**

## 📦 Space Complexity (SC)

✅ **O(1)**

---

## ⭐ Test

```python
print(gcd(12, 18))  # 6
print(gcd(100, 25)) # 25
```

---



# 🔢 **NUMBERS — LCM of Two Numbers**

## ✅ What is LCM?

**LCM (Least Common Multiple)** = the smallest number that is divisible by both numbers.

Example:
`a = 12, b = 18`
✅ LCM = **36**

---

## 🧠 Best Logic

Formula:

[
LCM(a,b) = \frac{a \times b}{GCD(a,b)}
]

So first find **GCD**, then calculate LCM.

---

# ✅ Code

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)
```

---

## ⏱ Time Complexity (TC)

O(log(min(a,b)))  (because of GCD)

## 📦 Space Complexity (SC)

O(1)

---

## ⭐ Test

```python
print(lcm(12, 18))  # 36
print(lcm(5, 10))   # 10
```

---

# 🔢 **NUMBERS — Check if a Number is Harshad Number**

## ✅ What is a Harshad Number?

A number is **Harshad (Niven) number** if:

[
n % (sum of digits of n) == 0
]

### Example: `18`

Sum of digits = `1 + 8 = 9`
18 % 9 = 0 ✅ Harshad

Example: `19`
Sum = 1+9=10
19 % 10 ≠ 0 ❌ Not Harshad

---

## 🧠 Simple Steps

1. Find sum of digits
2. Check `n % sum_digits == 0`

---

# ✅ Code

```python
def is_harshad(n):
    original = n
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    return original % total == 0
```

---

## ⏱ Time Complexity (TC)

O(D) (D = number of digits)

## 📦 Space Complexity (SC)

O(1)

---

## ⭐ Test

```python
print(is_harshad(18))  # True
print(is_harshad(19))  # False
print(is_harshad(21))  # True
```

---

# 🔢 **NUMBERS — Check if a Number is Abundant or Not**

## ✅ What is an Abundant Number?

A number is **Abundant** if:

[
{Sum of proper divisors (excluding itself)} > n
]

### Example: `12`

Proper divisors: `1, 2, 3, 4, 6`
Sum = `1+2+3+4+6 = 16`
✅ 16 > 12 → **Abundant**

Example: `10`
Divisors: `1,2,5`
Sum = 8
❌ 8 < 10 → Not abundant

---

## 🧠 Simple Steps

1. Find all divisors from `1 to n-1`
2. Add divisors that divide `n`
3. If sum > n → Abundant ✅

---

# ✅ Code (Simple)

```python
def is_abundant(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total > n
```

---

## ⏱ Time Complexity (TC)

**O(N)**

## 📦 Space Complexity (SC)

**O(1)**

---

## ⭐ Test

```python
print(is_abundant(12))  # True
print(is_abundant(10))  # False
print(is_abundant(18))  # True
```

---

Perfect ✅ Tamal! Here is the **FAST VERSION (√n method)** for **Abundant Number**.

---

# ✅ Abundant Number (FAST √n Method)

## 🧠 Why √n is faster?

Divisors come in pairs:

If `i` divides `n`, then `n//i` is also a divisor.

So we loop only till **√n**.

---

# ✅ Code (Efficient)

```python
def is_abundant_fast(n):
    if n < 12:   # smallest abundant number is 12
        return False

    total = 1   # 1 is always a proper divisor
    i = 2

    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
        i += 1

    return total > n
```

---

## ⏱ Time Complexity (TC)

✅ **O(√N)**

## 📦 Space Complexity (SC)

✅ **O(1)**

---

## ⭐ Test

```python
print(is_abundant_fast(12))  # True
print(is_abundant_fast(10))  # False
print(is_abundant_fast(18))  # True
```

---


# 🔢 **NUMBERS — Sum of Digits of a Number**

### 💡 Meaning

Input: `1234`
Sum = `1 + 2 + 3 + 4 = 10`

---

## 🧠 Simple Steps

1. Take last digit using `% 10`
2. Add it to `sum`
3. Remove last digit using `// 10`
4. Repeat until number becomes 0

---

# ✅ Code

```python
def sum_of_digits(n):
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    return total
```

---

## ⏱ Time Complexity (TC)

✅ **O(D)** (D = number of digits)

## 📦 Space Complexity (SC)

✅ **O(1)**

---

## ⭐ Test

```python
print(sum_of_digits(1234))  # 10
print(sum_of_digits(507))   # 12
```

---


Great ✅🔥 Tamal!

---

# 🔢 **NUMBERS — Sum of Numbers in the Given Range**

### 💡 Meaning

If range is:
`start = 5`, `end = 10`
Sum = `5+6+7+8+9+10 = 45`

---

## ✅ Method 1 (Loop Method)

### 🧠 Logic

Just add all numbers from start to end.

```python
def sum_in_range(start, end):
    total = 0

    for num in range(start, end + 1):
        total += num

    return total
```

✅ **TC:** O(N)
✅ **SC:** O(1)

---

## ✅ Method 2 (Fastest) — Formula Method

### 🧠 Logic

Sum from 1 to n:
[
S(n) = {n(n+1)}/{2}
]

So range sum:
[
S(end) - S(start-1)
]

```python
def sum_in_range_fast(start, end):
    def sum_n(n):
        return n * (n + 1) // 2

    return sum_n(end) - sum_n(start - 1)
```

✅ **TC:** O(1)
✅ **SC:** O(1)

---

## ⭐ Test

```python
print(sum_in_range(5, 10))         # 45
print(sum_in_range_fast(5, 10))    # 45
```

---

# 🔢 **Permutations: N people can occupy R seats**

## ✅ Meaning

You have **N people** and **R seats**.
You want to know: **How many ways to seat R people out of N?**

This is called **Permutation**:

[
P(N, R) = {N!}/{(N-R)!}
]

---

## 🧠 Simple Example

N = 5 people, R = 3 seats
Ways:

[
P(5,3) = {5!}/{2!} = {120}/{2} = 60
]

---

# ✅ Code (Simple)

```python
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def npr(n, r):
    if r > n:
        return 0
    return factorial(n) // factorial(n - r)
```

---

## ⏱ Time Complexity (TC)

Factorial runs up to N → **O(N)**
Total → **O(N)**

## 📦 Space Complexity (SC)

**O(1)**

---

## ⭐ Test

```python
print(npr(5, 3))  # 60
print(npr(10, 2)) # 90
```

---


# 🔥 FAST NPR (Efficient)

## 💡 Logic

[
P(N,R) = N * (N-1) * (N-2) * ... * (N-R+1)
]

So we multiply **only R terms**, not whole factorials ✅

---

## ✅ Code

```python
def npr_fast(n, r):
    if r > n:
        return 0

    result = 1
    for i in range(r):
        result *= (n - i)

    return result
```

---

## ⏱ Time Complexity (TC)

✅ **O(R)**

## 📦 Space Complexity (SC)

✅ **O(1)**

---

## ⭐ Test

```python
print(npr_fast(5, 3))   # 60
print(npr_fast(10, 2))  # 90
```

---


Sure ✅ Tamal! Let’s do **Add Two Fractions** step-by-step.

---

# 🔢 **Program to Add Two Fractions**

### 💡 Meaning

You have two fractions:

[
\frac{a}{b} + \frac{c}{d}
]

Result:

[
\frac{a \times d + c \times b}{b \times d}
]

Then simplify the fraction using **GCD**.

---

## 🧠 Simple Steps

1. Input: `a/b` and `c/d`
2. Numerator = `a*d + c*b`
3. Denominator = `b*d`
4. Find gcd of numerator and denominator
5. Divide both by gcd

---

# ✅ Code

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def add_fractions(a, b, c, d):
    num = a * d + c * b
    den = b * d

    g = gcd(num, den)

    num //= g
    den //= g

    return num, den
```

---

## ⏱ Time Complexity (TC)

GCD takes **O(log N)**
So total → **O(log N)**

## 📦 Space Complexity (SC)

**O(1)**

---

## ⭐ Test

```python
num, den = add_fractions(1, 2, 1, 3)
print(num, "/", den)   # 5 / 6
```

✅ Because: 1/2 + 1/3 = 5/6

---


# 🔢 **Replace all 0s with 1s in a Given Integer**

### 💡 Meaning

Input: `1020`
Output: `1121`

Because every `0` becomes `1`.

---

## 🧠 Simple Logic

1. Convert number to string
2. Replace `'0'` with `'1'`
3. Convert back to int

---

# ✅ Code (Simplest)

```python
def replace_0_with_1(n):
    return int(str(n).replace('0', '1'))
```

---

## ⏱ Time Complexity (TC)

O(D) (D = digits)

## 📦 Space Complexity (SC)

O(D) (string used)

---

## ⭐ Test

```python
print(replace_0_with_1(1020))  # 1121
print(replace_0_with_1(0))     # 1
```

---


# 🔢 **Can a Number be Expressed as a Sum of Two Prime Numbers?**

### 💡 Meaning

Check if there exist primes `p` and `q` such that:

[
p + q = n
]

Example:

* `10 = 3 + 7` ✅ Yes
* `11 = 5 + 6` ❌ No (6 not prime)

---

## 🧠 Simple Steps

1. Loop `p` from 2 to n
2. If `p` is prime and `(n-p)` is prime → return True
3. Else False

---

# ✅ Code

```python
def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def can_be_sum_of_two_primes(n):
    for p in range(2, n):
        if is_prime(p) and is_prime(n - p):
            return True
    return False
```

---

## ⏱ Time Complexity (TC)

Loop + prime check → approx **O(N * √N)**

## 📦 Space Complexity (SC)

**O(1)**

---

## ⭐ Test

```python
print(can_be_sum_of_two_primes(10))  # True  (3+7)
print(can_be_sum_of_two_primes(11))  # False
```

---

# 🔢 **Calculate the Area of a Circle**

### 💡 Formula

[
Area = pi * r^2
]

Where `r` = radius

---

# ✅ Code

```python
import math

def area_of_circle(r):
    return math.pi * r * r
```

---

## ⏱ Time Complexity (TC)

**O(1)**

## 📦 Space Complexity (SC)

**O(1)**

---

## ⭐ Test

```python
print(area_of_circle(5))  # 78.53981633974483
```

✅ If you want only 2 decimal places:

```python
print(round(area_of_circle(5), 2))  # 78.54
```

---

# 🔢 **Program to Find Roots of a Quadratic Equation**

Quadratic equation format:

[
ax^2 + bx + c = 0
]

---

## ✅ Formula (Discriminant)

[
D = b^2 - 4ac
]

### Cases:

✅ If `D > 0` → **2 real roots**
✅ If `D == 0` → **1 real root (same)**
✅ If `D < 0` → **2 complex roots**

---

# ✅ Code (Handles all cases)

```python
import math

def quadratic_roots(a, b, c):
    D = b*b - 4*a*c

    if D > 0:
        root1 = (-b + math.sqrt(D)) / (2*a)
        root2 = (-b - math.sqrt(D)) / (2*a)
        return root1, root2

    elif D == 0:
        root = -b / (2*a)
        return root, root

    else:
        real = -b / (2*a)
        imag = math.sqrt(-D) / (2*a)
        return (real, imag), (real, -imag)
```

---

## ⏱ Time Complexity (TC)

**O(1)**

## 📦 Space Complexity (SC)

**O(1)**

---

## ⭐ Test

```python
print(quadratic_roots(1, -3, 2))   # (2.0, 1.0)
print(quadratic_roots(1, 2, 1))    # (-1.0, -1.0)
print(quadratic_roots(1, 2, 5))    # complex roots
```

---