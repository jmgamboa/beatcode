# Two Pointers Problem Types & Solution Approaches

Two pointers is a family of techniques where you keep **two indices** (or iterators) and move them in a controlled way to maintain an invariant.  
It overlaps with sliding window, but is broader: pointers can move toward each other, across two arrays, or be chained (fast/slow).

---

## 1) Opposite-ends / Converging pointers (left ↔ right)

**Goal:** process pairs or enforce conditions by moving pointers from both ends inward.  
**Tell:** array/string, often **sorted**, and you’re looking for a pair/triple, palindrome checks, or minimizing/maximizing something based on ends.

**Template**
- `l = 0, r = n-1`
- While `l < r`:
  - evaluate condition using `a[l]` and `a[r]`
  - move `l` or `r` inward based on what improves the condition

**Examples**
- Two Sum II (sorted array)
- Valid Palindrome / palindrome with at most one deletion
- Container With Most Water
- Trapping Rain Water (variant with extra state)

---

## 2) Same-direction / “runner” pointers (like sliding window, but not always a window)

**Goal:** find ranges, remove duplicates, partition arrays, merge-like scans.  
**Tell:** both pointers move forward; one often “leads” and the other “follows.”

### 2a) Sliding window subtype (range maintained)
**Tell:** “longest/shortest subarray with constraint”  
(These are the classic sliding window problems.)

### 2b) Read/write pointer (in-place editing)
**Tell:** “remove duplicates”, “remove element”, “compress”, “move zeros”, “stable partition”.

**Template**
- `write = 0`
- For `read` in `[0..n-1]`:
  - if `a[read]` should stay:
    - `a[write] = a[read]`
    - `write += 1`
- return `write` (new length) or modified array

**Examples**
- Remove Duplicates from Sorted Array
- Remove Element
- Move Zeroes
- String compression (run-length encoding variants)

---

## 3) Pair / triplet finding in sorted arrays (2-sum / 3-sum patterns)

**Goal:** find pairs/triples meeting sum constraints efficiently.  
**Tell:** “find 3 numbers that sum to 0/target”, “closest sum”, “count pairs.”

**Template**
- Often sort first
- Fix one index `i`
- Use `l = i+1`, `r = n-1` to search pairs
- Move pointers based on comparison to target
- Skip duplicates carefully

**Examples**
- 3Sum / 4Sum (with nested loops + two pointers)
- 3Sum Closest
- Count pairs with sum ≤ X

---

## 4) Merging two sorted arrays / sequences

**Goal:** combine or compare two sorted lists efficiently.  
**Tell:** two inputs; both sorted; want merge, intersection, diff, or find common elements.

**Template**
- `i = j = 0`
- While `i < len(A)` and `j < len(B)`:
  - if `A[i] == B[j]`: take it; advance both
  - elif `A[i] < B[j]`: advance `i`
  - else: advance `j`

**Examples**
- Merge Sorted Array
- Intersection of Two Arrays (sorted approach)
- Find median of two sorted arrays (advanced; still pointer-ish but more binary-search heavy)

---

## 5) Partitioning (Dutch National Flag / quicksort partition style)

**Goal:** rearrange array into regions (e.g., < pivot, == pivot, > pivot) in one pass.  
**Tell:** “sort colors”, “group elements”, “partition by parity/value”.

### 5a) 2-way partition
- `l` tracks next slot for “good”
- `r` or `read` scans

**Examples**
- Move all odds before evens (stable or unstable variants)

### 5b) 3-way partition (Dutch National Flag)
**Template**
- `low = 0, mid = 0, high = n-1`
- While `mid <= high`:
  - if `a[mid]` is low group: swap low/mid, ++low, ++mid
  - elif mid group: ++mid
  - else high group: swap mid/high, --high

**Examples**
- Sort Colors

---

## 6) Fast & slow pointers (cycle detection / linked list tricks)

**Goal:** detect cycles, find middle, find cycle entry, remove nth from end.  
**Tell:** linked lists or pointer graphs; “cycle”, “middle”, “nth from end”.

**Common patterns**
- **Floyd cycle detection:** `slow += 1`, `fast += 2`
- **Find middle:** slow/fast until fast hits end
- **Nth from end:** move `fast` ahead by `n`, then move both

**Examples**
- Linked List Cycle / Cycle II
- Middle of the Linked List
- Remove Nth Node From End of List
- Happy Number (cycle on a function)

---

## 7) Multi-pointer “state machines” on strings (parsing / cleanup)

**Goal:** process strings with two indices for building output, validating, or trimming.  
**Tell:** “remove extra spaces”, “reverse words in-place-ish”, “normalize”.

**Examples**
- Reverse Words in a String (often two pointers + cleanup)
- Valid palindrome with filtering
- URLify / replace spaces

---

## 8) When two pointers works (and when it doesn’t)

Two pointers is great when movement decisions are **monotonic** or structure is helpful:
- array is **sorted**
- constraint improves by moving a pointer in one direction
- you can maintain an invariant with local updates

It struggles when:
- you need to revisit earlier elements often
- decisions aren’t monotonic
- the data isn’t sorted and sorting would break constraints (e.g., subarray order matters)

In those cases, you may need:
- hashing (set/map)
- prefix sums
- monotonic stacks/queues
- dynamic programming

---

# Quick “Which two pointers is this?” checklist

- Need pair from ends / sorted pair sum / palindrome → **Opposite-ends**
- In-place remove/compact/overwrite while scanning → **Read/write pointers**
- Triplets/quads with sum constraints → **Sort + fix + two pointers**
- Merge/intersect two sorted arrays → **Two-array pointers**
- Group elements into regions → **Partition pointers**
- Linked list cycle/middle/nth from end → **Fast & slow**

---

## Handy templates

### Opposite-ends (sorted pair sum)
```python
l, r = 0, n - 1
while l < r:
    s = a[l] + a[r]
    if s == target:
        return (l, r)
    if s < target:
        l += 1
    else:
        r -= 1
