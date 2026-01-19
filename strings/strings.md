# ✅ STRINGS — Problem 1

## **1) Check if a given string is palindrome or not**

### 💡 Meaning

A string is palindrome if it reads the same forward and backward.
Example:
✅ `"madam"` → palindrome
❌ `"hello"` → not palindrome

---

## 🧠 Simple Logic

Reverse the string and compare.

---

## ✅ Code (Very Simple)

```python
def is_palindrome_string(s):
    return s == s[::-1]
```

---

## ⏱ Time Complexity (TC)

**O(N)** (reversing string)

## 📦 Space Complexity (SC)

**O(N)** (new reversed string)

---

## ⭐ Test

```python
print(is_palindrome_string("madam"))  # True
print(is_palindrome_string("hello"))  # False
```

---

# ✅ STRINGS — Problem 2

## **Count number of vowels, consonants, spaces in a String**

### 💡 Meaning

Given a string, count:

* vowels (`a e i o u`)
* consonants (all other letters)
* spaces (`" "`)

Example:
Input: `"hi tamal"`
Vowels = 2 (`i, a`)
Consonants = 5 (`h, t, m, l`)
Spaces = 1

---

## 🧠 Simple Logic

1. Convert string to lowercase
2. Check each character:

* if vowel → vowels++
* else if alphabet → consonants++
* else if space → spaces++

---

## ✅ Code

```python
def count_vowels_consonants_spaces(s):
    s = s.lower()
    vowels = 0
    consonants = 0
    spaces = 0

    for ch in s:
        if ch in "aeiou":
            vowels += 1
        elif ch.isalpha():
            consonants += 1
        elif ch == " ":
            spaces += 1

    return vowels, consonants, spaces
```

---

## ⏱ Time Complexity (TC)

**O(N)**

## 📦 Space Complexity (SC)

**O(1)**

---

## ⭐ Test

```python
print(count_vowels_consonants_spaces("hi tamal"))  
# (2, 5, 1)
```

---

# ✅ STRINGS — Problem 3

## **Find the ASCII value of a character**

### 💡 Meaning

ASCII value is the numeric code for a character.

Examples:

* `'A'` → 65
* `'a'` → 97
* `'0'` → 48

---

## 🧠 Simple Logic

Use Python `ord()` function.

---

## ✅ Code

```python
def ascii_value(ch):
    return ord(ch)
```

---

## ⏱ Time Complexity (TC)

**O(1)**

## 📦 Space Complexity (SC)

**O(1)**

---

## ⭐ Test

```python
print(ascii_value('A'))  # 65
print(ascii_value('a'))  # 97
```

---
# ✅ STRINGS — Problem 4

## **Remove all vowels from the string**

### 💡 Meaning

Remove `a, e, i, o, u` (both small + capital)

Example:
Input: `"Hello World"`
Output: `"Hll Wrld"`

---

## 🧠 Simple Logic

* Loop each character
* If it’s not a vowel → keep it

---

## ✅ Code

```python
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    result = ""

    for ch in s:
        if ch not in vowels:
            result += ch

    return result
```

---

## ⏱ Time Complexity (TC)

**O(N)**

## 📦 Space Complexity (SC)

**O(N)**

---

## ⭐ Test

```python
print(remove_vowels("Hello World"))  # Hll Wrld
```

---

Perfect ✅🔥 Tamal!

---

# ✅ STRINGS — Problem 5

## **Remove spaces from a string**

### 💡 Meaning

Input: `"Hi Tamal Bro"`
Output: `"HiTamalBro"`

---

## 🧠 Simple Logic

* Loop characters
* Keep only the ones that are not `" "`

---

## ✅ Code

```python
def remove_spaces(s):
    result = ""

    for ch in s:
        if ch != " ":
            result += ch

    return result
```

---

## ⏱ Time Complexity (TC)

**O(N)**

## 📦 Space Complexity (SC)

**O(N)**

---

## ⭐ Test

```python
print(remove_spaces("Hi Tamal Bro"))  # HiTamalBro
```

---

# ✅ STRINGS — Problem 6

## **Remove characters from a string except alphabets**

### 💡 Meaning

Keep only letters (A-Z, a-z), remove everything else.

Example:
Input: `"Tamal@123!!"`
Output: `"Tamal"`

---

## 🧠 Simple Logic

* Loop each character
* If `ch.isalpha()` is True → keep it

---

## ✅ Code

```python
def keep_only_alphabets(s):
    result = ""

    for ch in s:
        if ch.isalpha():
            result += ch

    return result
```

---

## ⏱ Time Complexity (TC)

**O(N)**

## 📦 Space Complexity (SC)

**O(N)**

---

## ⭐ Test

```python
print(keep_only_alphabets("Tamal@123!!"))  # Tamal
```

---

# ✅ STRINGS — Problem 7

