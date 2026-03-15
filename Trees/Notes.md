# Tree Problem Types & Solution Approaches

Trees are about **recursive structure** — every subtree is itself a tree.
Most tree problems reduce to a traversal choice plus a few well-known patterns.
If you can identify which traversal and what information you're threading up/down, the code becomes mostly mechanical.

---

## 0) Core tree tools (you'll use these everywhere)

### DFS (Depth-First Search) — the default
Recursively visit a node, then its children.
Three orderings matter:

| Order | Visit sequence | Typical use |
|---|---|---|
| **Preorder** | root → left → right | copy tree, serialize, path problems |
| **Inorder** | left → root → right | BST problems (gives sorted order) |
| **Postorder** | left → right → root | aggregate from children up, delete tree |

### BFS (Breadth-First Search) — level-by-level
Use a **queue**. Push root, then pop and push children.
**When to use:** anything mentioning "level", "row", "depth by row", or "right side view".

### Return values vs. external state
- **Return value from recursion:** clean, functional — pass info upward.
- **Nonlocal / instance variable:** use when you need info across two subtrees simultaneously (e.g., diameter, max path sum).

---

## 1) Simple DFS — compute a single value per subtree

**Goal:** compute depth, count nodes, check a property, find a value.
**Tell:** "maximum depth", "count", "same tree", "symmetric".

**Template**
```python
def dfs(node):
    if not node:
        return base_case
    left = dfs(node.left)
    right = dfs(node.right)
    return combine(node.val, left, right)
```

**Examples**
- Maximum Depth of Binary Tree
- Count nodes
- Same Tree / Symmetric Tree

---

## 2) Path problems — track a running value from root to leaf

**Goal:** find a root-to-leaf path meeting a condition.
**Tell:** "path sum", "root to leaf", "sum equals target".

**Approach**
- Pass the **remaining target** (or running sum) down as a parameter
- At a leaf, check if condition is satisfied
- Two variants: does path exist? OR collect all paths?

**Collect all paths template**
```python
def dfs(node, path, result):
    if not node:
        return
    path.append(node.val)
    if not node.left and not node.right:
        result.append(list(path))
    dfs(node.left, path, result)
    dfs(node.right, path, result)
    path.pop()  # backtrack
```

**Examples**
- Path Sum
- Path Sum II (all paths)
- Binary Tree Paths

---

## 3) Height / balance — aggregate from leaves upward

**Goal:** compute heights or determine balance.
**Tell:** "balanced binary tree", "height", "is height-balanced".

**Key insight:** postorder — children report their heights first, then you combine.

**Balanced tree template**
```python
def height(node):
    if not node:
        return 0
    left = height(node.left)
    right = height(node.right)
    if left == -1 or right == -1 or abs(left - right) > 1:
        return -1  # sentinel for "unbalanced"
    return 1 + max(left, right)
```

**Examples**
- Balanced Binary Tree
- Maximum Depth of Binary Tree

---

## 4) Diameter / max path — span across two subtrees

**Goal:** longest path between any two nodes (may not pass through root).
**Tell:** "diameter", "longest path", "max path sum".

**Key insight:** the answer lives at the node where the two best branches meet.
Use a nonlocal variable updated at every node.

**Template**
```python
res = [0]  # or self.res = 0

def dfs(node):
    if not node:
        return 0
    left = dfs(node.left)
    right = dfs(node.right)
    res[0] = max(res[0], left + right)  # update global answer
    return 1 + max(left, right)         # return best single branch

dfs(root)
return res[0]
```

**Examples**
- Diameter of Binary Tree
- Binary Tree Maximum Path Sum (same shape, sums instead of counts)

---

## 5) Lowest Common Ancestor (LCA)

**Goal:** find the deepest node that is an ancestor of both p and q.
**Tell:** "lowest common ancestor", "LCA".

### 5a) General binary tree
**Approach:** if current node is p or q, return it. If both subtrees return non-null, current node is the LCA.

```python
def lca(node, p, q):
    if not node or node == p or node == q:
        return node
    left = lca(node.left, p, q)
    right = lca(node.right, p, q)
    if left and right:
        return node
    return left or right
```

### 5b) BST
**Approach:** use BST ordering — no recursion into both subtrees needed.

```python
def lca(node, p, q):
    while node:
        if p.val < node.val and q.val < node.val:
            node = node.left
        elif p.val > node.val and q.val > node.val:
            node = node.right
        else:
            return node
```

**Examples**
- Lowest Common Ancestor of a Binary Tree
- Lowest Common Ancestor of a BST

---

## 6) BST properties — exploit sorted structure

**Goal:** validate, search, insert, find kth element.
**Tell:** "binary search tree", "BST", "valid BST", "kth smallest".

**Key insight:** inorder traversal of a BST yields sorted order.

### Validate BST
Pass min/max bounds down — each node must stay within its allowed range.

```python
def valid(node, lo=float('-inf'), hi=float('inf')):
    if not node:
        return True
    if not (lo < node.val < hi):
        return False
    return valid(node.left, lo, node.val) and valid(node.right, node.val, hi)
```

### Kth Smallest in BST
Inorder traversal (iterative or recursive) — stop at the kth element.

**Examples**
- Validate Binary Search Tree
- Kth Smallest Element in a BST
- Insert into a BST

---

## 7) Level-order traversal (BFS)

**Goal:** process nodes level by level.
**Tell:** "level order", "by level", "right side view", "average of levels", "zigzag".

