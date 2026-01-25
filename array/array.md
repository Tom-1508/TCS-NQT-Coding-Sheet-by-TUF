  # ✅ **ARRAYS — Problem 1**

## **1) Find the smallest number in an array**

### **💡 Explanation (Very Simple)**

* We look at each number one by one.
* We keep a variable `smallest`.
* If we find a number smaller than it → update.

### **🧠 Step-by-step**

1. Assume the first element is the smallest.
2. Compare it with every other number.
3. If any number is smaller → replace `smallest`.
4. Return the final smallest number.

### **✅ Code**

```python
def smallest(arr):
    smallest = arr[0]        # assume 1st element is smallest
    for num in arr:          # go through each number
        if num < smallest:   # check if smaller
            smallest = num   # update
    return smallest
```

1️⃣ Find the Smallest Number

TC: O(N)
SC: O(1)
(Just one loop, no extra space)

---

# ✅ **ARRAYS — Problem 2**

## **2) Find the largest number in an array**

### **💡 Explanation**

* Same idea as smallest.
* Keep a variable `largest`.
* If a number is bigger → update.

### **🧠 Step-by-step**

1. Assume first number is the largest.
2. Check all numbers.
3. If we find a bigger one → update.

### **✅ Code**

```python
def largest(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest
```

2️⃣ Find the Largest Number

TC: O(N)
SC: O(1)

```python
print(smallest([5,2,9,1,6]))
print(largest([5,2,9,1,6]))
```

---

# ✅ **ARRAYS — Problem 3**

## **3) Second Smallest & Second Largest Number in an Array**

We will solve this in a simple, easy-to-understand way.

---

## **💡 Explanation (Very Simple)**

### **To find Second Smallest:**

1. First find the **smallest** number.
2. Then go through the array again and find the smallest number **greater than the smallest**.

### **To find Second Largest:**

1. First find the **largest** number.
2. Then find the largest number **smaller than the largest**.

We do it in **two passes** (very easy logic).

---

# ✅ **Step-by-step Code**

```python
def second_smallest(arr):
    # Step 1: find the smallest
    smallest = min(arr)

    # Step 2: find the smallest number greater than smallest
    second = float('inf')
    for num in arr:
        if smallest < num < second:
            second = num

    return second if second != float('inf') else None
```

```python
def second_largest(arr):
    # Step 1: find the largest
    largest = max(arr)

    # Step 2: find the largest number smaller than largest
    second = float('-inf')
    for num in arr:
        if second < num < largest:
            second = num

    return second if second != float('-inf') else None
```
3️⃣ Second Smallest & Second Largest

TC: O(N)
(We scan the array twice — still O(N))
SC: O(1)


# ⭐ Try It

```python
print(second_smallest([5, 2, 9, 1, 6]))
print(second_largest([5, 2, 9, 1, 6]))
```

Expected output:

```
2
6
```

---


# ✅ **ARRAYS — Problem 4**

## **4) Reverse a Given Array**

### **💡 Explanation (super simple)**

We use two pointers:

* **Left pointer** → starts at beginning
* **Right pointer** → starts at end
* Swap both
* Move left forward and right backward
* Until they cross

This reverses the array **in-place** (without creating a new array).

---

# ✅ **Step-by-step Code**

```python
def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # swap elements
        arr[left], arr[right] = arr[right], arr[left]

        # move pointers
        left += 1
        right -= 1

    return arr
```

4️⃣ Reverse an Array

TC: O(N)
(Swapping from both ends)
SC: O(1)
(In-place, no new array created)

# ⭐ Try It

```python
print(reverse_array([1,2,3,4,5]))
```

Expected:

```
[5,4,3,2,1]
```

---


# ✅ **ARRAYS — Problem 5**

## **5) Count Frequency of Each Element in an Array**

### **💡 Explanation (Very Simple)**

We want to count how many times each number appears.

We will use a dictionary:

* Key → number
* Value → how many times it appears

### **⏱ Time Complexity**

O(N) — we scan the array once.

### **📦 Space Complexity**

O(N) — dictionary can store up to N different elements.

---

# 🧠 Step-by-step Logic

