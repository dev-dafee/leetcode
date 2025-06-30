## Problem

Given a string `s`, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

## Intuition

- A string whose length is **prime** can only be represented as a repetition of a **single character**, since it has no proper divisors (excluding 1 and itself).
- If the string contains more than one unique character and its length is prime, it's impossible to divide it into equal repeating parts.
- For strings of **non-prime length**, we can check their proper divisors and test if repeating a substring of that length reconstructs the original string.

---

## Approach

1. Check if the string has length 1 → return `False`.
2. If all characters are identical → return `True`.
3. If the string length is prime → return `False` (no valid repeated substrings).
4. Otherwise:
   - Compute all **proper divisors** of the string length (excluding 1 and n).
   - For each divisor `d`:
     - Extract the substring `s[:d]`.
     - Repeat it `(len(s) // d)` times.
     - If it matches the original string, return `True`.
5. If no repeating pattern is found, return `False`.

---

## Complexity

- **Time complexity:**
  $$
  O(n \cdot \sqrt{n})$$  
  - Finding divisors takes **O(√n)**.
  - For each divisor, we may construct and compare a string of length **n**.
  $$
- **Space complexity:**
  $$
  O(\sqrt{n} + n)$$  
  - **O(√n)** for storing divisors in a set.
  - **O(n)** for temporary substrings during pattern checking.
  $$
