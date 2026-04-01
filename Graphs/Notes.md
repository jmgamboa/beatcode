# Graphs Problem Types & Solution Approaches

Graph problems usually involve **traversal** (DFS/BFS), **connectivity** (components, cycles, trees), or **ordering** (topological sort). The graph can be **explicit** (adjacency list/matrix) or **implicit** (grid neighbors, words one edit apart). Key patterns: **grid DFS/BFS**, **multi-source BFS**, **topological sort**, **union-find**, and **shortest path in unweighted graph** (BFS).

---

## 0) Core idea: representation and traversal

- **Explicit graph:** `adj[u]` = list of neighbors. For grids: 4 or 8 directions from `(r, c)`.
- **DFS:** stack (recursive or explicit); good for “visit each component”, “explore one path”, “detect cycle” with a visited set and (optionally) path/recursion stack.
- **BFS:** queue; good for **shortest path** in unweighted graphs and for **level-by-level** (e.g. “distance from sources”, “rotting oranges” time steps).
- **Multi-source BFS:** push **all** initial sources into the queue at distance 0; same BFS gives shortest distance from any source.

---

## 1) Grid: count components (number of islands)

**Goal:** in a 2D grid, count connected components of a certain cell value (e.g. `'1'` = land).  
**Tell:** “number of islands”, “count connected components in grid”.

**Approach**
- For each unvisited land cell, run **DFS or BFS** to mark all connected land; increment count. Use visited set or mutate grid (e.g. mark as `'0'` after visit).
- Neighbors: 4 directions `(r+1,c)`, `(r-1,c)`, `(r,c+1)`, `(r,c-1)` (and bounds check).

**Examples**
- Number of Islands

---

## 2) Grid: max area / size of component

**Goal:** find the **maximum** size of a connected component (e.g. max area of island).  
**Tell:** “max area of island”, “largest region”, “biggest connected component”.

**Approach**
- Same as count components, but for each DFS/BFS return the **size** (number of cells visited). Take max over all components.

**Examples**
- Max Area of Island

---

## 3) Clone graph (copy with new nodes)

**Goal:** deep copy a graph (each node has neighbors); every node and edge must be new.  
**Tell:** “clone graph”, “copy graph”, “deep copy”.

**Approach**
- **DFS or BFS** from given node. Use a map `old_node -> new_node`. When visiting a node, create its copy and map it; for each neighbor, if not yet copied, recurse/queue it, then add the copy of the neighbor to the current node’s copy’s neighbors.

**Examples**
- Clone Graph

---

## 4) Multi-source BFS (distance from any source)

**Goal:** fill distances from any of several sources (e.g. gates, rotten oranges). All sources start at distance 0.  
**Tell:** “walls and gates”, “fill rooms with distance to nearest gate”, “multi-source”.

**Approach**
- Push **all** source cells into the queue with distance 0. Run normal BFS: pop `(r, c, d)`, for each empty neighbor, set `dist[neighbor] = d+1` and push. Skip walls and already filled cells.

**Examples**
- Walls and Gates
- Rotting Oranges (same idea: all rotten oranges at time 0; BFS by “minute”; check if any fresh left)

---

## 5) Rotting oranges (multi-source BFS with time)

**Goal:** each minute, rotten oranges rot adjacent fresh ones; return minutes until no fresh, or -1 if some remain.  
**Tell:** “rotting oranges”, “spread from multiple sources”.

**Approach**
- Multi-source BFS: enqueue all rotten cells at “time” 0. Each level = one minute. For each cell popped, rot neighbors (push with time+1). Track fresh count; if it doesn’t reach 0, return -1. Else return max time (or last level).

**Examples**
- Rotting Oranges

---

## 6) Reach from two boundaries (Pacific / Atlantic)

**Goal:** which cells can reach **both** the Pacific border (top/left) and the Atlantic border (bottom/right) by moving to same or lower height?  
**Tell:** “pacific atlantic water flow”, “rain water flow”, “reach both oceans”.

**Approach**
- **Two DFS/BFS from borders:** (1) From all Pacific border cells, DFS/BFS “can flow to” (next cell has same or higher height). Mark all reachable. (2) From all Atlantic border cells, same. **Answer:** cells reachable from **both**.
- Reverse thinking: “which cells can the water flow **from** to the ocean?” = start from ocean and go **uphill** (neighbor height >= current).

**Examples**
- Pacific Atlantic Water Flow

---

## 7) Surrounded regions (flip inner O’s)

**Goal:** any `'O'` that is not on the border and not connected to the border should be flipped to `'X'`.  
**Tell:** “surrounded regions”, “capture”, “flip enclosed”.

**Approach**
- **DFS/BFS from all border `'O'`:** mark every `'O'` reachable from the border (e.g. temporary `'T'` or a visited set). Then: every `'O'` left is surrounded → flip to `'X'`; restore `'T'` to `'O'`.

**Examples**
- Surrounded Regions

---

## 8) Course schedule (can finish? cycle detection)

**Goal:** can you take all courses given prerequisites (directed edges)? = is the directed graph **acyclic**?  
**Tell:** “course schedule”, “prerequisites”, “can finish”.

**Approach**
- **Topological sort / cycle detection:** DFS with three states (unvisited, in stack, done). If you enter a node that is “in stack”, you have a cycle → return false. Or: run Kahn’s algorithm (BFS with in-degrees); if the number of nodes we process equals n, no cycle.
- Build graph: `prerequisites[i] = [a, b]` means b → a (a depends on b). So edge from prerequisite to course.

**Examples**
- Course Schedule

---

## 9) Course schedule II (topological order)

