# Greedy Problem Types & Solution Approaches

Greedy means **make the locally best choice** at each step and hope it leads to a global optimum. It works when the problem has **optimal substructure** and the **greedy choice property** (a local best is part of some global best). Common patterns: **sweep and extend**, **track a bound** (farthest reach, min balance), **sort then greedy**, and **two passes / two pointers**.

---

## 0) Core idea: when greedy works

- **Optimal substructure:** an optimal solution contains optimal solutions to subproblems.
- **Greedy choice property:** making the best local choice doesn’t rule out a global optimum (e.g. “take the earliest ending interval” for max non-overlapping).
- **Typical proof:** “if an optimal solution differs from our greedy choice, we can swap and still get an optimal (or better) solution.”

If you’re stuck, ask: “what’s the one thing I can decide **right now** that won’t hurt me later?”

---

## 1) Maximum subarray (Kadane’s — extend or restart)

**Goal:** find the contiguous subarray with the largest sum.  
**Tell:** “maximum subarray”, “largest sum”, “contiguous”.

**Approach**
- **Greedy / DP:** at each index, either **extend** the current subarray (add this element) or **restart** (start fresh from here). So: `current = max(nums[i], current + nums[i])`, then `best = max(best, current)`.
- If `current + nums[i] < nums[i]`, the previous prefix hurts us; drop it and start at `nums[i]`.

**Examples**
- Maximum Subarray

---

## 2) Jump Game (can you reach the end?)

**Goal:** determine if you can get from index 0 to the last index; from index `i` you may jump up to `nums[i]` steps.  
**Tell:** “jump game”, “reach last index”, “maximum jump length”.

**Approach**
- **Greedy:** track the **farthest index** you can reach so far. For each `i`, if `i > farthest`, you’re stuck → return false. Else update `farthest = max(farthest, i + nums[i])`. If `farthest >= n-1`, return true.

**Examples**
- Jump Game

---

## 3) Jump Game II (minimum number of jumps)

**Goal:** from index 0 to last index, minimize the number of jumps (same rule: from `i` you can jump up to `nums[i]` steps).  
**Tell:** “minimum jumps”, “jump game II”.

**Approach**
- **BFS-style / greedy:** maintain **current reach** (how far we can go with `jumps` jumps) and **next reach** (how far we can go with `jumps+1`). For each index in the current “level”, update `next_reach = max(next_reach, i + nums[i])`. When we pass `current_reach`, do one more jump: `jumps += 1`, `current_reach = next_reach`. Stop when `current_reach >= n-1`.

**Examples**
- Jump Game II

---

## 4) Gas Station (circular tour)

**Goal:** given gas at each station and cost to next station, find a starting index (if any) so you can complete a full circuit without running out of gas.  
**Tell:** “gas station”, “circuit”, “can travel around”.

**Approach**
- **Key fact:** if total gas >= total cost, a solution exists. If you run out going from A to B (i.e. tank goes negative), no start in [A, B] can succeed; start from the next station after B.
- **Greedy:** one pass. Track `total_gain += gas[i] - cost[i]` and `tank += gas[i] - cost[i]`. If `tank < 0`, you can’t start from any index in the current segment; set `start = i + 1` and reset `tank = 0`. At the end, if `total_gain >= 0`, return `start`; else return -1.

**Examples**
- Gas Station

---

## 5) Hand of Straights (consecutive groups of fixed size)

**Goal:** can you partition the array into groups of size `groupSize` such that each group consists of consecutive numbers? (Each element used once.)  
**Tell:** “hand of straights”, “consecutive groups”, “group size k”.

**Approach**
- **Greedy:** use a frequency map (or sort and simulate). For the smallest remaining number `x`, we must form a group `[x, x+1, ..., x+groupSize-1]`. Decrement counts for each. If any of these is missing (count 0 when needed), return false. Repeat until all used.
- **Implementation:** sort unique values, or use a min-heap / sorted structure. For each smallest `x`, form the group and decrement; if we can’t form the group, return false.

**Examples**
- Hand of Straights

---

## 6) Merge Triplets to Form Target Triplet

**Goal:** given triplets and a target `(a, b, c)`, can you pick a subset of triplets and “merge” them (take max per dimension) to get exactly the target?  
**Tell:** “merge triplets”, “form target triplet”, “max per position”.

**Approach**
- **Greedy:** we can only **increase** each dimension (merge = max). So ignore any triplet that has a value **greater** than the target in any dimension (using it would exceed target).
- Among the rest, check if we can reach target in all three: take the max of first, second, third components over the kept triplets. If that equals target, return true.