## **Reverse a String**

### 💡 Meaning

Input: `"hello"`
Output: `"olleh"`

---

## 🧠 Simple Logic

Use slicing `[::-1]` to reverse.

---

## ✅ Code (Simplest)

```python
def reverse_string(s):
    return s[::-1]
```

---

## ⏱ Time Complexity (TC)

**O(N)**

## 📦 Space Complexity (SC)

**O(N)**

---

## ⭐ Test

```python
print(reverse_string("hello"))  # olleh
```

---

# ✅ STRINGS — Problem 8

## **Remove brackets from an algebraic expression**

### 💡 Meaning

Remove: `(` `)` `{` `}` `[` `]`

Example:
Input: `"(a+b)*[c-d]"`
Output: `"a+b*c-d"`

---

## 🧠 Simple Logic

* Loop each character
* If it is NOT a bracket → keep it

---

## ✅ Code

```python
def remove_brackets(expr):
    brackets = "(){}[]"
    result = ""

    for ch in expr:
        if ch not in brackets:
            result += ch

    return result
```

---

## ⏱ Time Complexity (TC)

**O(N)**

## 📦 Space Complexity (SC)

**O(N)**

---

## ⭐ Test

```python
print(remove_brackets("(a+b)*[c-d]"))  # a+b*c-d
```

---

# ✅ STRINGS — Problem 9

## **Sum of the numbers in a String**

### 💡 Meaning

Extract numbers from string and sum them.

Example:
Input: `"a12b3c4"`
Numbers: 12, 3, 4
Output: **19**

---

## 🧠 Simple Logic

* Build digits together to form full numbers
* When a non-digit comes, add the formed number to sum

---

## ✅ Code (Simple)

```python
def sum_numbers_in_string(s):
    total = 0
    num = ""

    for ch in s:
        if ch.isdigit():
            num += ch
        else:
            if num != "":
                total += int(num)
                num = ""

    # add last number if string ends with digits
    if num != "":
        total += int(num)

    return total
```

---

## ⏱ Time Complexity (TC)

**O(N)**

## 📦 Space Complexity (SC)

**O(1)** (extra string `num` is small)

---

## ⭐ Test

```python
print(sum_numbers_in_string("a12b3c4"))   # 19
print(sum_numbers_in_string("100abc20"))  # 120
```

---

# ✅ STRINGS — Problem 10

## **Capitalize first and last character of each word**

### 💡 Meaning

Input: `"hello world"`
Output: `"HellO WorlD"`

(first letter uppercase + last letter uppercase)

---

## 🧠 Simple Logic

1. Split string into words
2. For each word:

   * if length = 1 → just uppercase it
   * else → uppercase first and last, keep middle same
3. Join back into a sentence

---

## ✅ Code

```python
def cap_first_last(s):
    words = s.split()
    result = []

    for w in words:
        if len(w) == 1:
            result.append(w.upper())
        else:
            new_word = w[0].upper() + w[1:-1] + w[-1].upper()
            result.append(new_word)

    return " ".join(result)
```

---

## ⏱ Time Complexity (TC)

**O(N)**

## 📦 Space Complexity (SC)

**O(N)**

---

## ⭐ Test

```python
print(cap_first_last("hello world"))   # HellO WorlD
print(cap_first_last("i am tamal"))    # I AM TamaL
```

---

# ✅ STRINGS — Problem 11

## **Calculate frequency of characters in a string**

### 💡 Meaning

Count how many times each character appears.

Example:
Input: `"aabbc"`
Output:
`a → 2`
`b → 2`
`c → 1`

---

## 🧠 Simple Logic

Use a dictionary:

* key = character
* value = count

---

## ✅ Code

```python
def char_frequency(s):
    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    return freq
```

---

## ⏱ Time Complexity (TC)

**O(N)**

## 📦 Space Complexity (SC)

**O(N)**

---

## ⭐ Test

```python
print(char_frequency("aabbc"))
# {'a': 2, 'b': 2, 'c': 1}
```

---

# ✅ STRINGS — Problem 12

## **Find Non-Repeating Characters of a String**

### 💡 Meaning

Non-repeating characters are those which appear **only once**.

Example:
Input: `"aabbcdde"`
Output: `['c', 'e']`

---

## 🧠 Simple Logic

1. Count frequency of each character
2. Print characters whose count == 1

---

## ✅ Code

```python
def non_repeating_chars(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    result = []
    for ch in s:
        if freq[ch] == 1:
            result.append(ch)

    return result
```

---

## ⏱ Time Complexity (TC)

**O(N)**

## 📦 Space Complexity (SC)

**O(N)**

---

## ⭐ Test

```python
print(non_repeating_chars("aabbcdde"))  # ['c', 'e']
```

---

# ✅ STRINGS — Problem 13

## **Check if two strings are anagram of each other**

