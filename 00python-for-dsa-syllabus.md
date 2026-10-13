# Python for DSA: Detailed Syllabus

**Goal:** Learn the Python and CSE fundamentals needed before starting Data Structures and Algorithms (DSA).

**Learning path:**
`FOR LOOPS → WHILE LOOPS → STRINGS → FUNCTIONS → LISTS/ARRAYS → DICTIONARIES → SETS → RECURSION → BIG-O → PROBLEM SOLVING → DSA`

**Legend:** `[x]` = taught in lessons, `[ ]` = still to learn.
Exercises answered and checked by the tutor are tracked separately in the Progress Tracker at the end.

---

## 1. For Loops

- [x] What is a `for` loop and why we use it
- [x] Basic syntax (`for variable in collection:`), colon and indentation
- [x] How a loop executes step by step (iteration tables)
- [x] `range(stop)`
- [x] `range(start, stop)`
- [x] `range(start, stop, step)`, including negative steps
- [x] Rule: start is included, stop is never included
- [x] Looping through numbers
- [x] Looping through strings
- [x] Looping through lists
- [x] Accumulator pattern (`total = 0` before the loop)
- [x] Nested `for` loops (`i`, `j`)
- [x] Nested loop patterns (stars, number triangles)
- [x] `range(i)` and `range(1, i + 1)` inside a nested loop
- [x] Reading Python Tutor (line numbers, Frames, step counter)
- [ ] `for` loop with `if`
- [ ] `for` loop with `break`
- [ ] `for` loop with `continue`
- [ ] Common mistakes (full list)
- [ ] How to trace a `for` loop manually (full practice)
- [ ] How many times a loop executes (counting practice)
- [ ] Basic time complexity of loops

---

## 2. While Loops

- [x] What is a `while` loop
- [x] Syntax
- [x] Initialization
- [x] Condition checking
- [x] Updating the variable
- [x] Infinite loops (and Ctrl + C to stop)
- [x] Tracing `while` loops with a table
- [x] `for` vs `while`: when to use each
- [x] Rewriting a `for` loop as a `while` loop and back
- [ ] `break` in `while`
- [ ] `continue` in `while`
- [ ] Nested `while` loops
- [ ] More `while` practice problems

---

## 3. Strings

### Part 1: Indexing and traversal
- [x] What is a string
- [x] Indexing (starts at 0)
- [x] Negative indexing (starts at -1)
- [x] `len()`
- [x] `IndexError` (index out of range)
- [x] Traversing by character (`for ch in s`)
- [x] Traversing by index (`for i in range(len(s))`)
- [x] Strings cannot be changed in place

### Part 2: Slicing, `in`, methods
- [x] Slicing `s[start:stop]`
- [x] Slice shortcuts (`s[:4]`, `s[2:]`, `s[-3:]`, `s[1:-1]`)
- [x] Slicing with a step (`s[::2]`, `s[::-1]`)
- [x] `in` and `not in`
- [x] Important methods: `upper`, `lower`, `strip`, `replace`, `count`, `find`, `split`, `join`, `startswith`, `endswith`, `isdigit`, `isalpha`
- [x] Methods return a new string (the original does not change)
- [x] Counting vowels using a loop and `in`
- [x] Splitting an email using `find` and slicing

### Part 3: Problem solving
- [x] Concatenation (`+`) and repetition (`*`)
- [x] String comparison (`==`, `<`, `>`, case sensitivity)
- [x] Reversing a string (slicing and loop)
- [x] Palindrome checking (reverse method and two-ends method)
- [x] Character counting with a loop
- [ ] More common string problems

---

## 4. Functions

### Basics
- [x] Why functions are needed (avoid repetition, reuse)
- [x] Defining a function (`def`)
- [x] Calling a function
- [x] Parameters vs arguments
- [x] `return`
- [x] `print` vs `return`
- [x] Code after `return` does not run
- [x] Function without `return` gives `None`

### Parameters
- [x] Multiple parameters (order matters)