1. Create an empty dictionary → `freq = {}`
2. For each number:

   * If not in dictionary → put it with count 1
   * If already there → increase its count
3. Return the dictionary

---

# ✅ **Code**

```python
def frequency(arr):
    freq = {}  # dictionary to store count

    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    return freq
```
# ⭐ Try It

```python
print(frequency([1,2,2,3,3,3]))
```

Expected output:

```
{1: 1, 2: 2, 3: 3}
```

---

# ✅ **ARRAYS — Problem 6**

## **6) Rearrange Array in Increasing–Decreasing Order**

### **💡 What the problem means**

You must rearrange the array like this:

* First smallest
* Then largest
* Then second smallest
* Then second largest
* And so on...

Example:
Input → `[1, 2, 3, 4, 5, 6]`
Output → `[1, 6, 2, 5, 3, 4]`

---

## **🧠 Simple Explanation**

1. First sort the array.
   Example sorted: `[1,2,3,4,5,6]`
2. Keep two pointers:

   * `left` at start (small values)
   * `right` at end (big values)
3. Pick one from left → then one from right → repeat.

---

## ✔️ Code (Very Simple)

```python
def rearrange_inc_dec(arr):
    arr = sorted(arr)           # step 1: sort
    left = 0
    right = len(arr) - 1
    result = []

    while left <= right:
        result.append(arr[left])   # smallest
        left += 1
        if left <= right:
            result.append(arr[right])  # largest
            right -= 1

    return result
```

---

## ⏱ **Time Complexity**

* Sorting the array → **O(N log N)**
* Two-pointer rearranging → **O(N)**
  **Total:** **O(N log N)**

## 📦 **Space Complexity**

* We create a new list → **O(N)**

## ⭐ Try It

```python
print(rearrange_inc_dec([1,2,3,4,5,6]))
```

Expected:

```
[1, 6, 2, 5, 3, 4]
```

---

# ✅ **ARRAYS — Problem 7**

## **7) Calculate Sum of Elements of an Array**

### **💡 Explanation (Very Simple)**

We keep a variable `total = 0`
Then we add each element to `total` one by one.

---

## ✔️ Code

```python
def sum_of_array(arr):
    total = 0
    for num in arr:
        total += num
    return total
```

---

## ⏱ Time Complexity

**O(N)** — we loop once through the array.

## 📦 Space Complexity

**O(1)** — we only use one variable (`total`).

## ⭐ Try It

```python
print(sum_of_array([1,2,3,4,5]))
```

Expected:

```
15
```

---


# ✅ **ARRAYS — Problem 8**

## **8) Rotate Array by K Elements (Left Rotation)**

We will solve using **simple method** (easy) — not block swap, because block swap is complicated and rarely needed in exams unless asked.

If you still want block-swap after this, I will teach it separately.

---

# 💡 **What is Array Rotation?**

Left rotation by **K** means:

`[1,2,3,4,5]`, K = 2
After rotation → `[3,4,5,1,2]`

We simply “cut” the array at K and move the first part to the end.

---

# 🧠 **Simple Explanation**

Steps for left rotate by K:

1. Normalize K:
   If K > length → `K = K % n`
2. Return array from index K to end
3. Then add the first K elements at the end

Example:
K = 2
`arr[K:] = [3,4,5]`
`arr[:K] = [1,2]`
Concatenate → `[3,4,5,1,2]`

---

# ✔️ **Very Simple Code**

```python
def left_rotate(arr, k):
    n = len(arr)
    
    k = k % n  # handle large k

    return arr[k:] + arr[:k]
```

---

# ⏱ **Time Complexity**

Slicing takes O(N)
So total → **O(N)**

# 📦 **Space Complexity**

New array created → **O(N)**

# ⭐ **Try It**

```python
print(left_rotate([1,2,3,4,5], 2))
```

Expected:

```
[3, 4, 5, 1, 2]
```

---

# ✅ **ARRAYS — Problem 9**

## **9) Average of All Elements in an Array**

### 💡 **Simple Explanation**

Average = (sum of elements) / (number of elements)

