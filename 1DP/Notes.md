# 1D Dynamic Programming Problem Types & Solution Approaches

1D DP means the state is **one index** (or one “position”) and you derive it from **smaller indices** or from a **bounded set of previous states**. Common patterns: **linear recurrence** (stairs, cost), **take/skip** (robber), **prefix/suffix decomposition** (decode ways, word break), **subarray ending at i** (max product), **LIS ending at i**, and **subset sum** (partition, coin change).

---

## 0) Core idea: state and recurrence

- **State:** `dp[i]` = best (or count/possible) for the subproblem up to index `i` (or “using first i elements”).
- **Recurrence:** express `dp[i]` in terms of `dp[i-1]`, `dp[i-2]`, or in general `dp[j]` for `j < i`.
- **Base case:** `dp[0]`, `dp[1]`, or an empty/subset base.
- **Order:** fill in increasing `i` (or sometimes reverse for space optimization).
- **Answer:** often `dp[n]` or `max(dp[:])` or `dp[target]`.

---

## 1) Climbing stairs (linear recurrence)

**Goal:** number of distinct ways to climb to the top (each step: 1 or 2 steps).  
**Tell:** “climbing stairs”, “ways to reach top”, “1 or 2 steps”.

**Approach**
- `dp[i]` = number of ways to reach step `i`. `dp[i] = dp[i-1] + dp[i-2]` (come from i-1 or i-2). Base: `dp[0] = 1`, `dp[1] = 1` (or `dp[1]=1`, `dp[2]=2`). Can reduce to two variables (fibonacci).

**Examples**
- Climbing Stairs

---

## 2) Min cost climbing stairs (linear + cost)

**Goal:** start at index 0 or 1, climb to past the last index; from step `i` you pay `cost[i]` and can go to i+1 or i+2. Minimize total cost.  
**Tell:** “min cost climbing stairs”, “minimum cost to reach top”.

**Approach**
- `dp[i]` = minimum cost to **reach** step `i` (and then you can step from it). `dp[i] = cost[i] + min(dp[i-1], dp[i-2])`. Base: `dp[0] = cost[0]`, `dp[1] = cost[1]`. Answer: `min(dp[n-1], dp[n-2])` (we can end by stepping from last or second-last).

**Examples**
- Min Cost Climbing Stairs

---

## 3) House robber (take or skip)

**Goal:** max sum of non-adjacent elements (can’t rob two adjacent houses).  
**Tell:** “house robber”, “non-adjacent”, “max sum”.

**Approach**
- `dp[i]` = max money from robbing houses `0..i` (and we may or may not rob `i`). Recurrence: `dp[i] = max(dp[i-1], nums[i] + dp[i-2])` (skip i, or take i and skip i-1). Base: `dp[0] = nums[0]`, `dp[1] = max(nums[0], nums[1])`. Can use two variables (prev, curr).

**Examples**
- House Robber

---

## 4) House robber II (circular)

**Goal:** same as House Robber but houses are in a **circle** (first and last are adjacent).  
**Tell:** “house robber II”, “circular”, “first and last adjacent”.

**Approach**
- Run the same DP **twice**: (1) exclude the last house (rob houses `0..n-2`), (2) exclude the first house (rob houses `1..n-1`). Answer = `max(rob_linear(0, n-2), rob_linear(1, n-1))`.

**Examples**
- House Robber II

---

## 5) Longest palindromic substring (expand or 2D)

**Goal:** find the longest substring that is a palindrome.  
**Tell:** “longest palindromic substring”, “longest palindrome”.

**Approach**
- **Expand around center:** for each center (character or between two characters), expand while equal; track max length and start. O(n²) time, O(1) space.
- **DP (2D):** `dp[i][j]` = whether `s[i:j+1]` is a palindrome; fill for increasing length; track longest. Often 1D DP notes still list this as “substring” — implementation can be 2D or expand.

**Examples**
- Longest Palindromic Substring

---

## 6) Palindromic substrings (count)

**Goal:** count how many substrings are palindromic.  
**Tell:** “palindromic substrings”, “count palindromes”.

**Approach**
- **Expand around center:** for each center, expand and count every valid palindrome (odd and even length). Increment count each time expansion succeeds.
- **DP (2D):** `dp[i][j]` = is `s[i:j+1]` palindrome; count all true. Same recurrence as longest palindromic substring.

**Examples**
- Palindromic Substrings

---

## 7) Decode ways (prefix choices)

**Goal:** a string of digits can be decoded as letters (1→A, …, 26→Z). One digit or two digits per character. Count number of ways to decode.  
**Tell:** “decode ways”, “ways to decode”, “digits to letters”.

**Approach**
- `dp[i]` = number of ways to decode `s[:i]`. From position `i`, we can take one digit (if `s[i-1]` != '0') or two digits (if `s[i-2:i]` in "10".."26"). So `dp[i] = (dp[i-1] if valid 1-char) + (dp[i-2] if valid 2-char)`. Base: `dp[0] = 1`, handle first one or two chars.

**Examples**
- Decode Ways

---

## 8) Coin change (unbounded knapsack / min coins)

**Goal:** minimum number of coins (from given denominations) that sum to `amount`; unlimited supply.  
**Tell:** “coin change”, “minimum coins”, “sum to amount”.