**Goal:** return a valid order to take all courses (if possible); else empty.  
**Tell:** “course schedule II”, “find order”, “topological order”.

**Approach**
- **Kahn’s algorithm:** compute in-degrees; queue all with in-degree 0; while queue not empty, pop, add to result, reduce in-degree of neighbors, push if 0. If result length != n, cycle → return [].  
- Or DFS: post-order traversal (push node when leaving) gives reverse topological order; reverse it. Check for cycle during DFS.

**Examples**
- Course Schedule II

---

## 10) Graph valid tree (connected and acyclic)

**Goal:** given n nodes and a list of undirected edges, is the graph a valid tree? (Tree = connected + acyclic = exactly one component and no cycle.)  
**Tell:** “graph valid tree”, “valid tree”, “n nodes n-1 edges”.

**Approach**
- **Necessary:** for a tree we need exactly **n-1 edges** (otherwise multiple components or cycle). If `len(edges) != n-1`, return false.
- **Sufficient:** with n-1 edges, “tree” ⟺ connected. Run **DFS/BFS** from 0 and count visited; if count != n, not connected. Or use **union-find**: add edges one by one; if both endpoints already in same component, cycle → return false; at the end check one component.

**Examples**
- Graph Valid Tree

---

## 11) Number of connected components (undirected)

**Goal:** count how many connected components in an undirected graph.  
**Tell:** “number of connected components”, “count components”.

**Approach**
- **DFS/BFS:** for each unvisited node, run a traversal, increment count.  
- **Union-find:** start with n components; for each edge, union the two endpoints; number of distinct roots = number of components.

**Examples**
- Number of Connected Components in an Undirected Graph

---

## 12) Redundant connection (first edge that creates cycle)

**Goal:** given a tree (as edge list) with one extra edge, return an edge that can be removed to make it a tree. Often “return the last such edge in the input”.  
**Tell:** “redundant connection”, “extra edge”, “remove to make tree”.

**Approach**
- **Union-find:** process edges in order. For each edge (u, v), if u and v are already in the same component, this edge creates a cycle → it’s redundant. Return the first (or last, per problem) such edge.

**Examples**
- Redundant Connection

---

## 13) Word ladder (shortest path in implicit graph)

**Goal:** transform word A to word B by changing one letter at a time; each intermediate must be in a word list. Find **minimum** number of steps.  
**Tell:** “word ladder”, “shortest transformation”, “one letter change”.

**Approach**
- **BFS:** state = current word; neighbors = all words that differ by exactly one letter (iterate positions and letters, or precompute “one-letter diff” groups). Start from beginWord, BFS until endWord; return level. Unweighted → BFS gives shortest path.
- **Optimization:** use a set for the word list and remove a word when visited (so we don’t revisit).

**Examples**
- Word Ladder

---

# Quick “Which graph pattern is this?” checklist

- Count islands / components in grid → **Grid DFS/BFS, count components**
- Max area of one component in grid → **Grid DFS/BFS, return max size**
- Deep copy graph → **Clone graph (DFS/BFS + node map)**
- Distance from nearest gate/source → **Multi-source BFS**
- Rotting spread from multiple sources → **Multi-source BFS by time/level**
- Cells that can reach both oceans → **Two DFS/BFS from borders, intersect**
- Flip enclosed O’s, keep border-connected → **DFS/BFS from border O’s**
- Can finish all courses? → **Cycle detection / topological sort**
- Return valid course order → **Topological sort (Kahn or DFS)**
- Is graph a tree? (n nodes, edges) → **Tree ⟺ n-1 edges + connected (or union-find)**
- Count connected components → **DFS/BFS count or union-find**
- Remove one edge to get tree → **Union-find, first edge that creates cycle**
- Shortest path word A → word B (one letter change) → **BFS on implicit graph**

---

## Common pitfalls (and how to avoid them)

- **Grid bounds:** always check `0 <= r < rows` and `0 <= c < cols` before accessing.
- **Clone graph:** map **every** node to its copy before traversing; when adding neighbors to the copy, use the copy of the neighbor (from the map), not the original.
- **Pacific/Atlantic:** “water flows from high to low” → from ocean we go **uphill** (neighbor height >= current). Don’t reverse the condition.
- **Surrounded regions:** only border `'O'` and their connected component escape; mark them first, then flip the rest.
- **Topological sort direction:** prerequisites [a, b] usually mean “a depends on b”, so edge b → a. Build `adj[b].append(a)` and in-degree for a.
- **Word ladder:** treat as **unweighted** graph; BFS gives shortest path. Don’t use DFS for shortest path.

---

## Handy templates

### Grid DFS (count islands / explore component)
```python
def numIslands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            dfs(r + dr, c + dc)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1
    return count
```

### Multi-source BFS (distance from gates)
```python
from collections import deque

def wallsAndGates(rooms):
    if not rooms:
        return
    q = deque()
    R, C = len(rooms), len(rooms[0])
    for r in range(R):
        for c in range(C):
            if rooms[r][c] == 0:
                q.append((r, c))
    while q:
        r, c = q.popleft()
        d = rooms[r][c]
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and rooms[nr][nc] == 2**31 - 1:
                rooms[nr][nc] = d + 1
                q.append((nr, nc))
```

### Union-find (redundant connection / components)
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # already connected → cycle
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True
```

### Kahn's topological sort (course schedule II)
```python
from collections import deque

def findOrder(numCourses, prerequisites):
    adj = [[] for _ in range(numCourses)]
    indeg = [0] * numCourses
    for a, b in prerequisites:
        adj[b].append(a)
        indeg[a] += 1
    q = deque(i for i in range(numCourses) if indeg[i] == 0)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == numCourses else []
```