### 💡 Meaning

Two strings are anagrams if they have **same characters with same frequency**.

Example:
✅ `"listen"` and `"silent"` → anagram
❌ `"hello"` and `"world"` → not anagram

---

# ✅ Method 1 (Simple) — Sort and Compare

### 🧠 Logic

Sort both strings → if same → anagram.

```python
def is_anagram_sort(s1, s2):
    return sorted(s1) == sorted(s2)
```

✅ **TC:** O(N log N)
✅ **SC:** O(N)

---

# ✅ Method 2 (Optimal) — Frequency Count

### 🧠 Logic

Count characters in both strings and compare.

```python
def is_anagram_optimal(s1, s2):
    if len(s1) != len(s2):
        return False

    freq = {}

    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s2:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False

    return True
```

✅ **TC:** O(N)
✅ **SC:** O(N)

---

## ⭐ Test

```python
print(is_anagram_sort("listen", "silent"))       # True
print(is_anagram_optimal("listen", "silent"))    # True
print(is_anagram_optimal("hello", "world"))      # False
```

---

# ✅ What is DP (Dynamic Programming) — in simple words

### 💡 DP = “Store answers so you don’t repeat work”

When a problem has **repeating subproblems**, DP helps you by **saving results** and reusing them.

Example:
If you calculate something again and again → DP saves time.

---

# ✅ When DP is used? (2 conditions)

A problem is DP when it has:

## ✅ 1) Overlapping Subproblems

Same small problem appears many times.

## ✅ 2) Optimal Substructure

Big problem answer depends on smaller answers.

---

# ✅ DP has 2 styles (you must know these)

## ✅ A) Memoization (Top-Down)

➡️ Recursion + Save results in dictionary/array

## ✅ B) Tabulation (Bottom-Up)

➡️ Build answers using loops in a table

---

# ✅ DP Example (Super Easy): Fibonacci

### Normal recursion (Brute ❌)

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

**Problem:** It repeats same fib calculations.

### DP Memoization ✅

```python
def fib(n, dp):
    if n <= 1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib(n-1, dp) + fib(n-2, dp)
    return dp[n]
```

### DP Tabulation ✅✅

```python
def fib(n):
    if n <= 1:
        return n
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

---

# ✅ Now DP in Strings (Your case)

String DP problems are mostly like:

✅ LCS (Longest Common Subsequence)
✅ Count common subsequences
✅ Edit distance
✅ Longest palindromic subsequence

These all work with a **2D DP table**.

---

# ✅ Understanding “Subsequence” first

Subsequence means:

* Order should remain
* Can skip characters

Example: `"abc"`
Subsequences:
✅ `""` (empty)
✅ `"a"`, `"b"`, `"c"`
✅ `"ab"`, `"ac"`, `"bc"`
✅ `"abc"`

Total subsequences = `2^n`

So brute force becomes huge quickly.

---

# ✅ Your Problem: Count Common Subsequences (Beginner view)

Given:
`s1 = "abc"`
`s2 = "abc"`

We want: how many subsequences are common?

Answer = 7 (`a b c ab ac bc abc`)
(Usually they exclude empty subsequence)

---

# ✅ Brute Force Approach (Not practical but best for understanding)

### 🧠 Idea:

1. Generate all subsequences of s1
2. Generate all subsequences of s2
3. Count common

But total subsequences = `2^n`
So brute is **very slow**.

✅ Brute code (understand only):

```python
def all_subseq(s, i, cur, res):
    if i == len(s):
        res.append(cur)
        return
    all_subseq(s, i+1, cur, res)           # skip
    all_subseq(s, i+1, cur + s[i], res)    # take

def brute_count_common(s1, s2):
    res1 = []
    res2 = []
    all_subseq(s1, 0, "", res1)
    all_subseq(s2, 0, "", res2)

    set2 = set(res2)
    count = 0
    for x in res1:
        if x != "" and x in set2:
            count += 1
    return count
```

⏱ TC: O(2^n + 2^m)
📦 SC: O(2^n + 2^m)
❌ not usable for big strings

---

# ✅ Better Approach (Still slow but improved)

Generate subsequences of smaller string and check in other (still exponential).

Not optimal.

---

# ✅ Optimal Approach = DP ✅✅✅

Now DP idea:

Instead of generating subsequences, we count them smartly.

---

## ✅ DP Table Meaning (MOST IMPORTANT PART)

Let:

`dp[i][j]` = number of common subsequences between:

* first `i` chars of s1
* first `j` chars of s2

So:

* `dp[0][*] = 0` (empty string has no non-empty common subsequence)
* `dp[*][0] = 0`

---

## ✅ Rule 1: If characters match

If `s1[i-1] == s2[j-1]`

Then common subsequences become:
✅ All from left + all from top + 1 (new ones created using this match)

So:
[
dp[i][j] = 1 + dp[i-1][j] + dp[i][j-1]
]

---

## ✅ Rule 2: If characters don’t match

Then we combine:

* dp[i-1][j] (ignore s1 char)
* dp[i][j-1] (ignore s2 char)
  But dp[i-1][j-1] gets counted twice → subtract once

So:
[
dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
]

---

# ✅ DP Code (Tabulation)

```python
def count_common_subsequences(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):

            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j] + dp[i][j-1]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

    return dp[n][m]
