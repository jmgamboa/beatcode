# Heaps and Queues Problem Types & Solution Approaches

Heaps (priority queues) give **O(log n)** insert and **O(1)** or **O(log n)** access to the min or max. They’re used for “always need the current best” (kth largest, merge k lists, scheduling) and for **simulation** (repeatedly take the max/min and update).  
Queues (and deques) show up in **BFS**, **level-order** traversal, and **monotonic queue** patterns.

---

## 0) Core idea: when to use a heap

- **Min-heap:** you repeatedly need the **smallest** element (e.g. k smallest, merge k sorted lists, Dijkstra).
- **Max-heap:** you repeatedly need the **largest** (e.g. k largest, Last Stone Weight, top‑k by frequency).
- **Size‑k heap:** keep the heap at exactly **k** elements so the top is the kth largest/smallest without scanning.

Language note: Python’s `heapq` is a **min-heap**. For a max-heap, negate values or use `(priority, item)` with negative priority.

---

## 1) Kth largest / Kth smallest (stream or array)

**Goal:** maintain or compute the kth largest (or kth smallest) element as data is added or from a static array.  
**Tell:** “kth largest in a stream”, “kth largest element”, “add and return kth largest”.

**Approach**
- **Min-heap of size k:** store the k largest elements. The **top is the kth largest**.
  - When adding: if heap size < k, push; else if new value > top, pop then push.
- For kth **smallest**, use a **max-heap of size k** (e.g. store negatives in a min-heap) so the top is the kth smallest.

**Examples**
- Kth Largest Element in a Stream
- Kth Largest Element in an Array (build heap from array, or quickselect)

---

## 2) Simulate by repeatedly taking max (or min)

**Goal:** repeatedly take the two largest (or two smallest), combine them, push the result back, until one or zero remain.  
**Tell:** “last stone weight”, “smash stones”, “combine two largest”.

**Approach**
- **Max-heap** of all elements (use negatives in a min-heap).
- While size ≥ 2: pop two, compute new value (e.g. difference), if non-zero push back.
- Return the last remaining element or 0.

**Examples**
- Last Stone Weight

---

## 3) K closest / K nearest points

**Goal:** from n points, find the k closest to a target (origin, point, etc.).  
**Tell:** “k closest points”, “k nearest”, “closest to origin”.

**Approach**
- **Option A:** min-heap of all points by distance; pop k times → O(n log n), O(n) space.
- **Option B:** max-heap of size k; if heap has k elements and current point is closer than top, pop then push. Top of max-heap = kth closest; at the end, all k elements in the heap are the k closest. No need to sort.

**Examples**
- K Closest Points to Origin

---

## 4) Task scheduler / greedy with cooldown

**Goal:** schedule tasks with a cooldown between same-type tasks; minimize total time or count idle slots.  
**Tell:** “task scheduler”, “cooldown”, “same task every n apart”.

**Approach**
- Count frequency per task. Use a **max-heap of (count, task)** (or negate counts for min-heap).
- Simulate time: each step, pick the most frequent **available** task (not on cooldown), decrement count, put on cooldown. If nothing available, idle.
- Alternatively: compute **idle slots** from the max frequency and fill with other tasks; formula-based (number of chunks × (n+1) + remainder, etc.).

**Examples**
- Task Scheduler

---

## 5) Design Twitter (merge k sorted lists / recent items)

**Goal:** support post tweet and get news feed = merge of recent tweets from followees, ordered by time.  
**Tell:** “design Twitter”, “news feed”, “recent posts from followed users”.

**Approach**
- Per user: store their recent tweets (e.g. list or deque, capped at some size).
- **getNewsFeed:** collect the most recent tweet from each followee, then **merge k sorted lists** using a **min-heap of (timestamp, user_id, index)**. Pop the latest (largest timestamp), push the next tweet from that user if any. Repeat until you have k tweets or no more.
- Follow/unfollow: maintain adjacency structure (set or list of followees).

