# Stack Problem Types & Solution Approaches

Stacks are about **LIFO** behavior and are often used to manage **nested structure**, **undo-like behavior**, or maintain a **monotonic** sequence of candidates.  
Most stack problems fall into a handful of recognizable patterns.

---

## 1) Balanced parentheses / delimiter matching

**Goal:** validate or process nested/paired symbols.  
**Tell:** parentheses/brackets/braces, “valid”, “balanced”, “well-formed”, nesting.

**Approach**
- Push opening symbols
- On closing symbol: check stack top matches
- Stack must end empty

**Examples**
- Valid Parentheses
- Remove outermost parentheses
- Minimum add to make parentheses valid

---

## 2) Expression parsing & evaluation (operator stack)

**Goal:** evaluate arithmetic expressions with precedence/parentheses.  
**Tell:** “evaluate expression”, `+ - * /`, parentheses, RPN, calculators.

**Common approaches**
- **RPN (Reverse Polish Notation):** single value stack
- **Infix evaluation:** operator stack + value stack
- **Shunting-yard:** convert infix → postfix then evaluate

**Examples**
- Evaluate Reverse Polish Notation
- Basic Calculator / Basic Calculator II
- Decode String (stack-based parsing)

---

## 3) Next Greater / Next Smaller element (monotonic stack)

**Goal:** for each element, find next greater/smaller element to the right/left.  
**Tell:** “next greater”, “next smaller”, “previous greater”, “span”, “warmer day”.

**Approach**
- Maintain a **monotonic stack** of indices
- While current element breaks monotonicity, pop and resolve answers

**Variants**
- Next greater to the right (strictly decreasing stack)
- Next smaller to the right (strictly increasing stack)
- Previous greater/smaller (scan left to right using stack)

**Examples**
- Next Greater Element I/II
- Daily Temperatures
- Online Stock Span

---

## 4) Monotonic stack for ranges / contributions (count subarrays)

**Goal:** count how many subarrays where each element is min/max, sum of mins/maxes, etc.  
**Tell:** “sum of subarray minimums/maximums”, “contribution”, “count ranges”.

**Approach**
- For each index `i`, find:
  - distance to previous smaller (or greater)
  - distance to next smaller (or greater)
- Contribution:
  - as minimum: `a[i] * left_span * right_span`
- Carefully handle duplicates with consistent strictness (`<` vs `<=`)

**Examples**
- Sum of Subarray Minimums
- Sum of Subarray Ranges
- Largest Rectangle in Histogram (related)

---

## 5) Histogram / rectangle / area problems

**Goal:** compute largest rectangle area using bar heights.  
**Tell:** “histogram”, “largest rectangle”, “max area”, bars.

**Approach**
- Monotonic increasing stack of indices
- When current height is smaller, pop heights and compute areas
- Use sentinel (0 height) at end to flush stack

**Examples**
- Largest Rectangle in Histogram
- Maximal Rectangle (2D reduction to histogram per row)

---

## 6) Min stack / max stack / stack with extra info

**Goal:** support `push/pop/top` plus `getMin/getMax` in O(1).  
**Tell:** “design a stack”, “min stack”, “max stack”.

**Approaches**
- Store `(value, current_min)` pairs
- Or maintain a separate min stack

**Examples**
- Min Stack

---

## 7) Simulation with a stack (“undo”, collisions, canonical form)

**Goal:** simulate processes where the latest item can cancel/merge with previous items.  
**Tell:** “collide”, “cancel”, “remove adjacent”, “simplify path”, “backspace”.

**Approach**
- Iterate items
- Push normally
- While top conflicts with incoming, pop/resolve

**Examples**
- Asteroid Collision
- Remove All Adjacent Duplicates in String
- Backspace String Compare
- Simplify Path

---

## 8) Stack as recursion replacement (DFS / iterative traversal)

**Goal:** convert recursion to iterative for trees/graphs or generate sequences.  
**Tell:** “iterative traversal”, “avoid recursion”, DFS.

**Approach**
- Push starting node/state
- Pop, process, push neighbors/states
- Often store extra state like `(node, visited)` for postorder

**Examples**
- Binary tree inorder/preorder/postorder (iterative)
- Flood fill / graph DFS

---

## 9) Stack for monotonic queue building blocks (related concept)

Not a stack-only problem, but stacks often appear in:
- building monotonic structures
- “remove k digits” (greedy + stack)

**Examples**
- Remove K Digits
- Make string smallest after removals

---

# Quick “Which stack pattern is this?” checklist

- Matching parentheses / nesting → **Delimiter stack**
- Evaluate expressions / decode → **Parsing stacks**
- Next greater/smaller / spans → **Monotonic stack**
- Sum of subarray mins/maxes → **Contribution via monotonic bounds**
- Largest rectangle / maximal rectangle → **Histogram monotonic stack**
- Design min/max stack → **Aux info per node or extra stack**
- Collisions / cancellations / simplification → **Simulation stack**
- Iterative DFS / traversal → **Explicit stack replaces recursion**

---

## Common pitfalls (and how to avoid them)

- **Using values instead of indices:** many monotonic problems need indices for distances.
- **Duplicate handling:** decide strictness (`<` vs `<=`) consistently to avoid double-counting.
- **Forgetting to flush the stack:** use a sentinel element at end.
- **O(n²) pop loops:** monotonic stacks are amortized O(n) if each element is pushed/popped once.
- **Mismatched delimiter mapping:** keep a clear map of closing → opening.

---

## Handy templates

### Balanced parentheses
```python
stack = []
pairs = {')': '(', ']': '[', '}': '{'}

for ch in s:
    if ch in "([{":
        stack.append(ch)
    else:
        if not stack or stack[-1] != pairs[ch]:
            return False
        stack.pop()

return not stack