### Variables and scope
- [x] Local variables
- [x] Global variables (reading them inside a function)
- [ ] Local vs global variables with the same name
- [ ] Modifying a global variable (the `global` keyword) and why it is usually avoided

### Functions with other topics
- [x] Functions with loops
- [x] Functions with strings
- [x] Functions with lists
- [x] Breaking a problem into functions
- [x] Functions calling other functions (basic)

### Extra topics useful for DSA
- [ ] Returning multiple values (`return a, b`)
- [ ] Default parameters
- [ ] Keyword arguments
- [ ] Passing a list to a function and changing it

---

## 5. Lists / Arrays

- [ ] What is an array?
- [ ] How Python lists are used like arrays
- [ ] Creating lists
- [ ] Indexing and negative indexing
- [ ] Slicing
- [ ] Traversing (by value and by index)
- [ ] Updating elements
- [ ] Searching
- [ ] Inserting
- [ ] Deleting
- [ ] Finding maximum and minimum
- [ ] Sum and counting
- [ ] Reversing
- [ ] Finding duplicates
- [ ] Removing duplicates
- [ ] Nested lists and 2D lists
- [ ] List methods
- [ ] Common mistakes
- [ ] Basic array problem-solving patterns

---

## 6. Dictionaries and Sets

### Dictionaries
- [ ] Key-value pairs
- [ ] Creating dictionaries
- [ ] Accessing values
- [ ] Updating values
- [ ] Adding and removing
- [ ] Traversing
- [ ] `keys()`, `values()`, `items()`
- [ ] Frequency counting
- [ ] Solving problems with dictionaries

### Sets
- [ ] What is a set and why it is useful
- [ ] Membership checking
- [ ] Removing duplicates
- [ ] Basic set operations
- [ ] Using sets in DSA problems

---

## 7. Recursion

- [ ] What is recursion and why it is useful
- [ ] A function calling itself
- [ ] Base case and recursive case
- [ ] How recursion works internally
- [ ] Call stack
- [ ] Step-by-step tracing
- [ ] Common recursion mistakes
- [ ] Recursion vs loops
- [ ] Countdown
- [ ] Printing numbers
- [ ] Sum of numbers
- [ ] Factorial
- [ ] Power
- [ ] Fibonacci
- [ ] Reverse a string
- [ ] Palindrome

---

## 8. Important Python Concepts Before DSA

- [ ] Mutable vs immutable
- [ ] References
- [ ] Scope
- [ ] Call stack
- [ ] Memory basics
- [ ] Basic debugging
- [ ] Reading Python errors
- [ ] Nested loops (revision)
- [ ] Basic problem-solving techniques
- [ ] Iteration vs recursion

---

## 9. Time and Space Complexity

- [ ] What is time complexity
- [ ] What is space complexity
- [ ] Why complexity matters
- [ ] Big-O notation
- [ ] O(1)
- [ ] O(log n)
- [ ] O(n)
- [ ] O(n log n)
- [ ] O(n²)
- [ ] Explaining complexity using simple loops

---

## 10. Problem-Solving Practice

Problems mixing: `for` loops, `while` loops, strings, functions, lists, dictionaries, sets, recursion, nested loops.

- [ ] Easy problems
- [ ] Medium problems
- [ ] Harder problems

**Rules:** the learner solves first. If wrong, the tutor explains the mistake and gives a hint before showing the solution.

---

## Final DSA Readiness Test

- [ ] Python coding and problem-solving test
- [ ] Pass the test

Only after passing: **"You are ready to start DSA."**

---

## Progress Tracker (exercises answered)

| Day | Topic | Exercises answered | Notes |
|---|---|---|---|
| 1 | For loops (Part 1) | Yes | `range()` counting was a weak spot |
| 1 (repeat) | `range()` counting | Partly | Practice Round 2 not answered |
| 2 | While loops (Part 1) | No | |
| 3 | `for` vs `while` | No | |
| 4 | Strings (Part 1) | No | |
| 5 | Strings (Part 2) | No | |
| 6 | Strings (Part 3) | No | |
| 7 | Functions (Part 1) | No | |
| 8 | Functions (Part 2) | No | |