**Examples**
- Merge Triplets to Form Target Triplet

---

## 7) Partition Labels (non-overlapping segments, each letter only in one)

**Goal:** partition the string into as many parts as possible so each letter appears in at most one part; return list of part lengths.  
**Tell:** “partition labels”, “split so each letter in one segment”.

**Approach**
- **Greedy:** for each letter, we need the **last index** where it appears (precompute last occurrence). Sweep with a pointer; maintain `end = max(end, last[s[i]])`. When `i == end`, we’ve completed a part (all letters in the part have their last occurrence ≤ end). Push length, reset start to i+1.

**Examples**
- Partition Labels

---

## 8) Valid Parenthesis String (parentheses with wildcard `*`)

**Goal:** string has `(`, `)`, and `*`; `*` can be treated as `(`, `)`, or empty. Is there a way to get a valid balanced parentheses string?  
**Tell:** “valid parenthesis string”, “wildcard”, “asterisk”.

**Approach**
- **Greedy balance range:** instead of one balance, track the **range** of possible balances: `[lo, hi]`. `(`: lo++, hi++; `)`: lo--, hi--; `*`: lo--, hi++. We must keep `lo` from going negative (can’t have more `)` than `(` so far). So: `lo = max(0, lo)` after each step. At the end, valid iff `lo == 0` (0 must be in the range).
- **Alternative:** two passes. First pass: treat `*` as `(`, check balance never negative and ends at 0 or positive. Second pass: treat `*` as `)`, check balance never negative and ends at 0. (Or single pass with low/high.)

**Examples**
- Valid Parenthesis String

---

# Quick “Which greedy pattern is this?” checklist

- Largest sum contiguous subarray → **Kadane (extend or restart)**
- Can you reach the end with max jump lengths? → **Jump Game (track farthest)**
- Minimum jumps to reach end → **Jump Game II (levels / next reach)**
- Complete a circular tour (gas vs cost) → **Gas Station (tank + total, reset start)**
- Partition into consecutive groups of size k → **Hand of Straights (smallest-first groups)**
- Merge triplets (max per dim) to get target → **Merge Triplets (discard > target, check max)**
- Partition string so each letter in one part → **Partition Labels (last index, extend end)**
- Balanced parentheses with `*` wildcard → **Valid Parenthesis String (balance range [lo, hi])**

---

## Common pitfalls (and how to avoid them)

- **Maximum subarray:** don’t reset to 0 when current sum goes negative; reset the **running segment** to start at current element (so current = nums[i], not 0).
- **Jump Game II:** don’t do a full BFS; one pass with “current reach” and “next reach” is enough. When you step past current reach, that’s one more jump.
- **Gas Station:** if total gas < total cost, no solution. When tank goes negative, the segment from current start to i is “bad”; start from i+1.
- **Hand of Straights:** you must form a group starting at the **smallest** remaining number; use a structure that gives you the minimum (sorted keys, min-heap, or sorted list).
- **Valid Parenthesis String:** one balance value isn’t enough; `*` gives multiple possibilities, so track the range [lo, hi] and clamp lo to 0.

---

## Handy templates

### Maximum subarray (Kadane)
```python
def maxSubArray(nums):
    best = current = nums[0]
    for i in range(1, len(nums)):
        current = max(nums[i], current + nums[i])
        best = max(best, current)
    return best
```

### Jump Game (reach last?)
```python
def canJump(nums):
    farthest = 0
    for i in range(len(nums)):
        if i > farthest:
            return False
        farthest = max(farthest, i + nums[i])
        if farthest >= len(nums) - 1:
            return True
    return farthest >= len(nums) - 1
```

### Partition Labels
```python
def partitionLabels(s):
    last = {c: i for i, c in enumerate(s)}
    start = end = 0
    out = []
    for i, c in enumerate(s):
        end = max(end, last[c])
        if i == end:
            out.append(end - start + 1)
            start = i + 1
    return out
```

### Valid Parenthesis String (balance range)
```python
def checkValidString(s):
    lo = hi = 0
    for c in s:
        if c == '(':
            lo, hi = lo + 1, hi + 1
        elif c == ')':
            lo, hi = lo - 1, hi - 1
        else:  # *
            lo, hi = lo - 1, hi + 1
        if hi < 0:
            return False
        lo = max(0, lo)
    return lo == 0
```
