# Backtracking Problem Types & Solution Approaches

Backtracking is **explore → try choice → recurse → undo** on a decision tree. You build a solution incrementally and backtrack when a path can’t lead to a valid result.  
Most backtracking problems are **generate all** (subsets, permutations, combinations) or **find one** (word search, N-queens).

---

## 0) Core idea: decision space + constraints

- **Decision:** at each step, what choices can we make? (include/skip, pick one of several options, place in a slot.)
- **Constraints:** when is a choice invalid? (duplicate use, sum exceeds target, invalid placement.)
- **Goal:** collect all valid **complete** states (e.g. full subset, full permutation) or find one.

Template: for each valid choice → add to state → recurse → remove from state (backtrack).

---

## 1) Subsets (include / skip each element)

**Goal:** generate all subsets of a set (no duplicates from order).  
**Tell:** “all subsets”, “power set”, “every possible subset”.

**Approach**
- One decision per index: **include** element at `i` or **skip** it.
- Recurse on `i + 1`.
- Record a copy of the current path whenever you want a “complete” subset (often at every step, so every node is a valid subset).

**Variants**
- **Subsets II:** input has duplicates; sort and skip recursion when `nums[i] == nums[i-1]` and we’re not taking the first of that duplicate group (same as “used in this level” logic).

**Examples**
- Subsets
- Subsets II
- Sum of All Subset XOR Totals (same decision tree, different aggregation)

---

## 2) Combinations (choose k from n)

**Goal:** all ways to choose `k` elements from `n` (order doesn’t matter).  
**Tell:** “combinations”, “choose k”, “all combinations of size k”.

**Approach**
- Same as subsets but **only record when path length == k**.
- Optionally prune: if “remaining elements” + “current path size” < k, stop.

**Examples**
- Combinations (e.g. “combine n choose k”)

---

## 3) Combination Sum (reuse / no reuse)

**Goal:** all unique combinations that sum to `target`. Same element may be reusable or not.  
**Tell:** “combination sum”, “all unique combinations that sum to target”.

**Approach**
- **Reuse allowed (Combination Sum):** at each step, try adding `candidates[i]` (and allow same index again) until sum exceeds target; then backtrack. To avoid duplicate combinations (e.g. [2,2,3] vs [3,2,2]), only move forward in the array (next choice starts at `i`, not `i+1`).
- **No reuse (Combination Sum II):** sort; at each step pick one element, recurse from `i+1`. Skip duplicates: if `candidates[i] == candidates[i-1]` and we didn’t use the previous one at this level, skip (otherwise duplicate combinations).

**Examples**
- Combination Sum (reuse)
- Combination Sum II (no reuse, duplicates in input)

---

## 4) Permutations (use each element exactly once)

**Goal:** all orderings of a set.  
**Tell:** “all permutations”, “all possible arrangements”.

**Approach**
- Track **used** indices (or a used set).
- For each slot (or for each step): try every **unused** element; mark used, recurse, unmark (backtrack).

**Variants**
- **Permutations II:** input has duplicates. Use a frequency map or sort + “used” array; skip when we’re choosing a duplicate and the previous equal element wasn’t used (avoids duplicate permutations).

**Examples**
- Permutations
- Permutations II

---

## 5) Letter combinations (choices per position)

**Goal:** generate all strings from a mapping (e.g. digits → letters).  
**Tell:** “letter combinations of a phone number”, “all possible strings from digits”.

**Approach**
- One decision per position (each digit): try each letter that maps from that digit; append, recurse to next position, pop (backtrack).

**Examples**
- Letter Combinations of a Phone Number

---

## 6) Generate parentheses (balance open/close)

**Goal:** all valid sequences of `n` pairs of parentheses.  
**Tell:** “generate parentheses”, “all valid combinations of n pairs”.

**Approach**
- Two choices per step: add `(` or add `)`.
- **Constraints:** open count ≤ n; close count ≤ open count (can’t close more than we’ve opened).
- Record when length == 2 * n.

**Examples**
- Generate Parentheses

---