Example:
Array = `[2, 4, 6]`
Sum = 12
Count = 3
Average = `12 / 3 = 4`

---

# ✔️ Code

```python
def average(arr):
    if len(arr) == 0:
        return None   # avoid division by zero
    
    total = 0
    for num in arr:
        total += num

    return total / len(arr)
```

---

# ⏱ **Time Complexity**

O(N) — loop through the array.

# 📦 **Space Complexity**

O(1) — only one variable used.

# ⭐ Try It

```python
print(average([2,4,6,8]))
```

Expected:

```
5.0
```

---

# ✅ **ARRAYS — Problem 10**

## **10) Find the Median of an Array**

### 💡 **Simple Explanation**

**Median** means the **middle value** after sorting.

There are two cases:

### **Case 1 — Odd number of elements**

Example: `[3, 1, 5]` → sorted → `[1, 3, 5]`
Middle element = **3** → median is 3

### **Case 2 — Even number of elements**

Example: `[4, 2, 9, 6]` → sorted → `[2, 4, 6, 9]`
Two middle elements = 4 and 6
Median = (4 + 6) / 2 = **5**

---

# ✔️ Code

```python
def find_median(arr):
    arr = sorted(arr)
    n = len(arr)
    mid = n // 2

    if n % 2 != 0:  
        # odd length
        return arr[mid]
    else:
        # even length = average of middle two
        return (arr[mid - 1] + arr[mid]) / 2
```

---

# ⏱ **Time Complexity**

Sorting takes **O(N log N)**
Other operations are O(1)

Total → **O(N log N)**

# 📦 **Space Complexity**

Sorted copy → **O(N)**
(If we sort the same array in-place, then O(1))

---

# ⭐ Try It

```python
print(find_median([3,1,5]))
print(find_median([4,2,9,6]))
```

Expected:

```
3
5.0
```

---

# ✅ **ARRAYS — Problem 11**

## **11) Remove Duplicates From a Sorted Array**

This is a classic **two-pointer** problem.

---

# 💡 **Simple Explanation**

Since the array is **already sorted**, duplicates will always be **next to each other**.

We want to create a version with **only unique elements**, keeping order.

### We use two pointers:

* **i (write pointer)** → position where the next unique element should go
* **j (read pointer)** → moves through array checking numbers

### Steps:

1. Start `i = 1` (first element is always unique)
2. Loop `j` from 1 to end
3. If `arr[j] != arr[j-1]`, it's a new unique number → write it at `arr[i]`, then `i += 1`
4. After loop, the first `i` elements are unique

---

# ✔️ Code

```python
def remove_duplicates_sorted(arr):
    if len(arr) == 0:
        return []

    i = 1  # write pointer

    for j in range(1, len(arr)):
        if arr[j] != arr[j - 1]:
            arr[i] = arr[j]
            i += 1

    return arr[:i]   # only unique part
```

---

# ⏱ **Time Complexity**

O(N) → single pass through the array.

# 📦 **Space Complexity**

O(1) → in-place, no extra array used (except final slice).

---

# ⭐ Try It

```python
print(remove_duplicates_sorted([1,1,2,2,3,4,4,4,5]))
```

Expected:

```
[1, 2, 3, 4, 5]
```
---

# ✅ **ARRAYS — Problem 12**

## **12) Remove Duplicates From an Unsorted Array**

### 💡 **Simple Explanation**

The array is **not sorted**, so duplicates can appear anywhere.

We use a **set** to track which elements we have already seen.

### Steps:

1. Create an empty set → `seen`
2. Create an empty list → `result`
3. For each element in array:

   * If not in `seen`, add to set and add to result
   * If already in `seen`, skip
4. Return the result list

This keeps the **original order** of elements.

---

# ✔️ Code

```python
def remove_duplicates_unsorted(arr):
    seen = set()
    result = []

    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result
```

---

# ⏱ **Time Complexity**

O(N)
(Set lookup is O(1) average case)

# 📦 **Space Complexity**

O(N)
(Set + result list store all unique elements)

# ⭐ Try It

```python
print(remove_duplicates_unsorted([4, 2, 4, 5, 2, 3, 1]))
```

Expected:

