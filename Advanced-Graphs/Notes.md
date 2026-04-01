# Advanced Graphs Problem Types & Solution Approaches

Advanced graphs go beyond basic BFS/DFS: **shortest paths with constraints** (Dijkstra, Bellman-Ford, k stops), **minimum spanning trees** (Prim/Kruskal), **Eulerian paths** (Hierholzer), **topological order from pairwise constraints** (alien dictionary), and **“minimize max along path”** (swim in rising water). Know when weights are **non-negative** (Dijkstra), when you need **exactly k edges** (Bellman-Ford style), and when the graph is **implicit** (grid as graph).

---

## 0) Core idea: pick the right algorithm

| Problem shape | Typical approach |
|---------------|------------------|
| Shortest time from source, non-negative edges | **Dijkstra** (heap) |
| Shortest path with **at most k edges** (can be negative?) | **Bellman-Ford** k relaxations or BFS by level |
| Connect all nodes min total edge cost | **MST** (Prim or Kruskal) |
| Use every edge exactly once, lexicographically | **Eulerian trail** + **Hierholzer** |
| Order characters from word list | **Topological sort** on character DAG |
| Minimize **maximum** weight seen on path | **Binary search + BFS**, **union-find by time**, or **modified Dijkstra** |

---

## 1) Network delay time (single-source shortest path)

**Goal:** directed weighted graph, signal from node `k`; return time for signal to reach all nodes, or -1 if some unreachable.  
**Tell:** “network delay time”, “shortest path from k”, “times to all nodes”.

**Approach**
- **Dijkstra:** `dist[v]` = min time from `k` to `v`. Min-heap `(time, node)`. Pop; if time > dist, skip. Relax neighbors: `dist[v] = min(dist[v], time + w)`. Non-negative weights only.
- After algorithm, if any node still ∞, return -1; else max(dist).

**Examples**
- Network Delay Time

---

## 2) Reconstruct itinerary (Eulerian path, lexicographic)

**Goal:** use **every ticket exactly once**; itinerary is sequence of airports; among valid itineraries, return **lexicographically smallest**.  
**Tell:** “reconstruct itinerary”, “use all flights”, “lexicographic”.

**Approach**
- **Hierholzer’s algorithm:** build adjacency list; **sort** each airport’s destinations (so you always take lexicographically smallest next). DFS from `"JFK"`: while current node has outgoing edges, go to next (pop from sorted list), recurse. **Post-order** append to answer (append city when stuck / on return), then **reverse** — gives Eulerian path that uses all edges.
- Why post-order: you defer “dead ends” until you’ve taken longer paths first.

**Examples**
- Reconstruct Itinerary

---

## 3) Min cost to connect all points (MST)

**Goal:** n points in plane; cost between i,j is Manhattan (or Euclidean) distance. Connect all points with minimum total edge cost.  
**Tell:** “min cost to connect all points”, “MST”, “connect all points”.

**Approach**
- **Kruskal:** sort all O(n²) edges by weight; union-find; add edge if it connects two components until n-1 edges.
- **Prim:** start from any node; min-heap of edges to unvisited nodes; grow tree. For dense complete graph, Kruskal with all edges is O(n² log n) sort; Prim can be O(n²) with clever implementation.

**Examples**
- Min Cost to Connect All Points

---

## 4) Swim in rising water (minimize max elevation on path)

**Goal:** grid; start (0,0), end (n-1,n-1); time `t` you can enter cell if `grid[i][j] <= t`. Minimize **t** such that a path exists.  
**Tell:** “swim in rising water”, “minimum time to reach”, “wait for water to rise”.

**Approach**
- **Binary search on answer `t`:** for each `t`, BFS/DFS whether path exists using cells ≤ t. O(n² log(max height)).
- **Dijkstra on “max along path”:** distance to cell = min over paths of **max(grid value on path)**. Relax: `new_dist = max(dist[u], grid[v])`; use min-heap by `new_dist`. Same as “widest path” variant.
- **Union-find:** sort cells by height; add cells in order; when (0,0) and (n-1,n-1) become connected, that height is answer.

**Examples**
- Swim In Rising Water

---

## 5) Alien dictionary (topological sort from words)

**Goal:** given sorted dictionary of alien words, derive a possible character order; or return "" if invalid.  
**Tell:** “alien dictionary”, “character order”, “sorted words”.

**Approach**
- Compare **adjacent words**; first differing pair gives edge `a → b` (a before b). Build **DAG** on characters.
- **Topological sort (Kahn or DFS):** if cycle detected, return "". Else return order of nodes (include chars that never appeared in edges if needed).
- Edge cases: `"abc"` before `"ab"` → invalid (prefix order). Empty graph → any order of unique chars.

**Examples**
- Alien Dictionary