## 7) Palindrome partitioning (partition into palindromic substrings)

**Goal:** partition string so every part is a palindrome.  
**Tell:** “palindrome partitioning”, “all ways to split into palindromes”.

**Approach**
- At each step, choose a **length** for the next segment (from current index to some end).
- Check that segment is a palindrome; if yes, add to path, recurse from rest of string, backtrack.

**Examples**
- Palindrome Partitioning

---

## 8) Grid / word search (find path in 2D)

**Goal:** find a path in a grid that spells a word (or satisfies a condition).  
**Tell:** “word search”, “path in grid”, “find word”.

**Approach**
- For each cell as potential start, DFS: try 4 (or 8) directions; mark cell visited, recurse, unmark (backtrack).
- Prune when current character doesn’t match next character of word.

**Examples**
- Word Search

---

## 9) N-Queens (place with row/column/diagonal constraints)

**Goal:** place N queens so no two attack each other; return all board configurations.  
**Tell:** “N-queens”, “all distinct solutions”.

**Approach**
- One queen per row: for row `r`, try each column `c`; check no conflict with previous queens (same col, same diagonal). Track columns and two diagonals (e.g. `r-c`, `r+c`) in sets.
- Place queen, recurse to next row, remove (backtrack).

**Examples**
- N-Queens

---

# Quick “Which backtracking pattern is this?” checklist

- All subsets / power set → **Subsets (include/skip)**
- Choose k from n (order doesn’t matter) → **Combinations**
- All combinations that sum to target → **Combination Sum** (reuse vs no reuse + duplicate handling)
- All orderings → **Permutations** (track used; handle duplicates in Permutations II)
- Digits → letters, one choice per position → **Letter combinations**
- Valid sequences of parentheses → **Generate parentheses (balance open/close)**
- Split string into palindromes → **Palindrome partitioning**
- Find path in grid spelling word → **Word search (grid DFS + backtrack)**
- Place pieces with row/col/diagonal constraints → **N-Queens**

---

## Common pitfalls (and how to avoid them)

- **Forgetting to backtrack:** always undo the choice after the recursive call (pop, unmark, remove from set).
- **Duplicate combinations (e.g. [2,2,3] vs [3,2,2]):** in combination sum, only move forward in the array (start next choice at same or next index depending on reuse). In combination sum II / subsets II, sort and skip duplicate values when the previous equal wasn’t taken at this level.
- **Duplicate permutations:** with duplicates in input, skip placing the same value again when the previous equal element wasn’t used.
- **Modifying shared state without copying:** when you add “path” to the result list, add `path.copy()` (or equivalent) so later backtracking doesn’t change the stored result.
- **Inefficient checks:** in N-queens, use sets for columns and diagonals instead of scanning the board each time.

---

## Handy templates

### Subsets (include/skip)
```python
def backtrack(i, path):
    result.append(path[:])
    for j in range(i, len(nums)):
        path.append(nums[j])
        backtrack(j + 1, path)
        path.pop()
result = []
backtrack(0, [])
```

### Permutations (use each once)
```python
def backtrack(path, used):
    if len(path) == len(nums):
        result.append(path[:])
        return
    for i in range(len(nums)):
        if used[i]:
            continue
        used[i] = True
        path.append(nums[i])
        backtrack(path, used)
        path.pop()
        used[i] = False
result = []
backtrack([], [False] * len(nums))
```

### Combination sum (reuse allowed)
```python
def backtrack(start, path, total):
    if total == target:
        result.append(path[:])
        return
    if total > target:
        return
    for i in range(start, len(candidates)):
        path.append(candidates[i])
        backtrack(i, path, total + candidates[i])  # reuse: same i
        path.pop()
```

### Generate parentheses
```python
def backtrack(open_count, close_count, path):
    if len(path) == 2 * n:
        result.append("".join(path))
        return
    if open_count < n:
        path.append("(")
        backtrack(open_count + 1, close_count, path)
        path.pop()
    if close_count < open_count:
        path.append(")")
        backtrack(open_count, close_count + 1, path)
        path.pop()
```