```
[4, 2, 5, 3, 1]
```

---

# ✅ **ARRAYS — Problem 13**

## **13) Adding an Element in an Array**

### 💡 **Simple Explanation**

In Python, arrays (lists) are dynamic.
So adding an element is simply:

* Use `append()` → adds at the end

Or

* Create a new array with the extra element.

---

# ✔️ Code (Using append)

```python
def add_element(arr, x):
    arr.append(x)
    return arr
```

### 🔍 Example

```python
print(add_element([1,2,3], 10))
```

Output:

```
[1, 2, 3, 10]
```

---

# ⏱ **Time Complexity**

* `append()` is **O(1)** average case.

# 📦 **Space Complexity**

* **O(1)** — no extra space (except dynamic resizing internally by Python).

---

If the exam wants “fixed-size array logic”, then you create a new array:

---

# ✔️ Code (Fixed-size style)

```python
def add_element_new(arr, x):
    new_arr = arr + [x]
    return new_arr
```

**TC:** O(N) (because new array is created)
**SC:** O(N)

---

# ✅ **ARRAYS — Problem 14**

## **14) Find All Repeating Elements in an Array**

### 💡 **Simple Explanation**

We want elements that appear **more than once**.

Steps:

1. Use a dictionary to count occurrences
2. Loop through dictionary
3. Collect the keys whose count > 1

This gives all repeating elements.

---

# ✔️ Code

```python
def repeating_elements(arr):
    freq = {}
    result = []

    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for num, count in freq.items():
        if count > 1:
            result.append(num)

    return result
```

---

# ⏱ **Time Complexity**

* Building frequency map → O(N)
* Checking frequencies → O(N)

Total → **O(N)**

# 📦 **Space Complexity**

* Dictionary stores counts → **O(N)**

# ⭐ Try It

```python
print(repeating_elements([1,2,3,2,3,4,5,3]))
```

Expected:

```
[2, 3]
```

---
# ✅ **ARRAYS — Problem 15**

## **15) Find All Non-Repeating Elements in an Array**

### 💡 **Simple Explanation**

Non-repeating elements are those that appear **exactly once**.

Steps:

1. Count occurrences using a dictionary
2. Pick only numbers whose count == 1

Very similar to the previous question.

---

# ✔️ Code

```python
def non_repeating_elements(arr):
    freq = {}
    result = []

    # Count occurrences
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Collect only elements that appear once
    for num, count in freq.items():
        if count == 1:
            result.append(num)

    return result
```

---

# ⏱ **Time Complexity**

O(N) — two loops but still linear.

# 📦 **Space Complexity**

O(N) — dictionary + output list.


# ⭐ Try It

```python
print(non_repeating_elements([1,2,2,3,4,4,5]))
```

Expected:

```
[1, 3, 5]
```

---




# ✅ **ARRAYS — Problem 16**

## **16) Find All Symmetric Pairs in an Array**

### 💡 **What is a symmetric pair?**

If we have pairs like:

```
(1, 2)
(3, 4)
(2, 1)
(5, 6)
(4, 3)
```

Symmetric pairs are the ones where:

* (a, b) and (b, a) both exist

So output should be:

```
(1, 2)
(3, 4)
```

(because (1,2) ↔ (2,1) and (3,4) ↔ (4,3))

---

# 🧠 **Simple Explanation**

We do this:

1. Create a dictionary `seen`
2. For every pair `(a, b)`:

   * Check if we have earlier seen `(b, a)`
   * If yes → symmetric pair found
   * Otherwise store `seen[a] = b`

---

# ✔️ Code

```python
def symmetric_pairs(pairs):
    seen = {}
    result = []

    for a, b in pairs:
        # check if reverse pair exists
        if b in seen and seen[b] == a:
            result.append((a, b))
        else:
            seen[a] = b

    return result
```

---

# ⏱ **Time Complexity**

O(N) — we process each pair once.

# 📦 **Space Complexity**

O(N) — dictionary stores pairs.

---

# ⭐ Try It

```python
pairs = [(1,2), (3,4), (5,6), (2,1), (4,3)]
print(symmetric_pairs(pairs))
```