**Examples**
- Design Twitter

---

## 6) Find median from data stream (two heaps)

**Goal:** add numbers and return the median at any time.  
**Tell:** “find median from data stream”, “running median”, “median in O(log n)”.

**Approach**
- **Left half:** **max-heap** (so you can get the max of the lower half = median when sizes are equal or left is one larger).
- **Right half:** **min-heap** (get the min of the upper half).
- **Invariant:** size(left) == size(right) or size(left) == size(right) + 1.
- **addNum:** add to one heap, then rebalance (move one element to the other so invariant holds).
- **getMedian:** if left size > right, return left’s top; else return average of both tops.

**Examples**
- Find Median from Data Stream

---

## 7) Queues: BFS and level-order

**Goal:** process nodes level by level (tree/graph).  
**Tell:** “level order”, “BFS”, “layer by layer”.

**Approach**
- **Queue** (e.g. `collections.deque`). Push root, then while queue: pop, process, push children. For level boundaries, snapshot `len(queue)` at the start of each level.

**Examples**
- Binary Tree Level Order Traversal
- BFS in graphs

---

## 8) Monotonic queue (deque for sliding min/max)

**Goal:** for each window, get min or max in O(1) amortized.  
**Tell:** “sliding window maximum/minimum”, “min in range”.

**Approach**
- **Deque** storing indices (or values) in **monotonic** order. For max: keep decreasing order; when current element is larger, pop from the back until order is restored. Front of deque = current window max. Remove front when it leaves the window.

**Examples**
- Sliding Window Maximum
- Often combined with DP or prefix sums

---

# Quick “Which heap/queue pattern is this?” checklist

- Kth largest/smallest in stream or array → **Min-heap (or max-heap) of size k**
- Repeatedly take two largest, combine, push back → **Max-heap simulation**
- K closest/nearest points → **Heap by distance (min-heap pop k, or max-heap size k)**
- Schedule tasks with cooldown → **Task scheduler (max-heap of frequencies + cooldown)**
- Merge recent feeds / k sorted lists by time → **Merge k sorted with heap (Design Twitter)**
- Running median → **Two heaps (left max, right min)**
- Level-by-level traversal → **BFS queue**
- Sliding window min/max → **Monotonic deque**

---

## Common pitfalls (and how to avoid them)

- **Max-heap in Python:** `heapq` is min-heap only; store `(-priority, item)` or negate values so “largest” becomes “smallest” after negation.
- **Kth largest with min-heap of size k:** the **top** of the min-heap is the kth largest (the smallest among the k largest). Don’t pop k times to get it.
- **Two heaps median:** keep the size invariant (left size ≥ right size, differ by at most 1) after every add; rebalance by moving one element from the larger heap to the smaller.
- **Task scheduler:** “available” means not on cooldown; track cooldown per task (e.g. time when it becomes available again) and only push back into the heap when that time has passed.
- **Design Twitter:** feed is “merge k sorted lists” by timestamp; use heap of (timestamp, user_id, index_in_that_user_list).

---

## Handy templates

### Kth largest in stream (min-heap of size k)
```python
import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = []
        for x in nums:
            self.add(x)

    def add(self, val):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]
```

### Last Stone Weight (max-heap via negation)
```python
import heapq

def lastStoneWeight(stones):
    heap = [-s for s in stones]
    heapq.heapify(heap)
    while len(heap) > 1:
        a, b = -heapq.heappop(heap), -heapq.heappop(heap)
        if a != b:
            heapq.heappush(heap, -(a - b))
    return -heap[0] if heap else 0
```

### Find median from data stream (two heaps)
```python
import heapq

class MedianFinder:
    def __init__(self):
        self.lo = []   # max-heap of left half (negate for min-heap)
        self.hi = []   # min-heap of right half

    def addNum(self, num):
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self):
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2
```
