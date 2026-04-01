# 2D Dynamic Programming Problem Types & Solution Approaches

2D DP means the state is **two indices** (or two dimensions): often **two strings** (LCS, edit distance, interleaving), **grid position** (unique paths, longest path in matrix), **interval** `[i, j]` (burst balloons), or **(index, state)** (stock with cooldown). Recurrence relates `dp[i][j]` to neighbors or smaller subproblems.

---

## 0) Core idea: two dimensions of state

- **Grid:** `dp[i][j]` = answer for cell `(i, j)` from top-left rules.
- **Two strings:** `dp[i][j]` = answer for `s1[:i]` vs `s2[:j]` (or first i chars, first j chars).
- **Interval:** `dp[i][j]` = optimal value for subarray/subproblem on indices `i..j`.
- **State machine on index:** `dp[i][state]` where state = holding / not holding / cooldown.

---

## 1) Unique paths (grid from top-left to bottom-right)

**Goal:** robot moves only right or down; count paths from `(0,0)` to `(m-1, n-1)`.  
**Tell:** “unique paths”, “grid”, “right and down only”.

**Approach**
- `dp[i][j]` = number of paths to `(i, j)`. `dp[i][j] = dp[i-1][j] + dp[i][j-1]`. Base: first row and first column are 1. Can optimize to 1D row.

**Examples**
- Unique Paths

---

## 2) Longest common subsequence (two strings)

**Goal:** longest subsequence common to both strings (order preserved, not necessarily contiguous).  
**Tell:** “longest common subsequence”, “LCS”, “two strings”.

**Approach**
- `dp[i][j]` = LCS length of `text1[:i]` and `text2[:j]`. If `text1[i-1] == text2[j-1]`: `dp[i][j] = 1 + dp[i-1][j-1]`. Else: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

**Examples**
- Longest Common Subsequence

---

## 3) Best time to buy and sell stock with cooldown (state on day)

**Goal:** max profit; after selling you must **cool down** one day before buying again.  
**Tell:** “stock with cooldown”, “sell then wait”.

**Approach**
- **State machine:** three states per day: `hold` (own stock), `sold` (just sold, in cooldown), `rest` (no stock, can buy). Or `dp[i][0]` = max profit on day i if **holding**, `dp[i][1]` if **not holding** and **can buy**, `dp[i][2]` if **not holding** in **cooldown** (sold yesterday). Transitions: buy from rest → hold; sell from hold → cooldown; cooldown → rest next day.
- Recurrence example: `hold[i] = max(hold[i-1], rest[i-1] - price[i])`, `sold[i] = hold[i-1] + price[i]`, `rest[i] = max(rest[i-1], sold[i-1])`.

**Examples**
- Best Time to Buy and Sell Stock With Cooldown

---

## 4) Coin change II (number of combinations)

**Goal:** count **combinations** of coins that sum to `amount` (order doesn’t matter; unlimited coins).  
**Tell:** “coin change II”, “number of combinations”, “order doesn’t matter”.

**Approach**
- **2D:** `dp[i][a]` = ways using first `i` coin types to make sum `a`. Or **1D:** `dp[a]` += `dp[a - coin]` iterating coins outer, amount inner (so each combination counted once).
- Key: outer loop over coins, inner over amount → avoids counting permutations.

**Examples**
- Coin Change II

---

## 5) Target sum (assign + or - to reach target)

**Goal:** assign `+` or `-` to each number so the expression equals `target`. Count ways.  
**Tell:** “target sum”, “plus minus”, “ways to reach target”.

**Approach**
- Let `P` = sum of numbers with `+`, `S` = total sum. Then `2P - S = target` → `P = (S + target) / 2`. Count subsets with sum `P` (0/1 knapsack count). If `(S + target)` odd or `target` out of range, return 0.
- **2D DP:** `dp[i][j]` = ways first `i` numbers sum to `j` with subset choice. Or 1D backwards.

**Examples**
- Target Sum

---

## 6) Interleaving string (two strings form a third)

**Goal:** is `s3` an interleaving of `s1` and `s2` (preserve order within each)?  
**Tell:** “interleaving string”, “merge two strings”.

**Approach**
- `dp[i][j]` = can `s1[:i]` and `s2[:j]` interleave to form `s3[:i+j]`. If `s1[i-1] == s3[i+j-1]`, `dp[i][j] |= dp[i-1][j]`. If `s2[j-1] == s3[i+j-1]`, `dp[i][j] |= dp[i][j-1]`. Base: `dp[0][0] = true`.

**Examples**
- Interleaving String

---

## 7) Longest increasing path in a matrix (DFS + memo)

**Goal:** longest strictly increasing path moving to 4 neighbors (no reuse).  
**Tell:** “longest increasing path in a matrix”, “matrix DFS”.

**Approach**
- **Memoization:** `memo[r][c]` = LIP starting at `(r, c)`. DFS to neighbors with strictly larger value; `memo[r][c] = 1 + max(dfs(nr, nc))`. Each cell computed once → O(mn). Not classic “fill table” order; still 2D state.

