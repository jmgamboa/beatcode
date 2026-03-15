# 🚀 DSA Patterns Curriculum 

👋  
With popular sets like NeetCode 150 or Blind 75, there can be a big gap from Easy to Medium. And even the concepts within Mediums feel sparse and not bridged together. That’s why I put together a **progressive** curriculum: a sequence of problems that gradually introduce atomic concepts and patterns you’ll need to tackle more complex ones.  

This is heavily inspired by Neetcode's program

---

## 🎯 Goal
Learn LeetCode by mastering **core patterns** (not memorizing solutions), through:
- ✅ Structured **progression** (Easy → Easier Medium → Medium -> Hard)
- ✅ Repetition with variation (pattern recognition)
---

## 🧱 Prerequisites
You should be comfortable with:
- your programming language of choice
- loops, conditionals, built-in functions
- different O notations

---

## 🧩 Curriculum (Recommended Order)
- 🗂️ Arrays and Hashmaps
- 🧺 Hashing & Frequency Maps  
- 🔁 Two Pointers  
- 🧱 Stack (Monotonic + classic)  
- 🔍 Binary Search
- 🪟 Sliding Window  
- 🌳 Trees (DFS/BFS basics)  
- 🔌 Heaps
- 🧵 Backtracking (recursive/subsets/permutations)
- 📊 Graphs
- 🧠 Dynamic Programming

---

## 🏁 North Star
**Consistency beats intensity.**  
60 minutes/day adds up. 📈🔥

---

## 📜 Scripts

Scripts live in `scripts/`. Requires Python 3.

### Build LeetCode CSV
Regenerates `scripts/leetcode_problems.csv` from the curriculum markdown files (url, difficulty, pattern). Run after adding or changing problems in any curriculum.

```bash
python3 scripts/build_leetcode_csv.py
```

### Random problem
Prints a random problem URL from the CSV. Optionally filter by difficulty.

```bash
# Any difficulty
python3 scripts/random_problem.py

# By difficulty (easy, medium, hard)
python3 scripts/random_problem.py --difficulty easy
python3 scripts/random_problem.py -d medium
```