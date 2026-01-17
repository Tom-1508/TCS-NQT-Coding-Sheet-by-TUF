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