Expected:

```
[(2, 1), (4, 3)]
```

(Your output order may differ — that’s fine)

---

# ✅ **ARRAYS — Problem 17**

## **17) Maximum Product Subarray**

### 💡 **Goal**

Find a subarray (continuous elements) whose **product is maximum**.

Example:

```
[2,3,-2,4]
Maximum product subarray = 6 (because 2×3 = 6)
```

---

# 🧠 **Why this problem is tricky?**

Because of **negative numbers**.

* Negative × Negative = Positive
* So sometimes a small negative number can later turn into the **maximum product**, if another negative appears.

So we must track:

* `max_ending_here` → maximum product ending at current index
* `min_ending_here` → minimum product ending at current index (because negative can flip)

At each step:

* If the current number is negative → swap max and min
* Update max and min
* Update result

---

# ✔️ **Very Clean Code**

```python
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
```

---

# ⏱ **Time Complexity**

O(N) — one pass through array.

# 📦 **Space Complexity**

O(1) — uses only a few variables.

---

# ⭐ Try It

```python
print(max_product_subarray([2,3,-2,4]))      # 6
print(max_product_subarray([-2,0,-1]))        # 0
print(max_product_subarray([-2,-3,4]))        # 24
```

---


# ✅ **ARRAYS — Problem 18**

## **18) Replace Each Element of the Array by Its Rank**

### 💡 **What does “rank” mean?**

Rank means the **position of the element when the array is sorted**.

Example:

```
arr = [40, 10, 30, 20]

Sorted → [10, 20, 30, 40]

Ranks:
10 → 1
20 → 2
30 → 3
40 → 4

Final answer → [4, 1, 3, 2]
```

---

# 🧠 **Simple Explanation**

1. Sort the array and keep **unique elements**
2. Create a dictionary:
   key = element, value = its rank (starting from 1)
3. Replace each element of original array using this dictionary

---

# ✔️ Code

```python
def replace_by_rank(arr):
    sorted_unique = sorted(set(arr))  # step 1: sort unique values

    # step 2: create rank map
    rank = {}
    for i, value in enumerate(sorted_unique):
        rank[value] = i + 1

    # step 3: replace each element by its rank
    result = []
    for num in arr:
        result.append(rank[num])

    return result
```


# ⏱ **Time Complexity**

* Sorting → O(N log N)
* Creating ranks → O(N)
* Replacing values → O(N)

**Total:** O(N log N)

# 📦 **Space Complexity**

O(N) — storing rank map + result array.

---

# ⭐ Try It

```python
print(replace_by_rank([40, 10, 30, 20]))
```

Expected:

```
[4, 1, 3, 2]
```

---

# ✅ **ARRAYS — Problem 19**

## **19) Sort Elements of an Array by Frequency**

### 💡 **What does this mean?**

We must sort elements so that:

* Elements with **higher frequency** come first
* If two elements have the **same frequency**, sort by **value (ascending)**

Example:

```
Input:  [2, 3, 2, 4, 5, 12, 2, 3, 3]
Freq:   2 →3 times, 3 →3 times, 4 →1, 5 →1, 12 →1

Sorted by frequency:
[2, 2, 2, 3, 3, 3, 4, 5, 12]
```

---

# 🧠 **Simple Explanation**

1. Count frequencies using a dictionary
2. Sort the array using a key:

   * First by **negative frequency** (to get higher freq first)
   * Then by number itself

Python allows custom sorting easily.

---

# ✔️ Code

```python
def sort_by_frequency(arr):
    # Step 1: count frequencies
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # Step 2: sort by (-frequency, number)
    arr_sorted = sorted(arr, key=lambda x: (-freq[x], x))

    return arr_sorted
```

---

# ⏱ **Time Complexity**

* Counting: O(N)
* Sorting: O(N log N)

**Total:** O(N log N)

# 📦 **Space Complexity**

O(N) → frequency dictionary + sorted output


# ⭐ Try It

```python
print(sort_by_frequency([2,3,2,4,5,12,2,3,3]))
```

Expected:

```
[2, 2, 2, 3, 3, 3, 4, 5, 12]
```

