# Binary Search Problem Types & Solution Approaches

Binary search isn’t just “find `x` in a sorted array.”  
Most interview/LeetCode binary search problems fall into a few common shapes. If you identify the shape, the code template becomes routine.

---

## 0) Core binary search invariants (the big idea)

Binary search works when the answer space is ordered and your check is **monotonic**:

- There is a predicate `P(mid)` that is either:
  - `False ... False, True ... True` (you want the first True), or
  - `True ... True, False ... False` (you want the last True)

You repeatedly shrink `[lo, hi]` while preserving the invariant.

---

## 1) Classic: search for a target in a sorted array

**Goal:** find index of `target` (or return -1).  
**Tell:** array is sorted; you compare `mid` to `target`.

**Template**
- `lo, hi = 0, n-1`
- while `lo <= hi`:
  - `mid = (lo+hi)//2`
  - move left/right based on comparison

**Examples**
- Standard “Binary Search”
- Search in a sorted list with distinct values

---

## 2) First / Last occurrence (lower_bound / upper_bound)

**Goal:** find boundaries for duplicates (first index of `target`, last index, count occurrences).  
**Tell:** “first occurrence”, “last occurrence”, “range of target”, duplicates exist.

### 2a) First occurrence / Lower bound (first index with `a[i] >= x`)
**Use when**
- first `target`
- insert position
- smallest index meeting a condition

### 2b) Upper bound (first index with `a[i] > x`)
**Use when**
- last occurrence is `upper_bound(x) - 1`
- count is `upper_bound(x) - lower_bound(x)`

**Examples**
- Find First and Last Position of Element in Sorted Array
- Search Insert Position

---

## 3) “Answer on a number line” (binary search on the answer)

**Goal:** find minimum/maximum feasible value when feasibility is monotonic.  
**Tell:** “minimize the maximum…”, “minimum days…”, “capacity…”, “can we do it in X…”.

**Recipe**
1. Define `feasible(x)` (can we achieve goal with parameter `x`?)
2. Ensure monotonicity:
   - if `feasible(x)` is true, then for larger `x` it stays true (or vice versa)
3. Binary search `x` over a numeric range

**Common patterns**
- **Minimize** something → find **first True**
- **Maximize** something → find **last True**

**Examples**
- Koko Eating Bananas (min speed)
- Capacity To Ship Packages Within D Days
- Split Array Largest Sum
- Min Days to Make Bouquets
- Aggressive cows / maximize minimum distance

---

## 4) Search in a rotated sorted array

**Goal:** find `target` in a rotated sorted array (with/without duplicates).  
**Tell:** array sorted but “rotated”; looks like two sorted halves.

**Key idea**
At each `mid`, **one side is sorted**:
- If left side sorted: check if target lies in `[lo..mid]`, else go right
- If right side sorted: check if target lies in `[mid..hi]`, else go left

**Examples**
- Search in Rotated Sorted Array
- Find Minimum in Rotated Sorted Array
- Rotated array with duplicates (harder: equality complicates decisions)

---

## 5) Peak / valley / “unimodal” arrays (binary search on shape)

**Goal:** find a peak, maximum, or minimum when array rises then falls (or vice versa).  
**Tell:** “peak element”, “mountain array”, unimodal function.

**Template**
- Compare `a[mid]` vs `a[mid+1]`
- If rising, move right; if falling, move left
- Often uses `lo < hi` loop with `hi = mid` / `lo = mid+1`

**Examples**
- Find Peak Element
- Peak Index in a Mountain Array

---

## 6) 2D / matrix binary search

Two common subtypes:

### 6a) Matrix is “globally sorted”
**Tell:** each row sorted AND first element of a row > last element of previous row.  
Treat as 1D array of length `m*n` and binary search.

**Example**
- Search a 2D Matrix

### 6b) Rows and columns individually sorted
Binary search per row/col doesn’t fully solve it; typical solutions use:
- “staircase” search from top-right or bottom-left (not binary search)
- or binary search on row boundaries in some variants

**Example**
- Search a 2D Matrix II (often staircase)

---

## 7) Binary search with custom predicate (first True / last True)

Sometimes you’re not searching values, but an index satisfying a condition.

**Tell:** “first index where…”, “minimum index such that…”, monotonic condition over indices.

**Examples**
- First bad version
- Minimum index with prefix sum >= X (when prefix sums are non-decreasing)

---

## 8) Common pitfalls (and how to avoid them)

### Off-by-one boundaries
Choose one of these styles and stick to it:

**A) Inclusive bounds:** `lo <= hi`
- `hi = mid - 1` / `lo = mid + 1`

**B) Half-open bounds:** `[lo, hi)` with `lo < hi`
- `hi = mid` / `lo = mid + 1`

Half-open is often cleaner for “first True”.

### Mid overflow
Use `mid = lo + (hi - lo)//2` (important in languages with 32-bit ints).

### Infinite loops
Make sure each iteration strictly shrinks the search space.

### Predicate not monotonic
If `feasible(x)` flips back and forth, binary search won’t work.

### Duplicate ambiguity in rotated arrays
When `a[lo] == a[mid] == a[hi]`, you may need to shrink edges (`lo += 1`, `hi -= 1`) which can degrade to O(n).

---

# Quick “Which binary search is this?” checklist

- Find `target` in sorted array → **Classic**
- Need first/last position or insertion point → **Lower/Upper bound**
- “Minimize/maximize X such that condition holds” → **Binary search on answer**
- Sorted but rotated → **Rotated array search**
- “Peak/mountain/unimodal” → **Peak search using neighbor comparison**
- 2D matrix special sorting → **Flattened 1D BS** (globally sorted) or **staircase** (row+col sorted)
- “first index where predicate becomes true” → **First True / last True**

---

## Handy generic templates

### First True (minimum `x` such that `P(x)` is True)
```python
lo, hi = low, high  # answer in [low, high]
while lo < hi:
    mid = (lo + hi) // 2
    if P(mid):
        hi = mid
    else:
        lo = mid + 1
return lo
