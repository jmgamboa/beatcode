# Sliding Window Problem Types & Solution Approaches

Sliding window problems mostly fall into a few recurring “shapes.”  
If you can identify the shape, the solution template is almost automatic.

---

## 1) Fixed-size window

**Goal:** compute something over every window of size `k` (max sum, average, #distinct, etc.)  
**Tell:** window size never changes.

**Template**
- Build the first window
- Slide the window:
  - add the new right element
  - remove the old left element

**Examples**
- Maximum sum of subarray length `k`
- Find if any anagram of `p` occurs in `s` (fixed `len(p)`)

---

## 2) Variable-size window with a constraint (expand–shrink)

**Goal:** longest/shortest subarray/substring that satisfies a condition  
**Tell:** phrases like “at most k …”, “no more than …”, “sum ≤ …”, “distinct ≤ k”, etc.

**Template**
- Expand `r` (include new element)
- While constraint is violated, shrink `l` (remove left elements)
- Update answer:
  - **Longest:** update whenever window is valid
  - **Shortest:** update when it becomes valid, then shrink to minimize

**Examples**
- Longest substring with at most `k` distinct characters
- Minimum length subarray with sum ≥ `S` (**usually requires non-negative numbers**)
- Longest subarray with sum ≤ `S` (**non-negative**)

**Key note:** This relies on “shrinking helps” (monotonicity).  
It often breaks when numbers can be negative for sum constraints.

---

## 3) “Exactly K” constraints (built from “at most”)

**Goal:** count windows that satisfy “exactly K” of something  
**Tell:** “exactly K distinct”, “exactly K odds”, etc.

**Common trick**
- `count(exactly K) = count(at most K) - count(at most K-1)`

**Examples**
- Subarrays with exactly `K` distinct integers
- “Nice subarrays” (exactly `K` odd numbers)

---

## 4) Best window ending at `r` (last-seen / index jump)

**Goal:** constraints like “no repeats” where you can jump `l` forward directly  
**Tell:** you can identify the *precise* position causing the violation (e.g., last occurrence).

**Template**
- Maintain map: `last_pos[value]`
- If violation at `r`:
  - `l = max(l, last_pos[value] + 1)`
- Update: `last_pos[value] = r`

**Examples**
- Longest substring without repeating characters
- Longest subarray with all unique values

**Why it’s nice:** often avoids inner `while` loops.

---

## 5) Frequency matching windows (anagram/permutation / “covering”)

Two common subtypes:

### 5a) Fixed-length frequency match
**Goal:** window frequency equals target frequency  
Usually **fixed window size** (pattern length).

**Approach**
- Keep counts for window + target
- Maintain a “matched” counter (how many characters meet required counts)

**Examples**
- Find all anagrams of `p` in `s`
- Check if any permutation of `p` exists in `s`

### 5b) Minimum covering window (cover all required counts)
**Goal:** smallest window that covers all required characters (with multiplicity)

**Template**
- Expand until covered
- Shrink to minimal while still covered
- Track best

**Examples**
- Minimum window substring
- Smallest subarray containing all required items (with duplicates)

---

## 6) Windows with “budget” (replace / flip problems)

**Goal:** you can “fix” up to `k` bad elements (replacements, flips, deletions) and want the longest window  
**Tell:** “at most k replacements/flips/deletions”.

**Template**
- Expand
- Track a “badness” metric
- Shrink while `badness > k`

**Examples**
- Longest repeating character replacement
- Max consecutive ones with at most `k` zeros flipped

---

## 7) Circular / wrap-around windows

**Goal:** array/string is circular and windows can wrap around.

**Approaches**
- Duplicate the array/string: `arr2 = arr + arr`, then use windows with a max length cap
- Or use modular indexing carefully

**Examples**
- Pattern search in circular strings
- Some circular max/min window problems (sometimes Kadane-like variants)

---

## 8) When sliding window *doesn’t* apply (common traps)

Sliding window needs a property like:
- **Non-negative numbers** for sum constraints (expand increases sum, shrink decreases)
- A constraint that predictably becomes valid by shrinking
- Or a direct jump via last-seen indices / monotonic behavior

**Classic trap:** negative numbers + shortest subarray with sum ≥ `K`  
Plain sliding window fails.

**Common alternatives**
- **Prefix sums + deque (monotonic queue)** for shortest subarray with sum ≥ `K` (works with negatives)
- **Prefix sums + hashmap** for exact-sum counting problems

---

# Quick “Which template do I use?” checklist

- Window size is constant `k` → **Fixed-size**
- “Longest/shortest with at most …” → **Variable-size expand–shrink**
- “Exactly K …” → **AtMost(K) - AtMost(K-1)**
- “No repeats / jump to last occurrence” → **Last-seen index jump**
- “Anagram / pattern counts” → **Frequency matching**
- “Replace/flip up to k” → **Budget window**
- Negatives + sum constraints → **Prefix sums + deque**, not plain sliding window