---


# ✅ **ARRAYS — Problem 20**

## **20) Rotation of Elements of Array — Left and Right**

We will implement **simple rotation**, not block-swap.

---

# 💡 **Left Rotation**

Move elements to the left by **K positions**.

Example:
`[1,2,3,4,5]` left rotate by 2 → `[3,4,5,1,2]`

---

# 💡 **Right Rotation**

Move elements to the right by **K positions**.

Example:
`[1,2,3,4,5]` right rotate by 2 → `[4,5,1,2,3]`

---

# 🧠 **Simple Logic**

Use slicing:

### Left Rotate:

```
arr[k:] + arr[:k]
```

### Right Rotate:

Right rotation by K is same as left rotation by `n-k`:

```
arr[n-k:] + arr[:n-k]
```

---

# ✔️ Code

```python
def rotate_left(arr, k):
    n = len(arr)
    k = k % n
    return arr[k:] + arr[:k]
```

```python
def rotate_right(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]
```

---

# ⏱ **Time Complexity**

O(N) — slicing takes linear time.

# 📦 **Space Complexity**

O(N) — new array created.

---

# ⭐ Try It

```python
print(rotate_left([1,2,3,4,5], 2))   # [3,4,5,1,2]
print(rotate_right([1,2,3,4,5], 2))  # [4,5,1,2,3]
```

---

# ✅ **ARRAYS — Problem 21**

## **21) Find Equilibrium Index of an Array**

### 💡 **Meaning**

An index **i** is called an *equilibrium index* if:

```
sum of elements on left of i  ==  sum of elements on right of i
```

Example:

```
arr = [1, 3, 5, 2, 2]

Left sums:    [ ,1,1+3,1+3+5,1+3+5+2]
Right sums:   [3+5+2+2,5+2+2,2+2,2, ]

Equilibrium index = 2 (0-based)
because:
sum left  = 1 + 3 = 4
sum right = 2 + 2 = 4
```

---

# 🧠 **Simple Explanation**

Instead of calculating left sum and right sum repeatedly, we do this:

1. Compute total sum of array
2. Keep a variable `left_sum = 0`
3. Loop through array:

   * Reduce current number from `total` → this becomes **right sum**
   * If `left_sum == right_sum`, index found
   * Add current number to `left_sum`

Very efficient.

---

# ✔️ Code

```python
def equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    result = []

    for i in range(len(arr)):
        total_sum -= arr[i]   # now total_sum is right sum

        if left_sum == total_sum:
            result.append(i)

        left_sum += arr[i]

    return result
```

---

# ⏱ **Time Complexity**

O(N) — just one loop.

# 📦 **Space Complexity**

O(1) — except output list of indices.

---

# ⭐ Try It

```python
print(equilibrium_index([1, 3, 5, 2, 2]))
```

Expected:

```
[2]
```

---


# ✅ **ARRAYS — Problem 22**

## **22) Circular Rotation of Array by K Positions**

### 💡 **Meaning**

Circular rotation means elements wrap around like a circle.

It is the **same as left or right rotation**, because rotation is naturally circular.

Example (right rotation):

```
arr = [1,2,3,4,5]
K = 2

Output = [4,5,1,2,3]
```

---

# 🧠 **Simple Explanation**

Right circular rotation by K →
Take last K elements and put them at front.

Left rotation by K →
Take first K elements and put them at end.

This is identical to the rotate functions we wrote earlier.

---

# ✔️ Code (Right Circular Rotation)

```python
def circular_rotate_right(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]
```

---

# ✔️ Code (Left Circular Rotation)

```python
def circular_rotate_left(arr, k):
    n = len(arr)
    k = k % n
    return arr[k:] + arr[:k]
```

---

# ⏱ **Time Complexity**

O(N)

# 📦 **Space Complexity**

O(N)

---

# ⭐ Try It

```python
print(circular_rotate_right([1,2,3,4,5], 2))
print(circular_rotate_left([1,2,3,4,5], 2))
```

---



# ✅ **ARRAYS — Problem 23**

## **23) Sort an Array According to the Order Defined by Another Array**

### 💡 **Problem Meaning**