```

⏱ TC: **O(N×M)**
📦 SC: **O(N×M)** ✅

---

# ✅ Let me show you a tiny example table (so DP becomes clear)

s1 = `"ab"`
s2 = `"ab"`

We compute dp:

Final answer should be:
`a, b, ab` → 3

DP gives 3 ✅

---

# ✅ How to think DP for ANY string DP problem (your exam shortcut)

Whenever you see:
✅ “common”
✅ “subsequence”
✅ “two strings”
✅ “minimum operations”
✅ “match pattern”

Think:

### ✅ DP state = dp[i][j]

Meaning: answer for first `i` chars & first `j` chars

### ✅ transition depends on:

* match → take + skip
* no match → max / min / add-subtract

---

# ✅ Your personal DP learning path (1 hour crash)

### Level 1 (easy)

✅ Fibonacci
✅ Climbing stairs
✅ Min cost climbing

### Level 2 (strings)

✅ LCS length
✅ Longest palindromic subsequence
✅ Edit distance (basic)

### Level 3 (counting DP)

✅ Count distinct subsequences
✅ Count common subsequences (this one)

---

# ✅ Your Exam Advice (Tomorrow)

⚡ If DP comes, mostly they ask:
✅ **LCS length**
✅ **Longest common substring**
✅ Basic counting logic

This “count common subsequences” is slightly advanced, but now you know the DP idea.

---

# ✅ STRINGS — Count Common Subsequence in Two Strings

## 💡 Meaning (Very Simple)

You are given 2 strings:

`s1 = "abc"`
`s2 = "abc"`

A **subsequence** means you can pick characters **in order**, but you can skip some.

Example subsequences of `"abc"`:

* `"a"`, `"b"`, `"c"`
* `"ab"`, `"ac"`, `"bc"`
* `"abc"`

✅ **Common subsequences** are subsequences that exist in **both strings**.

---

# ✅ Most Common Interpretation in Coding Sheets

They usually mean:

## ✅ Count of **Common Subsequence = LCS Count**

But **counting all common subsequences** is a **DP problem** (harder).

So I’ll give you the **standard DP solution** (correct).

---

# ✅ DP Idea (Simple)

Let `dp[i][j]` = number of common subsequences between:

`s1[0...i-1]` and `s2[0...j-1]`

### If characters match:

```
dp[i][j] = 1 + dp[i-1][j] + dp[i][j-1]
```

### If characters don’t match:

```
dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
```

✅ `+1` means adding the new subsequence formed by matching characters.

---

# ✅ Code (Standard DP)

```python
def count_common_subsequences(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j] + dp[i][j - 1]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

    return dp[n][m]
