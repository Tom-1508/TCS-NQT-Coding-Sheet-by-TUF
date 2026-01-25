# ✅ NUMBER SYSTEM — 1) Convert Binary to Decimal

### 💡 Meaning

Binary `"1011"` → Decimal `11`

Because:
[
1*2^3 + 0*2^2 + 1*2^1 + 1*2^0 = 8+0+2+1 = 11
]

---

## ✅ Method (Simple)

Loop from right to left, use power of 2.

---

## ✅ Code

```python
def binary_to_decimal(binary_str):
    decimal = 0
    power = 0

    for digit in binary_str[::-1]:
        if digit == '1':
            decimal += 2 ** power
        power += 1

    return decimal
```

---

## ⏱ Time Complexity (TC)

✅ O(N)  (N = number of bits)

## 📦 Space Complexity (SC)

✅ O(1)

---

## ⭐ Test

```python
print(binary_to_decimal("1011"))  # 11
print(binary_to_decimal("1000"))  # 8
```

---

# ✅ NUMBER SYSTEM — 2) Convert **Binary to Octal**

### 💡 Meaning

Binary → Octal conversion

Example:
Binary: `"110101"`
Octal: `"65"`

---

## 🧠 Simple Logic

✅ Octal works in groups of **3 bits**:

* Split binary from right side into groups of 3
* Convert each group to decimal (0–7)
* Join result

Example:
`110101` → `110 101`

* `110` = 6
* `101` = 5
  ✅ Result = `65`

---

## ✅ Code (Easy)

```python
def binary_to_octal(binary_str):
    # make length multiple of 3 by adding leading zeros
    while len(binary_str) % 3 != 0:
        binary_str = "0" + binary_str

    octal = ""

    for i in range(0, len(binary_str), 3):
        group = binary_str[i:i+3]
        value = int(group, 2)   # convert 3-bit group to decimal
        octal += str(value)

    return octal.lstrip("0") or "0"
```

---

## ⏱ Time Complexity (TC)

✅ O(N)

## 📦 Space Complexity (SC)

✅ O(N)

---

## ⭐ Test

```python
print(binary_to_octal("110101"))  # 65
print(binary_to_octal("1011"))    # 13
```

---
# ✅ NUMBER SYSTEM — 3) Decimal to Binary Conversion

### 💡 Meaning

Decimal `13` → Binary `"1101"`

---

## 🧠 Simple Logic

Repeated division by 2:

* Take remainder `n % 2` (this gives last binary bit)
* Update `n = n // 2`
* Reverse the collected bits

Example: 13
13%2=1
6%2=0
3%2=1
1%2=1
→ binary = `1101`

---

## ✅ Code

```python
def decimal_to_binary(n):
    if n == 0:
        return "0"

    binary = ""

    while n > 0:
        binary = str(n % 2) + binary
        n //= 2

    return binary
```

---

## ⏱ Time Complexity (TC)

✅ O(log₂ N)

## 📦 Space Complexity (SC)

✅ O(log₂ N)

---

## ⭐ Test

```python
print(decimal_to_binary(13))  # 1101
print(decimal_to_binary(0))   # 0
print(decimal_to_binary(8))   # 1000
```

---

# ✅ NUMBER SYSTEM — 4) Convert **Decimal to Octal**

### 💡 Meaning

Decimal `83` → Octal `"123"`

---

## 🧠 Simple Logic

Repeated division by 8:

* Take remainder `n % 8`
* Update `n = n // 8`
* Reverse remainders

Example: 83
83%8=3
10%8=2
1%8=1
→ octal = `123`

---

## ✅ Code

```python
def decimal_to_octal(n):
    if n == 0:
        return "0"

    octal = ""

    while n > 0:
        octal = str(n % 8) + octal
        n //= 8

    return octal
```

---

## ⏱ Time Complexity (TC)

✅ O(log₈ N)

## 📦 Space Complexity (SC)

✅ O(log₈ N)

---

## ⭐ Test

```python
print(decimal_to_octal(83))  # 123
print(decimal_to_octal(8))   # 10
```

---

# ✅ NUMBER SYSTEM — 5) Convert **Octal to Binary**

### 💡 Meaning

Octal `"65"` → Binary `"110101"`

---

## 🧠 Simple Logic (Best & Easy)

Each octal digit converts to **3-bit binary**:

Octal to Binary mapping:

* `0 → 000`
* `1 → 001`
* `2 → 010`
* `3 → 011`
* `4 → 100`
* `5 → 101`
* `6 → 110`
* `7 → 111`

Example: `"65"`

* 6 → 110
* 5 → 101
  ✅ Binary = `110101`

---

## ✅ Code

```python
def octal_to_binary(octal_str):
    mapping = {
        '0': "000", '1': "001", '2': "010", '3': "011",
        '4': "100", '5': "101", '6': "110", '7': "111"
    }

    binary = ""
    for ch in octal_str:
        binary += mapping[ch]

    return binary.lstrip("0") or "0"
```

---

## ⏱ Time Complexity (TC)

✅ O(N)  (N = number of octal digits)

## 📦 Space Complexity (SC)

✅ O(N)

---

## ⭐ Test

```python
print(octal_to_binary("65"))   # 110101
print(octal_to_binary("10"))   # 1000
```

---

# ✅ NUMBER SYSTEM — 6) Convert **Octal to Decimal**

### 💡 Meaning

Octal `"123"` → Decimal `83`

Because:
[
1\cdot8^2 + 2\cdot8^1 + 3\cdot8^0 = 64 + 16 + 3 = 83
]

---

## 🧠 Simple Logic

Loop digits left to right:
[
decimal = decimal \times 8 + digit
]

---

## ✅ Code

```python
def octal_to_decimal(octal_str):
    decimal = 0

    for ch in octal_str:
        decimal = decimal * 8 + int(ch)

    return decimal
```

---

## ⏱ Time Complexity (TC)

✅ O(N)

## 📦 Space Complexity (SC)

✅ O(1)

---

## ⭐ Test

```python
print(octal_to_decimal("123"))  # 83
print(octal_to_decimal("10"))   # 8
```

---

# ✅ NUMBER SYSTEM — 7) Convert Digits/Numbers to Words

### 💡 Meaning

Input: `123`
Output: `"One Two Three"`

Input: `507`
Output: `"Five Zero Seven"`

---

## 🧠 Simple Logic

1. Create mapping of digits → words
2. Convert number to string
3. Replace each digit using mapping

---

## ✅ Code

```python
def number_to_words(n):
    mapping = {
        '0': "Zero", '1': "One", '2': "Two", '3': "Three", '4': "Four",
        '5': "Five", '6': "Six", '7': "Seven", '8': "Eight", '9': "Nine"
    }

    s = str(n)
    result = []

    for ch in s:
        result.append(mapping[ch])

    return " ".join(result)
```

---

## ⏱ Time Complexity (TC)

✅ O(D) (D = number of digits)

## 📦 Space Complexity (SC)

✅ O(D)

---

## ⭐ Test

```python
print(number_to_words(123))   # One Two Three
print(number_to_words(507))   # Five Zero Seven
```

---