---

## 6) Cheapest flights within k stops (shortest path with edge budget)

**Goal:** directed graph, prices; find cheapest price from `src` to `dst` with **at most k stops** (k stops = k+1 edges max, or problem defines stops as intermediate airports — read carefully: usually **at most k stops** means ≤ k intermediate nodes, so ≤ k+1 edges).  
**Tell:** “cheapest flights within k stops”, “at most k stops”.

**Approach**
- **Bellman-Ford style (k+1 rounds):** `dist[v]` = min cost to reach v with ≤ current number of edges. Each round: for each edge `(u,v,w)`, `dist[v] = min(dist[v], dist[u] + w)`. Run **k+1** iterations (or k+1 “layers” copying previous dist to avoid using same round twice). Use a **copy** of dist each iteration so one path doesn’t use multiple edges in one “stop layer”.
- Alternatively: **BFS by level** for small k, or state `(node, stops)` in Dijkstra (can be heavy).

**Examples**
- Cheapest Flights Within K Stops

---

# Quick “Which advanced graph pattern is this?” checklist

- Shortest time from source, non-negative weights → **Dijkstra**
- Use every flight once, lexicographic route → **Hierholzer + sorted adjacency**
- Connect all points min total distance → **MST (Kruskal/Prim)**
- Minimize max cell height on path from corner to corner → **Binary search + BFS / Dijkstra(max) / UF by height**
- Order of letters from sorted word list → **Topological sort + cycle check**
- Cheapest path with ≤ k stops → **Bellman-Ford k+1 layers (copy dist each round)**

---

## Common pitfalls (and how to avoid them)

- **Dijkstra:** don’t use on graphs with **negative** edge weights (breaks greedy). Network delay uses non-negative times.
- **Reconstruct itinerary:** must use **all** edges; Hierholzer post-order + reverse. Sort destinations **descending** before DFS if you pop from end (or ascending if iterating in order) — goal is lexicographically smallest **first** flight from each airport.
- **MST:** n points → n-1 edges in tree; Kruskal needs union-find; watch integer overflow on distance sums.
- **Swim in rising water:** answer is **max height along path**, not sum; Dijkstra state is min-max, not sum.
- **Alien dictionary:** invalid if longer word is prefix of shorter and appears first; build edges only from first mismatch.
- **K stops:** clarify if k = number of **intermediate** airports (edges = k+1). Bellman-Ford: use **previous round’s** dist when relaxing to avoid counting more than one edge per “stop layer” in one iteration.

---

## Handy templates

### Dijkstra (network delay time)
```python
import heapq

def networkDelayTime(times, n, k):
    graph = [[] for _ in range(n + 1)]
    for u, v, w in times:
        graph[u].append((v, w))
    dist = [float('inf')] * (n + 1)
    dist[k] = 0
    heap = [(0, k)]
    while heap:
        t, u = heapq.heappop(heap)
        if t > dist[u]:
            continue
        for v, w in graph[u]:
            if t + w < dist[v]:
                dist[v] = t + w
                heapq.heappush(heap, (dist[v], v))
    mx = max(dist[1:])
    return mx if mx < float('inf') else -1
```

### Cheapest flights within k stops (Bellman-Ford layers)
```python
def findCheapestPrice(n, flights, src, dst, k):
    dist = [float('inf')] * n
    dist[src] = 0
    for _ in range(k + 1):
        nd = dist[:]
        for u, v, w in flights:
            if dist[u] != float('inf') and dist[u] + w < nd[v]:
                nd[v] = dist[u] + w
        dist = nd
    return dist[dst] if dist[dst] != float('inf') else -1
```

### Kruskal MST (sketch)
```python
def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, i, j):
    ri, rj = find(parent, i), find(parent, j)
    if ri == rj:
        return False
    if rank[ri] < rank[rj]:
        parent[ri] = rj
    else:
        parent[rj] = ri
        if rank[ri] == rank[rj]:
            rank[ri] += 1
    return True
# Sort edges by weight, add if union succeeds until n-1 edges.
```

### Alien dictionary (topo from adjacent words)
```python
from collections import defaultdict, deque

def alienOrder(words):
    graph = defaultdict(set)
    indeg = {c: 0 for w in words for c in w}
    for i in range(len(words) - 1):
        a, b = words[i], words[i + 1]
        if len(a) > len(b) and a.startswith(b):
            return ""
        for x, y in zip(a, b):
            if x != y:
                if y not in graph[x]:
                    graph[x].add(y)
                    indeg[y] += 1
                break
    q = deque([c for c in indeg if indeg[c] == 0])
    order = []
    while q:
        c = q.popleft()
        order.append(c)
        for nxt in graph[c]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return "".join(order) if len(order) == len(indeg) else ""
```