```

---

## ⏱ Time Complexity (TC)

✅ **O(N × M)**

## 📦 Space Complexity (SC)

✅ **O(N × M)**

---

## ⭐ Test

```python
print(count_common_subsequences("abc", "abc"))   # 7
```

✅ Output `7` because common subsequences are:
`a, b, c, ab, ac, bc, abc`

---

# ✅ LCS = Longest Common Subsequence

### 💡 Meaning

You have two strings, find the **longest subsequence** that is common in both.

✅ Subsequence = order same, can skip characters.

---

## ✅ Example 1

`s1 = "abcde"`
`s2 = "ace"`

Common subsequence = `"ace"`
✅ LCS length = **3**

---

## ✅ Example 2

`s1 = "abc"`
`s2 = "dc"`

Common subsequence = `"c"`
✅ LCS length = **1**

---

# ✅ Why DP?

Because brute force tries all subsequences = `2^n` ❌

DP makes it **fast** ✅

---

# ✅ DP Meaning (Most Important)

Let:

### ✅ `dp[i][j]` = LCS length of

`s1[0...i-1]` and `s2[0...j-1]`

So:

* `dp[0][j] = 0` (empty string has no common subsequence)
* `dp[i][0] = 0`

---

# ✅ DP Rules (Very Simple)

### ✅ Case 1: Characters match

If `s1[i-1] == s2[j-1]`

Then this character is part of LCS:

[
dp[i][j] = 1 + dp[i-1][j-1]
]

✅ “take it and move diagonally”

---

### ✅ Case 2: Characters don’t match

If `s1[i-1] != s2[j-1]`

Then we try both options:

* skip char from s1 → `dp[i-1][j]`
* skip char from s2 → `dp[i][j-1]`

Take maximum:

[
dp[i][j] = max(dp[i-1][j], dp[i][j-1])
]

✅ “skip one and take best”

---

# ✅ LCS Code (Tabulation)

```python
def lcs_length(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]
```

---

## ⏱ Time Complexity (TC)

✅ **O(N × M)**

## 📦 Space Complexity (SC)

✅ **O(N × M)**

---

# ⭐ Test

```python
print(lcs_length("abcde", "ace"))   # 3
print(lcs_length("abc", "dc"))      # 1
```

---

# ✅ Super Quick DP Table Understanding (1 line)

When characters match → go **diagonal +1**
When not match → go **max(top, left)**

---


Perfect ✅🔥 Tamal!

Now let’s upgrade:

# ✅ LCS Part 2: **Print the actual LCS string** (not only length)

---

## 🧠 Simple Idea

1. First build the DP table (same as before)
2. Start from `dp[n][m]`
3. Move back:

   * If characters match → take that char and go diagonally
   * Else move towards the bigger value (top or left)

---

# ✅ Code: Print LCS String

```python
def lcs_string(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # build dp table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # backtrack to build LCS string
    i, j = n, m
    lcs = []

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs.append(s1[i - 1])
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

    return "".join(reversed(lcs))
```

---

## ⏱ Time Complexity (TC)

✅ **O(N × M)**

## 📦 Space Complexity (SC)

✅ **O(N × M)**

---

## ⭐ Test

```python
print(lcs_string("abcde", "ace"))   # ace
print(lcs_string("AGGTAB", "GXTXAYB"))  # GTAB
```

---



Perfect ✅ Tamal!
Now we do:

# ✅ **Longest Common Substring** (NOT subsequence)

---

## 💡 Difference (Super Important)

### ✅ Subsequence

Order matters, can skip.
Example: `"abcde"` & `"ace"` → `"ace"` ✅

### ✅ Substring

Must be **continuous** (no skipping).
Example: `"abcde"` & `"abfce"` → `"ab"` ✅

---

# ✅ Problem

Given two strings, find the **length of the longest common substring**.

Example:
`s1 = "abcdxyz"`
`s2 = "xyzabcd"`
Longest common substring = `"abcd"`
✅ Answer = 4

---

# ✅ DP Meaning

Let:

### ✅ `dp[i][j]` = length of longest common substring

ending at `s1[i-1]` and `s2[j-1]`

---

## ✅ Rules

### ✅ If characters match

```
dp[i][j] = 1 + dp[i-1][j-1]
```

### ❌ If not match

```
dp[i][j] = 0
```

(because substring must be continuous)

Also keep a `max_len`.

---

# ✅ Code (Simple)

```python
def longest_common_substring_length(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_len = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                max_len = max(max_len, dp[i][j])
            else:
                dp[i][j] = 0

    return max_len
```

---

## ⏱ Time Complexity (TC)

✅ **O(N × M)**

## 📦 Space Complexity (SC)

✅ **O(N × M)**

---

# ⭐ Test

```python
print(longest_common_substring_length("abcdxyz", "xyzabcd"))  # 4
print(longest_common_substring_length("abc", "ac"))          # 1
```

---

# ✅ Print the **Longest Common Substring** (not only length)

---

## 🧠 Idea

While filling DP, whenever we get a bigger length:

* store `end_index = i` (where substring ends in s1)
* later substring is: `s1[end_index-max_len : end_index]`

---

# ✅ Code (Print substring + length)

```python
def longest_common_substring(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_len = 0
    end_index = 0   # end position in s1

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]

                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_index = i
            else:
                dp[i][j] = 0

    substring = s1[end_index - max_len : end_index]
    return substring, max_len
```

---

## ⏱ Time Complexity (TC)

✅ **O(N × M)**

## 📦 Space Complexity (SC)

✅ **O(N × M)**

---

## ⭐ Test

```python
sub, length = longest_common_substring("abcdxyz", "xyzabcd")
print(sub, length)   # abcd 4
```

---


Yes Tamal ✅🔥
Greedy is **super important** for company exams, and it’s easy once you get the mindset.

I’ll introduce Greedy in the **most beginner-friendly** way, and then we’ll connect it to the **wildcard matching greedy** you just used.

---

# ✅ What is Greedy Algorithm? (Beginner Definition)

### 💡 Greedy = “Take the best decision RIGHT NOW”

Instead of thinking about all future possibilities, Greedy chooses the **best choice at the current step** and moves on.

✅ It works when:

* The current best choice leads to the final best answer.

---

# ✅ Simple Real-life Example

You have ₹100 and want maximum chocolates:

* you always pick the **cheapest chocolate first**
  This is “greedy choice”.

---

# ✅ Typical Greedy Pattern

Greedy problems usually look like:

✅ “minimum / maximum”
✅ “best / optimal”
✅ “choose intervals / tasks / elements”
✅ “match pattern”
✅ “reduce something fast”

---

# ✅ Greedy vs Brute vs DP (Very Simple)

### ❌ Brute Force:

Try all possible paths → slow

### ✅ DP:

Try all but smartly save answers → fast but complex

### ✅ Greedy:

Don’t try all → just choose best now → fastest, simplest

---

# ✅ Now understand the Wildcard Greedy (the one I gave)

### Pattern has:

* `?` = match 1 char
* `*` = match 0 or more chars

The **hardest part is `*`** because it can match many lengths.

---

## ✅ Greedy trick for `*`

When we see `*`, we **don’t decide immediately** how many characters it will take.

Instead we say:

✅ “I will remember this `*`, and if mismatch happens later, I will expand it”

That’s exactly greedy + backup.

---

# ✅ Variables in Greedy Wildcard Code (Very Important)

### `i` → pointer in text

### `j` → pointer in pattern

### `star_idx`

Stores the position of last `*` in pattern
➡️ “Where is the last `*` that I can use to fix mismatch?”

### `match_idx`

Stores the text position where `*` started matching
➡️ “How many characters `*` has taken so far?”

---

# ✅ Step-by-Step Example (Understand it deeply)

### Text = `"abcd"`

### Pattern = `"a*d"`

Expected ✅ True (`* = bc`)

---

### ✅ Start

```
i=0, j=0
text[i]=a , pattern[j]=a ✅ match
i=1, j=1
```

---

### ✅ Now pattern[j] = '*'

We don’t match anything yet, just “save star”

```
star_idx = j = 1
match_idx = i = 1
j = 2
```

---

### ✅ Now compare:

```
text[i] = b
pattern[j] = d
Mismatch ❌
```

But we have a `*` saved ✅

So we say:
✅ “let star take one more character from text”

```
j = star_idx + 1  -> 2   (retry matching after '*')
match_idx += 1    -> 2
i = match_idx     -> 2
```

Meaning:
`*` matched `"b"`

---

### ✅ Now compare:

```
text[i] = c
pattern[j] = d
Mismatch ❌
```

Again, use star:

```
match_idx = 3
i = 3
```

Now `*` matched `"bc"`

---

### ✅ Now compare:

```
text[i] = d
pattern[j] = d ✅ match
i=4, j=3
```

Text finished ✅
Pattern finished ✅
➡️ Return True ✅

---

# ✅ Why this works?

Because `*` is flexible.

Greedy strategy is:
✅ Try to match with smallest usage of `*`
❌ If mismatch → increase `*` gradually

This avoids DP and is super fast.

---

# ✅ One more example (important)

Text: `"aa"`
Pattern: `"a"`

Steps:

* `a` matches first `a`
* text left still has `a`
* pattern ended
  ➡️ mismatch and no `*`
  ✅ return False

---

# ✅ Greedy Summary in 4 lines (cheat-sheet)

✅ If match / `?` → move both pointers
✅ If `*` → save star position, move pattern pointer
✅ If mismatch and star exists → expand star (move text pointer)
✅ If mismatch and no star → false

---

# ✅ Now your homework (2 quick checks)

Tell me True/False without running:

1. text = `"abcdef"`, pattern = `"a*ef"`
2. text = `"abcd"`, pattern = `"a*c?"`

Reply answers like:
`1) True, 2) False`

Then I’ll confirm and move you to next string topic ✅




# ✅ STRINGS — Wildcard Pattern Matching

## **Check if two strings match where one string contains wildcard characters**

### 💡 Wildcards meaning (most common)

In pattern string:

* `?` → matches **exactly 1 character**
* `*` → matches **0 or more characters**

✅ Example:

* Text: `"abcd"` Pattern: `"a?cd"` → ✅ True (`? = b`)
* Text: `"abcd"` Pattern: `"a*d"` → ✅ True (`* = bc`)
* Text: `"abcd"` Pattern: `"a*c"` → ❌ False

---

# ✅ Method 1 (Best & Easy) — Greedy (No DP)

## 🧠 Simple Idea

We use 2 pointers:

* `i` for text
* `j` for pattern

Also store:

* `star_idx` = where `*` occurred in pattern
* `match_idx` = where we started matching after `*`

This is the most used optimal solution.

---

## ✅ Code (Greedy)

```python
def wildcard_match(text, pattern):
    i = 0  # text pointer
    j = 0  # pattern pointer
    star_idx = -1
    match_idx = 0

    while i < len(text):

        # Case 1: match or '?'
        if j < len(pattern) and (pattern[j] == text[i] or pattern[j] == '?'):
            i += 1
            j += 1

        # Case 2: '*'
        elif j < len(pattern) and pattern[j] == '*':
            star_idx = j
            match_idx = i
            j += 1

        # Case 3: mismatch but we had a previous '*'
        elif star_idx != -1:
            j = star_idx + 1
            match_idx += 1
            i = match_idx

        # Case 4: mismatch and no '*'
        else:
            return False

    # skip remaining '*' in pattern
    while j < len(pattern) and pattern[j] == '*':
        j += 1

    return j == len(pattern)