You are given:

* **Main array:** arr
* **Order array:** order

You must sort `arr` so that:

1. Elements appear **in the same order** as they appear in `order`
2. Elements not in `order` should come at the end, **sorted normally**

### Example:

```
arr    = [2, 1, 2, 5, 7, 1, 9, 3]
order  = [2, 1, 8, 3]

Output = [2, 2, 1, 1, 3, 5, 7, 9]
```

Why?

* `2` appears first in order → take all 2s
* then `1` → take all 1s
* then `8` → does not exist, ignore
* then `3` → take all 3s
* remaining elements not in order: `[5,7,9]` → sort them → append

---

# 🧠 **Simple Explanation**

1. Count frequencies of elements in arr
2. For each element in `order`, append that element’s frequency to result
3. Remove these from the count
4. Append all remaining elements sorted

---

# ✔️ Code

```python
def sort_by_another(arr, order):
    # Step 1: frequency map
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    result = []

    # Step 2: process elements in 'order'
    for val in order:
        if val in freq:
            result.extend([val] * freq[val])
            del freq[val]  # remove processed element

    # Step 3: process remaining items sorted
    remaining = []
    for val, count in freq.items():
        remaining.extend([val] * count)

    result.extend(sorted(remaining))
    return result
```

---

# ⏱ **Time Complexity**

* Frequency counting → O(N)
* Processing order array → O(M)
* Sorting leftovers → O(K log K)

Worst case → **O(N log N)**

# 📦 **Space Complexity**

O(N) → frequency map + result array

---

# ⭐ Try It

```python
print(sort_by_another(
    [2,1,2,5,7,1,9,3],
    [2,1,8,3]
))
```

Expected:

```
[2, 2, 1, 1, 3, 5, 7, 9]
```

---

# ✅ **ARRAYS — Problem 24**

# **24) Search an Element in an Array**

We will learn **two methods**:

1️⃣ **Linear Search** → works on any array
2️⃣ **Binary Search** → works only on **sorted** arrays

---

# ✔️ **1) Linear Search (Very Simple)**

### 💡 Explanation

* Go through the array one by one
* If element matches → return its index
* If not found → return -1

### Code

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

### ⏱ Time Complexity

O(N)

### 📦 Space Complexity

O(1)

---

# ✔️ **2) Binary Search (Faster, but requires sorted array)**

### 💡 Explanation

Binary search divides the array into halves:

1. Check middle element
2. If target is smaller → search left half
3. If target is bigger → search right half
4. Repeat until found or left > right

### Code

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

### ⏱ Time Complexity

O(log N)

### 📦 Space Complexity

O(1)

---

# ⭐ Try It

```python
print(linear_search([4,2,7,1,9], 7))           # 2
print(binary_search([1,2,3,4,5,6,7], 4))      # 3
```

---

# ✅ **ARRAYS — Problem 25**

## **25) Check if One Array Is a Subset of Another Array**

### 💡 **Meaning**

Array B is a subset of Array A if **every element in B appears in A**.

Example:

```
A = [1,2,3,4,5]
B = [2,3,5] → YES (subset)
C = [2,6] → NO (6 is missing)
```

---

# 🧠 **Simple Explanation**

We use a **set**, because searching in a set is O(1).

Steps:

1. Convert bigger array (A) into a set
2. Loop through B
3. If any element is *not* in the set → NOT a subset
4. If all elements found → YES

---

# ✔️ Code

```python
def is_subset(arrA, arrB):
    setA = set(arrA)

    for num in arrB:
        if num not in setA:
            return False
    return True
```

---

# ⏱ **Time Complexity**

* Set creation → O(N)
* Loop through subset array → O(M)

Total → **O(N + M)**

# 📦 **Space Complexity**

O(N) — set stores all elements of A

---

# ⭐ Try It

```python
print(is_subset([1,2,3,4,5], [2,3,5]))  # True
print(is_subset([1,2,3,4,5], [2,6]))    # False
```

---

# 🎉 **Congratulations, Tamal!**

You have completed the **entire Arrays section** of your exam sheet!
You’re doing amazing 🔥🔥

---
