# Intervals Problem Types & Solution Approaches

Interval problems usually involve **overlap**, **merging**, or **covering** a point/range. The two main orderings are **sort by start** (for merging, insert) and **sort by end** (for “max non-overlapping”, greedy keep). **Min-heap of end times** often answers “how many concurrent?” or “shortest interval containing this point”.

---

## 0) Core idea: overlap and ordering

- **Overlap:** two intervals `[a,b]` and `[c,d]` overlap iff `a <= d` and `c <= b` (or equivalently: not (b < c or d < a)).
- **Sort by start:** good for merging (sweep left to right, extend current interval if next overlaps) and for “insert one”.
- **Sort by end:** good for “max set of non-overlapping” (greedy: pick next that starts ≥ last end).
- **Min-heap of end times:** when you need “currently active” intervals (e.g. min meeting rooms = max concurrent).

---

## 1) Can attend all meetings / no overlap check

**Goal:** determine if any two intervals overlap (e.g. can one person attend all meetings).  
**Tell:** “meeting rooms”, “can attend all”, “no overlap”, “conflicting”.

**Approach**
- **Sort by start time.** Then check: for each adjacent pair, `intervals[i].end <= intervals[i+1].start`. If any pair fails, there’s an overlap.

**Examples**
- Meeting Rooms

---

## 2) Merge overlapping intervals

**Goal:** merge all overlapping intervals into disjoint ones.  
**Tell:** “merge intervals”, “merge overlapping”, “union of intervals”.

**Approach**
- **Sort by start.** Maintain a current merged interval. For each next interval:
  - If it **overlaps** current (next.start <= current.end), extend current: `current.end = max(current.end, next.end)`.
  - Else push current to result and set current = next.
- Push the last current.

**Examples**
- Merge Intervals

---

## 3) Minimum meeting rooms (max overlapping at once)

**Goal:** find the minimum number of “resources” (rooms) needed so no interval is left uncovered. = **maximum number of intervals overlapping at any time**.  
**Tell:** “meeting rooms II”, “minimum rooms”, “minimum conference rooms”, “max concurrent”.

**Approach**
- **Option A — Sort starts and ends:** split each interval into `(start, +1)` and `(end, -1)`. Sort by time; if tie, process ends before starts (so we free a room before counting the next). Sweep and count; max count = min rooms.
- **Option B — Min-heap of end times:** sort by start. For each interval: pop all from heap that have end <= current start (those meetings ended). Push current end. **Heap size** = rooms in use; track max heap size.

**Examples**
- Meeting Rooms II

---

## 4) Insert interval (into sorted non-overlapping list)

**Goal:** insert one new interval into a sorted list of non-overlapping intervals, merging if needed.  
**Tell:** “insert interval”, “add interval”, “insert and merge”.

**Approach**
- Intervals are sorted by start. Three phases:
  1. Add all intervals that **end before** new interval starts (no overlap).
  2. **Merge** all intervals that overlap the new one: while current interval start <= new.end, extend new interval to cover it (`new.start = min(..., current.start)`, `new.end = max(..., current.end)`), then skip that interval.
  3. Add the merged interval, then add remaining intervals (start > new.end).

**Examples**
- Insert Interval

---

## 5) Non-overlapping intervals (min remove = max keep)

**Goal:** remove the minimum number of intervals so the rest are non-overlapping. Same as **keep the maximum number of non-overlapping intervals**.  
**Tell:** “non-overlapping intervals”, “erase overlapping”, “min remove”.

**Approach**
- **Sort by end time.** Greedy: keep an interval if its start >= “last kept end”. Track `last_end`. For each interval (in sorted order): if `interval.start >= last_end`, keep it and set `last_end = interval.end`. Else skip (we’re removing it). Count kept; answer is `n - kept` (min remove).

**Examples**
- Non-overlapping Intervals

---

## 6) Minimum interval to include each query (offline + heap)

**Goal:** for each query point `q`, find the **shortest** interval that **contains** `q`.  
**Tell:** “minimum interval to include each query”, “shortest interval containing”, “query point”.

**Approach**
- **Offline:** sort queries by value. Sort intervals by start (or leave as-is and use heap).
- For each query `q`:
  - **Add** all intervals with `start <= q` into a **min-heap keyed by (length, end)** (or by end then length). So the heap holds “candidate intervals that have started by q”.
  - **Remove** intervals with `end < q` (no longer contain q).
  - If heap is empty, answer is -1; else **top** is the shortest interval that contains `q` (smallest length among those with start <= q <= end).
- To avoid re-scanning all intervals per query: sort intervals by start, sort queries, and sweep. For current query, add intervals whose start <= q to the heap, then pop invalid (end < q); top is the answer.

**Examples**
- Minimum Interval to Include Each Query

---

# Quick “Which interval pattern is this?” checklist

- Can one person do all? Any overlap? → **Sort by start, check adjacent ends ≤ next starts**
- Merge overlapping into disjoint → **Sort by start, merge while overlapping**
- Min rooms / max concurrent → **Sort starts and ends (+1/-1) or min-heap of end times**
- Insert one and merge → **Insert interval (three phases: before, merge, after)**
- Min remove so rest non-overlapping → **Sort by end, greedy keep (start ≥ last end)**
- Shortest interval containing each query point → **Offline queries + min-heap by length (with start ≤ q, end ≥ q)**

---

## Common pitfalls (and how to avoid them)

- **Overlap condition:** intervals `[a,b]` and `[c,d]` overlap iff `a <= d` and `c <= b`. Don’t use only `a < d` if intervals are closed; equality still overlaps.
- **Merge: extend by end:** when merging, new end is `max(current.end, next.end)`; start is already the current (leftmost) start.
- **Meeting rooms II:** if you use a heap, pop **all** ended meetings before pushing the new one, so heap size = “currently in use”.
- **Non-overlapping: sort by end.** Sorting by start gives the wrong greedy (you want “earliest ending” first to leave room for more).
- **Minimum interval per query:** heap stores “candidates that have started”; remove those that have ended (`end < q`). Heap key = length (and maybe end for cleanup).

---

## Handy templates

### Merge overlapping intervals (sort by start)
```python
def merge(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    out = [intervals[0]]
    for s, e in intervals[1:]:
        if s <= out[-1][1]:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return out
```

### Non-overlapping intervals (min remove; sort by end)
```python
def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[1])
    kept = 1
    last_end = intervals[0][1]
    for s, e in intervals[1:]:
        if s >= last_end:
            kept += 1
            last_end = e
    return len(intervals) - kept
```

### Meeting Rooms II (min-heap of end times)
```python
import heapq

def minMeetingRooms(intervals):
    intervals.sort(key=lambda x: x[0])
    heap = []  # min-heap of end times
    for start, end in intervals:
        while heap and heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
    return len(heap)
```