**Examples**
- Longest Increasing Path in a Matrix

---

## 8) Distinct subsequences (count ways t is subsequence of s)

**Goal:** number of distinct subsequences of `s` that equal `t`.  
**Tell:** “distinct subsequences”, “count subsequences equal to t”.

**Approach**
- `dp[i][j]` = number of ways to form `t[:j]` as a subsequence of `s[:i]`. If `s[i-1] == t[j-1]`: `dp[i][j] = dp[i-1][j-1] + dp[i-1][j]` (use or skip this char). Else: `dp[i][j] = dp[i-1][j]`. Base: `dp[i][0] = 1` (empty t).

**Examples**
- Distinct Subsequences

---

## 9) Edit distance (Levenshtein)

**Goal:** min operations (insert, delete, replace) to turn `word1` into `word2`.  
**Tell:** “edit distance”, “minimum operations”.

**Approach**
- `dp[i][j]` = edit distance between `word1[:i]` and `word2[:j]`. If chars match: `dp[i][j] = dp[i-1][j-1]`. Else: `1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])` (delete, insert, replace).

**Examples**
- Edit Distance

---

## 10) Burst balloons (interval DP)

**Goal:** burst balloons `i..j` (exclusive of virtual boundaries); when you burst `k` you get `nums[left] * nums[k] * nums[right]` coins. Maximize total.  
**Tell:** “burst balloons”, “interval DP”, “last balloon to burst”.

**Approach**
- **Think last:** `dp[i][j]` = max coins from **open interval** `(i, j)` (balloons strictly between i and j, with `nums[i]` and `nums[j]` as fixed boundaries). For last balloon `k` in `(i, j)`: `dp[i][j] = max over k of dp[i][k] + nums[i]*nums[k]*nums[j] + dp[k][j]`. Pad array with 1 at ends. Length increasing.

**Examples**
- Burst Balloons

---

## 11) Regular expression matching (`.` and `*`)

**Goal:** does pattern `p` match string `s`? `.` matches one char; `*` matches zero or more of preceding element.  
**Tell:** “regular expression matching”, “wildcard”, “dot star”.

**Approach**
- `dp[i][j]` = does `s[:i]` match `p[:j]`. Cases: if `p[j-1]` is letter or `.`: match if `dp[i-1][j-1]` and char match. If `p[j-1] == '*'`: zero of prev char → `dp[i][j-2]`; or one or more → `dp[i-1][j]` if `p[j-2]` matches `s[i-1]`. Careful indexing.

**Examples**
- Regular Expression Matching

---

# Quick “Which 2D DP pattern is this?” checklist

- Paths in grid (right/down) → **Unique paths (prefix sums on grid)**
- Two strings, longest common subsequence → **LCS**
- Stock with cooldown → **State machine (hold / sold / rest) or dp[i][state]**
- Count ways to make amount with coins (unordered) → **Coin change II (2D or 1D outer coins)**
- Assign +/- to reach target → **Target sum → subset sum to (S+target)/2**
- s3 interleave of s1 and s2 → **Interleaving string dp[i][j]**
- Longest increasing path in matrix → **DFS + memo on (r,c)**
- Count subsequences of s equal to t → **Distinct subsequences**
- Min edits between two strings → **Edit distance**
- Optimal on interval [i,j] with “last choice” → **Burst balloons (interval DP)**
- Pattern with `.` and `*` → **Regex matching 2D DP**

---

## Common pitfalls (and how to avoid them)

- **Coin change II:** coin change I is **min coins**; II is **count combinations**. Use outer loop on coins so you don’t count permutations.
- **Target sum:** reduce to subset sum; check `(sum(nums) + target) % 2 == 0` and bounds on subset sum.
- **Interleaving:** index `i+j` in `s3` must align; base case `dp[0][0] = true`.
- **Burst balloons:** define `dp[i][j]` on **open** interval (balloons between i and j), not closed; pad `nums` with 1.
- **Regex matching:** `*` means “repeat previous element”; handle `a*` matching empty vs multiple `a`s.
- **LIS in matrix:** use **strict** inequality for neighbors; memo avoids exponential revisits.

---

## Handy templates

### Unique paths
```python
def uniquePaths(m, n):
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[-1]
```

### Longest common subsequence
```python
def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
```

### Edit distance
```python
def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]
```

### Interleaving string
```python
def isInterleave(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False
    m, n = len(s1), len(s2)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for i in range(m + 1):
        for j in range(n + 1):
            if i > 0 and s1[i - 1] == s3[i + j - 1]:
                dp[i][j] |= dp[i - 1][j]
            if j > 0 and s2[j - 1] == s3[i + j - 1]:
                dp[i][j] |= dp[i][j - 1]
    return dp[m][n]
```

### Stock with cooldown (state machine)
```python
def maxProfit(prices):
    hold, sold, rest = float('-inf'), 0, 0
    for p in prices:
        hold, sold, rest = max(hold, rest - p), hold + p, max(rest, sold)
    return max(sold, rest)
```
