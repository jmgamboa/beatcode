# Linked List Problem Types & Solution Approaches

Linked list problems usually boil down to a small set of recurring patterns.  
If you can recognize the pattern, the implementation becomes mostly mechanical.

---

## 0) Core linked list tools (you’ll use these everywhere)

### Dummy (sentinel) node
Use a dummy head to simplify edge cases (deleting head, building new list, etc.).

**When to use:** removing nodes, merging, partitioning, building a result list.

### Two pointers
- **Slow/Fast**: middle, cycle detection, cycle entry
- **Prev/Curr/Next**: reversal, deletion, rearrangement

### Head mutation safety
If you might change the head, use a dummy node or return the new head explicitly.

---

## 1) Traversal & basic bookkeeping

**Goal:** length, search, accumulate, compare, etc.  
**Tell:** “iterate through list”, “find value”, “count”.

**Template**
- `curr = head`
- while `curr`: process; `curr = curr.next`

**Examples**
- Get length
- Find node by value
- Sum of nodes

---

## 2) Reversal patterns

### 2a) Reverse entire list (iterative)
**Goal:** reverse list direction.  
**Tell:** “reverse linked list”.

**Template**
- `prev = None`, `curr = head`
- While `curr`:
  - `nxt = curr.next`
  - `curr.next = prev`
  - `prev = curr`
  - `curr = nxt`
- return `prev`

**Examples**
- Reverse Linked List

### 2b) Reverse sublist / in k-groups
**Goal:** reverse between positions, reverse nodes in groups.  
**Tell:** “reverse between m and n”, “reverse nodes in k group”.

**Approach**
- Find segment boundaries
- Reverse the segment
- Reconnect: `before -> reversed_head -> tail -> after`

**Examples**
- Reverse Linked List II
- Reverse Nodes in k-Group

---

## 3) Deletion / filtering nodes

**Goal:** remove nodes matching condition/value.  
**Tell:** “remove elements”, “delete node(s) with value X”.

**Best tool:** **dummy node** + `prev/curr`

**Template**
- `dummy.next = head`
- `prev = dummy`, `curr = head`
- If delete `curr`: `prev.next = curr.next` (don’t move `prev`)
- Else: move both

**Examples**
- Remove Linked List Elements
- Delete duplicates (varies by problem)
- Remove Nth node from end (often two pointers)

---

## 4) Fast & slow pointers (cycle / middle / nth from end)

### 4a) Find middle
**Tell:** “middle of linked list”
- slow moves 1, fast moves 2

### 4b) Detect cycle (Floyd)
**Tell:** “has cycle”
- If slow meets fast → cycle exists

### 4c) Find cycle entry
**Tell:** “return node where cycle begins”
- After meeting, move one pointer to head; move both 1 step; they meet at entry

### 4d) Nth from end
**Tell:** “remove/find Nth from end”
- Advance `fast` by `n`, then move both until `fast` hits end

**Examples**
- Linked List Cycle / Cycle II
- Middle of the Linked List
- Remove Nth Node From End

---

## 5) Merge-like problems (sorted lists)

**Goal:** merge two (or k) sorted lists.  
**Tell:** “merge two sorted lists”, “merge k lists”.

**Best tool:** dummy node + tail pointer

**Template**
- Compare heads, append smaller, advance that list
- Append remainder

**Examples**
- Merge Two Sorted Lists
- Merge k Sorted Lists (often with heap)

---

## 6) Duplicate handling (sorted list variants)

There are two common versions:

### 6a) Remove duplicates but keep one copy
**Tell:** “remove duplicates” (keep one)
- If `curr.val == curr.next.val`: skip `curr.next`

**Example**
- Remove Duplicates from Sorted List

### 6b) Remove all nodes that have duplicates
**Tell:** “remove all duplicates entirely”
- Use dummy + lookahead to detect runs and skip whole run

**Example**
- Remove Duplicates from Sorted List II

---

## 7) Partitioning / rearranging nodes (stable)

**Goal:** reorder nodes based on condition while preserving relative order in each group.  
**Tell:** “partition list”, “odd-even”, “reorder by < x”.

**Approach**
- Build two lists (small/large, odd/even) using dummy heads
- Concatenate at the end

**Examples**
- Partition List
- Odd Even Linked List

---

## 8) Palindrome checks

**Goal:** determine if list reads the same forward/backward.  
**Tell:** “palindrome linked list”.

**Approach**
1. Find middle (slow/fast)
2. Reverse second half
3. Compare halves
4. (Optional) restore list

**Example**
- Palindrome Linked List

---

## 9) “Intersection” & “meeting point” tricks

### 9a) Intersection of two linked lists
**Tell:** “intersection node”
**Trick:** pointer switching
- `pA` traverses A then B
- `pB` traverses B then A
- They meet at intersection or at `None`

**Example**
- Intersection of Two Linked Lists

### 9b) Align by length
Alternative: compute lengths and advance the longer list first.

---

## 10) Random pointer / deep copy / complex nodes

**Goal:** clone list with `random` pointers.  
**Tell:** node has extra pointer (random).

**Approaches**
- HashMap old → new
- Interleave nodes (O(1) extra space trick)

**Example**
- Copy List with Random Pointer

---

## 11) Common pitfalls (and how to avoid them)

- **Losing the rest of the list:** always save `next` before rewiring pointers.
- **Head deletions:** use a **dummy node**.
- **Infinite loops:** ensure pointers advance; be careful when skipping nodes.
- **Off-by-one in sublist reversal:** confirm boundary nodes (`before`, `start`, `end`, `after`).
- **Restoring structure:** some problems require list unchanged (restore after reverse).

---

# Quick “Which linked list pattern is this?” checklist

- Reverse something → **Prev/Curr/Next**
- Delete nodes / filter → **Dummy + Prev/Curr**
- Middle / cycle / nth from end → **Slow/Fast or gap pointers**
- Merge sorted lists → **Dummy + Tail**
- Partition / reorder into groups → **Two dummy lists + concat**
- Palindrome → **Middle + reverse half + compare**
- Intersection → **Pointer switching** or **align lengths**
- Random pointers → **HashMap** or **interleaving**

---

## Handy templates

### Dummy node for deletions / building
```python
dummy = ListNode(0)
dummy.next = head
prev, curr = dummy, head

while curr:
    if should_delete(curr):
        prev.next = curr.next
    else:
        prev = curr
    curr = curr.next

return dummy.next