**Approach**
- `dp[a]` = minimum number of coins to make sum `a`. For each coin `c`: if `a >= c`, `dp[a] = min(dp[a], 1 + dp[a-c])`. Initialize `dp[0] = 0`, `dp[a] = inf` for a > 0. Fill in increasing `a`.

**Examples**
- Coin Change

---

## 9) Maximum product subarray (track min and max)

**Goal:** contiguous subarray with the **largest product**.  
**Tell:** “maximum product subarray”, “largest product”, “contiguous”.

**Approach**
- Negative × negative = positive, so we need both **max** and **min** product ending at each index. Let `maxHere = max(nums[i], maxHere * nums[i], minHere * nums[i])`, `minHere = min(nums[i], maxHere_old * nums[i], minHere * nums[i])`. Update global max. One pass, O(1) space.

**Examples**
- Maximum Product Subarray

---

## 10) Word break (segment into words)

**Goal:** can the string `s` be segmented into space-separated words from a dictionary?  
**Tell:** “word break”, “segment into words”, “dictionary”.

**Approach**
- `dp[i]` = can we segment `s[:i]`? For each `i`, for each word in dict: if `s[i-len(word):i] == word` and `dp[i-len(word)]` is true, then `dp[i] = true`. Base: `dp[0] = true`. Answer: `dp[len(s)]`.

**Examples**
- Word Break

---

## 11) Longest increasing subsequence (LIS ending at i)

**Goal:** length of the longest strictly increasing subsequence (not necessarily contiguous).  
**Tell:** “longest increasing subsequence”, “LIS”, “subsequence”.

**Approach**
- **O(n²):** `dp[i]` = length of LIS **ending at** index `i`. `dp[i] = 1 + max(dp[j] for j < i and nums[j] < nums[i])`. Answer = max(dp).
- **O(n log n):** “patience sorting” — maintain a list of “tails” of increasing length; binary search to update. Length of that list = LIS length.

**Examples**
- Longest Increasing Subsequence

---

## 12) Partition equal subset sum (subset sum)

**Goal:** can we partition the array into two subsets with equal sum? (So: is there a subset that sums to `total/2`?)  
**Tell:** “partition equal subset sum”, “split into two equal sum”, “subset sum”.

**Approach**
- If total is odd, impossible. Else target = total/2. `dp[j]` = can we form sum `j` using (some subset of) the numbers seen so far? Iterate over numbers; for each, update `dp` **backwards** from target to 0: `dp[j] |= dp[j - num]` so we don’t reuse the same element. Base: `dp[0] = true`. Answer: `dp[target]`.

**Examples**
- Partition Equal Subset Sum

---

# Quick “Which 1D DP pattern is this?” checklist

- Ways to climb (1 or 2 steps) → **Linear recurrence (fibonacci-like)**
- Min cost to climb (pay per step) → **Linear + cost**
- Max sum non-adjacent → **Take or skip (House Robber)**
- Circular non-adjacent → **Run twice, exclude first or last**
- Longest palindromic substring → **Expand around center or 2D DP**
- Count palindromic substrings → **Expand or 2D DP**
- Ways to decode digits → **Decode ways (1 or 2 digit prefix)**
- Min coins for amount → **Unbounded knapsack (coin change)**
- Max product contiguous subarray → **Track max and min ending at i**
- Segment string into dictionary words → **Word break (prefix match)**
- Longest increasing subsequence → **LIS ending at i (O(n²)) or patience O(n log n)**
- Partition into two equal sum subsets → **Subset sum (1D, iterate backwards)**

---

## Common pitfalls (and how to avoid them)

- **House Robber II:** don’t run one pass with “first and last” special case; run two separate linear robber runs (exclude first, exclude last).
- **Decode ways:** handle `'0'` — single digit `'0'` is invalid; two digits `"10"`, `"20"` are valid. Don’t double-count.
- **Coin change:** initialize `dp[0] = 0` and others as “infinity”; fill in **increasing** amount order.
- **Maximum product subarray:** one variable isn’t enough; negative can become max later. Keep both max and min ending at current index.
- **Word break:** match **suffix** of `s[:i]` with a word; ensure `dp[i - len(word)]` is true. Use a set for dict for O(1) lookup.
- **Partition equal subset sum:** iterate **backwards** over `j` (from target down to num) when updating `dp[j]` so each number is used at most once.

---

## Handy templates

### Climbing stairs / Fibonacci
```python
def climbStairs(n):
    if n <= 1:
        return 1
    prev, curr = 1, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
```

### House robber (take or skip)
```python
def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    prev, curr = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        prev, curr = curr, max(curr, nums[i] + prev)
    return curr
```

### Coin change (min coins)
```python
def coinChange(coins, amount):
    dp = [0] + [float('inf')] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if a >= c:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return dp[amount] if dp[amount] != float('inf') else -1
```

### Word break
```python
def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    dp = [True] + [False] * len(s)
    for i in range(1, len(s) + 1):
        for w in wordSet:
            if i >= len(w) and s[i - len(w):i] == w and dp[i - len(w)]:
                dp[i] = True
                break
    return dp[len(s)]
```

### Partition equal subset sum (subset sum, one pass backwards)
```python
def canPartition(nums):
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    dp = [True] + [False] * target
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] |= dp[j - num]
    return dp[target]
```