**Template**
```python
from collections import deque

queue = deque([root])
result = []

while queue:
    level_size = len(queue)
    level = []
    for _ in range(level_size):
        node = queue.popleft()
        level.append(node.val)
        if node.left:  queue.append(node.left)
        if node.right: queue.append(node.right)
    result.append(level)

return result
```

**Right side view:** take `level[-1]` from each level.
**Zigzag:** reverse alternating levels.

**Examples**
- Binary Tree Level Order Traversal
- Binary Tree Right Side View
- Average of Levels in Binary Tree
- Binary Tree Zigzag Level Order Traversal

---

## 8) Tree construction — build from traversal sequences

**Goal:** reconstruct tree from preorder + inorder (or postorder + inorder).
**Tell:** "construct binary tree from preorder and inorder traversal".

**Key insight:** preorder[0] is always the root. Find it in inorder to split left/right subtrees.

```python
def build(preorder, inorder):
    if not inorder:
        return None
    root_val = preorder[0]
    root = TreeNode(root_val)
    mid = inorder.index(root_val)
    root.left = build(preorder[1:mid+1], inorder[:mid])
    root.right = build(preorder[mid+1:], inorder[mid+1:])
    return root
```

**Optimization:** use a hashmap for O(1) inorder index lookups.

**Examples**
- Construct Binary Tree from Preorder and Inorder Traversal
- Construct Binary Tree from Postorder and Inorder Traversal

---

## 9) Subtree problems

**Goal:** check if one tree is a subtree of another; count matching subtrees.
**Tell:** "subtree of another tree", "same structure".

**Approach**
- At each node in the main tree, check if the subtree rooted there matches `subRoot`
- Use a helper `isSameTree(s, t)`

```python
def isSubtree(root, subRoot):
    if not root:
        return False
    if isSameTree(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)
```

**Examples**
- Subtree of Another Tree
- Count Univalue Subtrees

---

## 10) Good nodes / count nodes with condition

**Goal:** count nodes satisfying a condition relative to path from root.
**Tell:** "count good nodes", "nodes greater than all ancestors".

**Approach:** pass the max value seen so far on the path down from root.

```python
def dfs(node, max_so_far):
    if not node:
        return 0
    good = 1 if node.val >= max_so_far else 0
    new_max = max(max_so_far, node.val)
    return good + dfs(node.left, new_max) + dfs(node.right, new_max)
```

**Examples**
- Count Good Nodes in Binary Tree

---

## 11) Serialize / deserialize

**Goal:** convert tree to/from a string representation.
**Tell:** "serialize", "deserialize", "encode", "decode tree".

**Approach:** preorder DFS with null markers. On deserialize, use a queue/iterator of tokens.

```python
def serialize(root):
    res = []
    def dfs(node):
        if not node:
            res.append('N')
            return
        res.append(str(node.val))
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return ','.join(res)

def deserialize(data):
    tokens = iter(data.split(','))
    def dfs():
        val = next(tokens)
        if val == 'N':
            return None
        node = TreeNode(int(val))
        node.left = dfs()
        node.right = dfs()
        return node
    return dfs()
```

**Examples**
- Serialize and Deserialize Binary Tree

---

# Quick "Which tree pattern is this?" checklist

- Compute depth / count / same tree → **Simple DFS, return value upward**
- Path from root to leaf (sum, collect) → **DFS passing running value down**
- Diameter / max path / span → **Postorder + nonlocal global max**
- Balanced check → **Height with -1 sentinel**
- LCA → **General: return p/q, both non-null = LCA | BST: use ordering**
- BST validity / kth → **Inorder is sorted; pass bounds for validation**
- Level-by-level / right side / zigzag → **BFS with queue, snapshot level size**
- Reconstruct from sequences → **Preorder root splits inorder**
- Subtree match → **isSameTree at every node**
- Node condition relative to ancestors → **DFS passing running max/min down**
- Serialize / deserialize → **Preorder with null markers**

---

## Common pitfalls (and how to avoid them)

- **Forgetting the null base case:** always handle `if not node: return ...` first.
- **Wrong inorder index in construction:** use a hashmap, not `.index()`, for O(1) lookup.
- **Diameter vs max path sum confusion:** diameter counts edges (or nodes), path sum uses `node.val` which can be negative — never take negative branches.
- **BST validation with just left < root < right:** wrong. Must pass bounds through the whole subtree (e.g., left subtree must have all values `< root`, not just direct child).
- **Using global mutable state carelessly:** use `self.res` or `res = [val]` to safely share state across recursive calls.
- **BFS level boundary:** snapshot `len(queue)` at the start of each level, before pushing children.

---

## Handy templates

### Generic DFS returning a value
```python
def dfs(node):
    if not node:
        return base_case
    left = dfs(node.left)
    right = dfs(node.right)
    return combine(node.val, left, right)
```

### Generic BFS level order
```python
from collections import deque
queue = deque([root])
while queue:
    for _ in range(len(queue)):
        node = queue.popleft()
        # process node
        if node.left:  queue.append(node.left)
        if node.right: queue.append(node.right)
```

### Iterative inorder (BST)
```python
stack, curr = [], root
while stack or curr:
    while curr:
        stack.append(curr)
        curr = curr.left
    curr = stack.pop()
    # process curr
    curr = curr.right
```

### Invert / mirror a tree
```python
def invert(node):
    if not node:
        return None
    node.left, node.right = invert(node.right), invert(node.left)
    return node
```
