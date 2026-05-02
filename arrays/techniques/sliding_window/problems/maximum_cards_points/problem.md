# Maximum Points You Can Obtain from Cards

[LeetCode Link](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/)

---

## Problem Statement

There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array `cardPoints`.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly `k` cards.

Your score is the sum of the points of the cards you have taken.

Return the maximum score you can obtain.

---

## Example Input/Output

### Example 1:
```
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: Take cards [1, 6, 5] or [5, 6, 1] from the ends to maximize score.
```

### Example 2:
```
Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Any two cards from the ends give the same score.
```

### Example 3:
```
Input: cardPoints = [9,7,7,9,7,7,9], k = 3
Output: 26
Explanation: Choose the three best cards from the ends.
```

---

## Pattern Used

**Sliding Window (Fixed-Size Window / Complement Window)**

The key idea is to recognize that if you must take `k` cards from the ends, the cards you leave behind form a contiguous subarray of size `n - k`. Finding the minimum sum of that excluded window maximizes the score taken from the ends.

---

## Clues to Identify Pattern

- The choice is always from the **beginning or end** of the array.
- You must take exactly `k` cards, so the remaining cards form a **single contiguous block**.
- The problem asks for a **maximum sum** under a fixed number of picks.
- A brute force solution checks **all combinations of left/right picks** and is too slow for large `n`.
- The optimal result can be found by sliding a window over the **complement** of the taken cards.

---

## Approach 1: Brute Force

**Time Complexity:** O(k * (n - k)) → O(n²) in the worst case

**Space Complexity:** O(1)

**Idea:**
- Try every possible way to take `i` cards from the left and `k - i` cards from the right.
- For each split, compute the sum of the chosen cards and keep track of the maximum.
- This is equivalent to testing every contiguous excluded subarray of size `n - k` with a fresh sum calculation.

**See full implementation:** [brute_force_approach.py](brute_force_approach.py)

---

## Approach 2: Optimized

**Time Complexity:** O(n)

**Space Complexity:** O(1)

**Idea:**
- Compute the total sum of all cards.
- The cards not taken form a contiguous subarray of length `n - k`.
- Find the minimum sum of any window of length `n - k`.
- Maximum score = total sum - minimum excluded window sum.
- Use a fixed-size sliding window to update the excluded window sum in constant time as it moves.

**See full implementation:** [fixed_window.py](fixed_window.py)

---

## Key Learning

- When selecting from the ends, the remaining middle portion is a useful complement to analyze.
- Converting an “ends selection” problem into a “fixed-size excluded window” problem often yields an O(n) solution.
- Sliding window is especially effective when the number of elements to keep or exclude is fixed.
- Always look for a way to avoid recomputing sums from scratch across overlapping subarrays.

---

## Edge Cases

- `k == 0`: return `0` because no cards are taken.
- `k == len(cardPoints)`: return the sum of the entire array.
- `cardPoints` contains all equal values: every valid selection has the same score.
- `cardPoints` has negative or mixed values: the same complement-window idea still works, but verify the algorithm handles negative sums correctly.
- Very small arrays: `n == 1` or `k == 1`.

---

## Mistakes to Avoid

- ❌ Assuming you can only take from one side at a time.
- ❌ Recomputing the sum of the excluded window from scratch for each split.
- ❌ Forgetting the special case when `k == n`.
- ❌ Using a variable-size sliding window instead of the fixed-size `n - k` window.
- ❌ Confusing the problem with taking any `k` cards in the array rather than taking exactly from the ends.

---

## Test Cases

See the implementation and test suite in [test_cases.py](test_cases.py).
