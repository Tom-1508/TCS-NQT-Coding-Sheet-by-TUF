# ✅ SORTING — 1) Bubble Sort Algorithm

## 💡 Idea (Very Simple)

* Compare **adjacent** elements
* Swap if they are in wrong order
* Biggest element “bubbles” to the end each pass

Example:
`[5, 1, 4]`
Pass1 → `[1,4,5]`

---

## ✅ Code

```python
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr
```

---

## ⏱ Time Complexity (TC)

* Worst: **O(N²)**
* Best (already sorted): **O(N)** (because of `swapped`)

## 📦 Space Complexity (SC)

✅ **O(1)** (in-place)

---

## ⭐ Test

```python
print(bubble_sort([5, 1, 4, 2, 8]))
```

---

# ✅ SORTING — 2) Selection Sort Algorithm

## 💡 Idea (Very Simple)

* Find the **smallest element**
* Put it in the correct position (front)
* Repeat for next positions

Example:
`[5, 3, 1]`

* smallest = 1 → swap with first → `[1, 3, 5]`

---

## ✅ Code

```python
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
```

---

## ⏱ Time Complexity (TC)

✅ Worst/Best: **O(N²)**

## 📦 Space Complexity (SC)

✅ **O(1)**

---

## ⭐ Test

```python
print(selection_sort([64, 25, 12, 22, 11]))
```

---

# ✅ SORTING — 3) Insertion Sort Algorithm

## 💡 Idea (Very Simple)

* Imagine sorting cards in your hand
* Take one element and insert it into its correct position in the left (sorted) part

Example:
`[5, 3, 4]`

* Insert 3 before 5 → `[3,5,4]`
* Insert 4 between 3 and 5 → `[3,4,5]`

---

## ✅ Code

```python
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr
```

---

## ⏱ Time Complexity (TC)

* Worst: **O(N²)**
* Best (already sorted): **O(N)**

## 📦 Space Complexity (SC)

✅ **O(1)**

---

## ⭐ Test

```python
print(insertion_sort([12, 11, 13, 5, 6]))
```

---

# ✅ SORTING — 4) Merge Sort Algorithm

## 💡 Idea (Simple)

Merge Sort uses **Divide & Conquer**:

1. Divide array into 2 halves
2. Sort both halves
3. Merge both sorted halves

---

## ✅ Code (Clean)

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    i = j = 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result
```

---

## ⏱ Time Complexity (TC)

✅ **O(N log N)** (always)

## 📦 Space Complexity (SC)

✅ **O(N)** (extra array used for merging)

---

## ⭐ Test

```python
print(merge_sort([5, 2, 4, 6, 1, 3]))
```

---

# ✅ SORTING — 5) Quick Sort Algorithm

## 💡 Idea (Simple)

1. Pick a **pivot** element
2. Put smaller elements on left, bigger on right
3. Recursively sort left and right parts

---

## ✅ Code (Easy & Clean)

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    right = []

    for i in range(len(arr) - 1):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)
```

---

## ⏱ Time Complexity (TC)

* Average: ✅ **O(N log N)**
* Worst: ❌ **O(N²)** (if pivot always smallest/largest)

## 📦 Space Complexity (SC)

✅ **O(N)** (extra arrays + recursion)

---

## ⭐ Test

```python
print(quick_sort([10, 7, 8, 9, 1, 5]))
```

Expected:

```
[1, 5, 7, 8, 9, 10]
```

---