```

---

## ⏱ Time Complexity (TC)

✅ **O(N + M)** (almost linear)

## 📦 Space Complexity (SC)

✅ **O(1)**

---

# ⭐ Test

```python
print(wildcard_match("abcd", "a?cd"))  # True
print(wildcard_match("abcd", "a*d"))   # True
print(wildcard_match("abcd", "a*c"))   # False
print(wildcard_match("aa", "*"))       # True
print(wildcard_match("aa", "a"))       # False
print(wildcard_match("aa", "a*"))      # True
```

---

# ✅ Wildcard Matching using DP (Pattern has `?` and `*`)

## 💡 DP Meaning

Let:

### ✅ `dp[i][j] = True/False`

Means:

* first `i` characters of **text**
* match first `j` characters of **pattern**

---

## ✅ Rules

### ✅ If pattern char is normal letter or `?`

If they match:

```
dp[i][j] = dp[i-1][j-1]
```

### ✅ If pattern char is `*`

`*` can match:

* empty → dp[i][j-1]
* one or more chars → dp[i-1][j]

So:

```
dp[i][j] = dp[i][j-1] OR dp[i-1][j]
```

---

# ✅ DP Code (Simple)

```python
def wildcard_match_dp(text, pattern):
    n = len(text)
    m = len(pattern)

    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True

    # text empty, pattern can match only if all are '*'
    for j in range(1, m + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if pattern[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

            elif pattern[j - 1] == '?' or pattern[j - 1] == text[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            else:
                dp[i][j] = False

    return dp[n][m]
```

---

## ⏱ Time Complexity (TC)

✅ **O(N × M)**

## 📦 Space Complexity (SC)

✅ **O(N × M)**

---

## ⭐ Test

```python
print(wildcard_match_dp("abcd", "a?cd"))  # True
print(wildcard_match_dp("abcd", "a*d"))   # True
print(wildcard_match_dp("abcd", "a*c"))   # False
```

---

# ✅ STRINGS — Return Maximum Occurring Character

### 💡 Meaning

Find the character that appears **maximum times** in the string.

Example:
Input: `"aabbbcc"`
Output: `'b'` (because b occurs 3 times)

---

## 🧠 Simple Logic

1. Use a dictionary to count frequency of each character
2. Track max frequency
3. Return the character with highest frequency

✅ If there is a tie, we return the one that appears **first** (common expectation)

---

# ✅ Code (Simple + Exam Friendly)

```python
def max_occurring_char(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    max_char = s[0]
    max_count = freq[max_char]

    for ch in s:
        if freq[ch] > max_count:
            max_count = freq[ch]
            max_char = ch

    return max_char
```

---

## ⏱ Time Complexity (TC)

✅ **O(N)**

## 📦 Space Complexity (SC)

✅ **O(N)**

---

## ⭐ Test

```python
print(max_occurring_char("aabbbcc"))  # b
print(max_occurring_char("tamal"))    # a (appears 2 times)
```

---
Sure ✅ Tamal! Very common question.

---

# ✅ STRINGS — Remove all duplicates from the input string

### 💡 Meaning

Remove repeated characters and keep only **one occurrence**.

Example:
Input: `"aabbccdd"`
Output: `"abcd"`

Input: `"programming"`
Output: `"progamin"` (first occurrence kept)

---

## 🧠 Simple Logic (Keep order)

1. Use a `set` to store seen characters
2. If character not seen → add to result
3. If already seen → skip

---

# ✅ Code (Best for exam)

```python
def remove_duplicates(s):
    seen = set()
    result = ""

    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result += ch

    return result
```

---

## ⏱ Time Complexity (TC)

✅ **O(N)**

## 📦 Space Complexity (SC)

✅ **O(N)**

---

## ⭐ Test

```python
print(remove_duplicates("aabbccdd"))     # abcd
print(remove_duplicates("programming"))  # progamin
```

---

# ✅ STRINGS — Print all the duplicates in the input string

### 💡 Meaning

Print characters that appear **more than 1 time**.

Example:
Input: `"aabbcdd"`
Duplicates: `a, b, d`

---

## 🧠 Simple Logic

1. Count frequency using dictionary
2. Print chars whose count > 1

---

# ✅ Code (Simple)

```python
def print_duplicates(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    result = []
    for ch, count in freq.items():
        if count > 1:
            result.append(ch)

    return result
```

---

## ⏱ Time Complexity (TC)

✅ **O(N)**

## 📦 Space Complexity (SC)

✅ **O(N)**

---

## ⭐ Test

```python
print(print_duplicates("aabbcdd"))   # ['a', 'b', 'd']
print(print_duplicates("abcd"))      # []
```

---

# ✅ STRINGS — Remove characters from first string present in second string

### 💡 Meaning

Remove all characters from `s1` that are present in `s2`.

Example:
`s1 = "abcdef"`
`s2 = "bd"`
Output = `"acef"` ✅
(b and d removed)

---

## 🧠 Simple Logic

1. Convert `s2` into a set (fast lookup)
2. Build result from `s1` only if char not in set

---

# ✅ Code

```python
def remove_chars(s1, s2):
    remove_set = set(s2)
    result = ""

    for ch in s1:
        if ch not in remove_set:
            result += ch

    return result
```

---

## ⏱ Time Complexity (TC)

✅ **O(N + M)**

## 📦 Space Complexity (SC)

✅ **O(M)**

---

## ⭐ Test

```python
print(remove_chars("abcdef", "bd"))     # acef
print(remove_chars("tamal", "am"))      # tl
```

---

# ✅ 1) Change every letter to the next lexicographic alphabet

### Example: `"abcd"` → `"bcde"`, `"z"` → `"a"`

```python
def next_lexicographic(s):
    res = ""
    for ch in s:
        if 'a' <= ch <= 'z':
            res += 'a' if ch == 'z' else chr(ord(ch) + 1)
        elif 'A' <= ch <= 'Z':
            res += 'A' if ch == 'Z' else chr(ord(ch) + 1)
        else:
            res += ch
    return res
```

✅ TC: O(N) | ✅ SC: O(N)

---

# ✅ 2) Find the largest word in a given string

(largest = longest length)

```python
def largest_word(s):
    words = s.split()
    if not words:
        return ""
    ans = words[0]
    for w in words:
        if len(w) > len(ans):
            ans = w
    return ans
```

✅ TC: O(N) | ✅ SC: O(N)

---

# ✅ 3) Sort characters in a string

```python
def sort_characters(s):
    return "".join(sorted(s))
```

✅ TC: O(N log N) | ✅ SC: O(N)

---

# ✅ 4) Count number of words in a given string

```python
def count_words(s):
    return len(s.split())
```

✅ TC: O(N) | ✅ SC: O(N)

---

# ✅ 5) Find word with highest number of repeated letters

Example: `"apple banana"` → `"banana"` (a repeated 3 times)

```python
def word_highest_repeated_letters(s):
    words = s.split()
    best_word = ""
    best_repeat = -1

    for w in words:
        freq = {}
        for ch in w:
            freq[ch] = freq.get(ch, 0) + 1

        max_in_word = max(freq.values())  # highest repetition in this word

        if max_in_word > best_repeat:
            best_repeat = max_in_word
            best_word = w

    return best_word
```

✅ TC: O(N) | ✅ SC: O(K) per word

---

# ✅ 6) Change case of each character in a string

(lower → upper, upper → lower)

```python
def toggle_case(s):
    res = ""
    for ch in s:
        if ch.islower():
            res += ch.upper()
        elif ch.isupper():
            res += ch.lower()
        else:
            res += ch
    return res
```

✅ TC: O(N) | ✅ SC: O(N)

---

# ✅ 7) Concatenate one string with another

```python
def concatenate_strings(s1, s2):
    return s1 + s2
```

✅ TC: O(N+M) | ✅ SC: O(N+M)

---

# ✅ 8) Find substring in a string (print starting position)

(0-based index, if not found → -1)

```python
def find_substring(s, sub):
    return s.find(sub)
```

✅ TC: O(N*M) worst | ✅ SC: O(1)

✅ If want 1-based position:

```python
def find_substring_1based(s, sub):
    idx = s.find(sub)
    return idx + 1 if idx != -1 else -1
```

---

# ✅ 9) Reverse words in a string

Example: `"I am Tamal"` → `"Tamal am I"`

```python
def reverse_words(s):
    words = s.split()
    words.reverse()
    return " ".join(words)
```

✅ TC: O(N) | ✅ SC: O(N)

---

# ✅ Quick Testing Block (Copy-Paste)

```python
print(next_lexicographic("abcz"))                 # bcda
print(largest_word("hi this is tamal"))           # tamal
print(sort_characters("tamal"))                   # aalm t? (sorted)
print(count_words("I am Tamal"))                  # 3
print(word_highest_repeated_letters("apple banana orange"))  # banana
print(toggle_case("TaMaL123"))                    # tAmAl123
print(concatenate_strings("hello", "world"))      # helloworld
print(find_substring("hello world", "world"))     # 6
print(reverse_words("I am Tamal"))                # Tamal am I
```

---
