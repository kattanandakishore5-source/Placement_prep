# Time & Space Complexity Notes

Understanding computational complexity is a core foundational topic for technical placement interviews and backend engineering. This document provides a reference for Big-O notation, asymptotic analysis, and Python's internal operational complexities.

---

## 1. What is Big-O Notation?

Big-O notation describes the **upper bound** (worst-case scenario) of an algorithm's growth rate as the input size $n$ approaches infinity. It characterizes how execution time or memory footprint scales.

### Common Complexity Classes (Fastest to Slowest)
| Notation | Name | Typical Example | Behavior as $n$ grows |
| :--- | :--- | :--- | :--- |
| **$O(1)$** | Constant | Dictionary lookup, array indexing, basic arithmetic | Execution time remains identical regardless of input size |
| **$O(\log n)$** | Logarithmic | Binary search, balanced BST lookup | Problem size cuts in half each step |
| **$O(n)$** | Linear | Single loop, linear search, summing a list | Scaled proportionally with input size |
| **$O(n \log n)$** | Linearithmic | Merge sort, Timsort (`list.sort()` / `sorted()`) | Efficient comparison-based sorting |
| **$O(n^2)$** | Quadratic | Nested loops over input, bubble sort | Time grows quadratically ($10 \times n \implies 100 \times \text{time}$) |
| **$O(2^n)$** | Exponential | Naive recursive Fibonacci, generating subsets | Doubles with each additional element |
| **$O(n!)$** | Factorial | Generating all permutations (Traveling Salesperson) | Infeasible for $n > 12$ |

---

## 2. Complexity Analysis of Day 1: Calculator

The Day 1 Calculator performs fundamental operations on two input values:

```python
number_1 = int(input(...))
operator = input(...)
number_2 = int(input(...))
result = number_1 + number_2
```

### Time Complexity: $O(1)$
- **Input Parsing**: Reading short strings from stdin and converting small numbers runs in constant time $O(1)$.
- **Arithmetic Operations**: Addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`) on standard fixed-size floating-point or 64-bit integers execute in $O(1)$ CPU cycles.
- **Branching (if/elif/else)**: Evaluating conditionals with a constant number of branches (4 checks) takes $O(1)$ time.
- **Overall Time Complexity**: **$O(1)$** (Constant Time).

### Space Complexity: $O(1)$
- Memory is allocated only for a few primitive variables (`number_1`, `number_2`, `operator`, `result`).
- No auxiliary data structures (lists, trees, recursion call stacks) scale with input.
- **Overall Auxiliary Space Complexity**: **$O(1)$** (Constant Space).

> [!NOTE]
> In Python 3, integers have **arbitrary precision** (bignums). If numbers have $d$ digits, addition takes $O(d)$ and multiplication takes $O(d^{\log_2 3}) \approx O(d^{1.58})$ via Karatsuba algorithm. For standard user input numbers ($d \le 64$), this is effectively $O(1)$.

---

## 3. Complexity Reference for Python Built-in Data Structures

### Lists (`list`)
Python lists are dynamic arrays (contiguous memory blocks).
| Operation | Average Case | Worst Case | Notes |
| :--- | :--- | :--- | :--- |
| Indexing `a[i]` | $O(1)$ | $O(1)$ | Direct pointer arithmetic |
| Store `a[i] = v` | $O(1)$ | $O(1)$ | Direct assignment |
| Append `a.append(v)` | $O(1)$ amortized | $O(n)$ | Amortized constant; occasional over-allocation reallocation |
| Pop last `a.pop()` | $O(1)$ | $O(1)$ | Shrinks logical size |
| Pop intermediate `a.pop(i)` | $O(n)$ | $O(n)$ | Requires shifting $n - i$ elements |
| Insert `a.insert(i, v)` | $O(n)$ | $O(n)$ | Requires shifting elements to the right |
| Search `v in a` | $O(n)$ | $O(n)$ | Linear scan |
| Slice `a[i:j]` | $O(k)$ | $O(k)$ | Where $k = j - i$; copies elements |
| Length `len(a)` | $O(1)$ | $O(1)$ | Stored in PyObject header |

### Dictionaries (`dict`)
Python dictionaries use hash tables with open addressing.
| Operation | Average Case | Worst Case | Notes |
| :--- | :--- | :--- | :--- |
| Get `d[key]` | $O(1)$ | $O(n)$ | $O(n)$ on severe hash collision |
| Insert / Set `d[key] = v`| $O(1)$ | $O(n)$ | Amortized $O(1)$ |
| Delete `del d[key]` | $O(1)$ | $O(n)$ | Hash lookup + mark deleted |
| Key check `key in d` | $O(1)$ | $O(n)$ | Computes `hash(key)` and checks bucket |
| Iteration `for k in d` | $O(n)$ | $O(n)$ | Traverses active entries |

### Sets (`set`)
Similar internal implementation to `dict` (keys only, no values).
- Search (`x in s`): $O(1)$ average, $O(n)$ worst.
- Add (`s.add(x)`): $O(1)$ average, $O(n)$ worst.
- Union / Intersection (`s1 | s2`, `s1 & s2`): $O(\text{len}(s_1) + \text{len}(s_2))$.

---

## 4. Key Rules for Interview Complexity Calculations

1. **Drop Constants**: $O(2n + 5) \implies O(n)$, $O(500) \implies O(1)$.
2. **Drop Non-Dominant Terms**: $O(n^2 + 100n + \log n) \implies O(n^2)$.
3. **Sequential Steps Add**: If step 1 takes $O(A)$ and step 2 takes $O(B)$, total is $O(A + B)$.
4. **Nested Loops Multiply**: A loop of $N$ iterations containing an inner loop of $M$ iterations is $O(N \times M)$.
5. **Recursion Complexity**: Use the Master Theorem or draw the recursion tree:
   $$\text{Total Time} = \text{Number of Recursion Calls} \times \text{Work per Call}$$
