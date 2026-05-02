# Minimum Size Subarray Sum

[LeetCode Link](https://leetcode.com/problems/minimum-size-subarray-sum/description/)

---

## Problem Statement

Given an array of **positive integers** `nums` and a **positive integer** `target`, return the **minimal length** of a contiguous subarray whose sum is **greater than or equal to** `target`. If there is no such subarray, return `0` instead.

**Constraint:** All numbers in the array are positive integers.

---

## Example Input/Output

### Example 1:
```
Input: nums = [2, 3, 1, 2, 4, 3], target = 7
Output: 2
Explanation: The subarray [4, 3] has the minimal length under the problem constraint.
```

### Example 2:
```
Input: nums = [1, 2, 3], target = 10
Output: 0
Explanation: No subarray of nums is greater than or equal to the target.
```

### Example 3:
```
Input: nums = [1, 4, 7, 2], target = 7
Output: 1
Explanation: The subarray [7] has the minimal length. A single element can satisfy the condition.
```

---

## Pattern Used

**Sliding Window** (Two Pointers Technique)

This problem is a classic example of the **variable-size sliding window** pattern. The key insight is that since all numbers are positive, we can use a greedy approach with two pointers to find the optimal subarray in linear time.

---

## Clues to Identify This Pattern

1. ✓ Looking for a **contiguous subarray** with a specific property (sum >= target)
2. ✓ Need to find the **minimal/maximal length** of that subarray
3. ✓ All elements are **positive** (this is critical! allows us to shrink the window)
4. ✓ **Brute force is O(n²)** but we need better → Think of optimization
5. ✓ Can use **two pointers** to avoid re-checking overlapping subarrays
6. ✓ Problem has an **optimal substructure** property

---

## Approach 1: Brute Force

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)

**Algorithm:**
- Iterate through each position `i` as the starting point
- For each start position, iterate through subsequent positions `j`
- Keep a running sum from `i` to `j`
- When sum >= target, record the window length and break
- Return the minimum length found

**See full implementation:** [brute_force_approach.py](brute_force_approach.py)

**Why it's inefficient:**
- We recalculate sums for overlapping subarrays
- We don't leverage the property that all numbers are positive
- For each starting position, we check every possible ending position

---

## Approach 2: Optimized (Sliding Window)

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

**Algorithm:**
1. Use **two pointers**: `left` (start of window) and `right` (end of window)
2. Expand the window by moving `right` and adding `nums[right]` to the current sum
3. When `current_sum >= target`:
   - Record the window length
   - **Shrink from the left**: remove `nums[left]` from sum and move `left` forward
   - Continue shrinking until sum < target (to find the minimal window)
4. Return the minimum length found

**Key Insight:**
- Since all numbers are positive, if a window `[left, right]` has sum >= target, any larger window `[left, right+k]` will also satisfy the condition
- Therefore, we can always shrink from the left to find smaller valid windows
- This prevents redundant calculations

**See full implementation:** [variable_window.py](variable_window.py)

---

## Key Learning

### Why Sliding Window Works Here:

1. **Monotonic Property:** If sum >= target at position right, then sum < target for some left is guaranteed (after shrinking)
2. **No Backtracking:** Once we move left pointer, we never need to go back, ensuring O(n) complexity
3. **Positive Numbers:** Guarantee that sum is non-decreasing as we extend right and non-increasing as we shrink left
4. **Early Termination:** If we find a window of size 1, we can return immediately (optimal solution)

### When to Use This Pattern:

- **Subarray/substring** problems
- Looking for **minimal/maximal length** with a condition
- Elements are **homogeneous** (all positive, all negative, etc.)
- Need to optimize from O(n²) to O(n)

---

## Edge Cases

| Case | Input | Expected Output | Explanation |
|------|-------|-----------------|-------------|
| No Solution | `nums = [1, 2, 3]`, `target = 10` | `0` | Sum of entire array is less than target |
| Single Element | `nums = [1, 4, 7, 2]`, `target = 7` | `1` | Single element satisfies condition |
| Entire Array | `nums = [1, 1, 1]`, `target = 3` | `3` | Need all elements to reach target |
| Large Element | `nums = [10, 2, 3]`, `target = 5` | `1` | First element alone exceeds target |
| Empty Array | `nums = []`, `target = 7` | `0` | No elements to form subarray |
| Minimum Length | `nums = [1, 2, 3, 4, 5]`, `target = 11` | `3` | Window [3, 4, 5] has sum = 12 |

---

## Mistakes to Avoid

### ❌ Mistake 1: Using the wrong pointer movement strategy
```
❌ WRONG: Moving only the right pointer, never shrinking left
        This becomes O(n²) as you recalculate sums

✓ CORRECT: Shrink the window from left when sum >= target
          This ensures each element is visited at most twice
```

### ❌ Mistake 2: Not handling the case where no subarray exists
```
❌ WRONG: Returning min_length directly without checking if it was updated
         Will return a large number or wrong value

✓ CORRECT: Return 0 if min_length is still infinity/unchanged
```

### ❌ Mistake 3: Forgetting to update the sum when moving pointers
```
❌ WRONG: Move pointers but don't update current_sum
         Leads to incorrect comparisons

✓ CORRECT: Add nums[right] when expanding
           Subtract nums[left] when shrinking
```

### ❌ Mistake 4: Using >= vs > incorrectly
```
❌ WRONG: Using > instead of >= 
         Problem asks for sum "greater than or equal to" target

✓ CORRECT: Use >= in the condition
```

### ❌ Mistake 5: Not considering the "all positive" constraint
```
❌ WRONG: Assuming this technique works with negative numbers
         It doesn't! Greedy shrinking fails with negative numbers

✓ CORRECT: Recognize this is specific to all-positive arrays
           Different approaches needed for mixed signs
```

---

## Test Cases

See comprehensive test cases: [test_cases.py](test_cases.py)

The test suite includes:
- Standard cases with multiple valid subarrays
- Edge cases with no solution
- Single element matches
- Entire array requirements
- Early termination scenarios

---

## Related Patterns

- **Longest Substring Without Repeating Characters:** Similar sliding window, different condition
- **Maximum Window Sum:** Uses same two-pointer approach
- **Substring with K Distinct Characters:** Variable-size sliding window variant
- **Median of Two Sorted Arrays:** Different sliding window application

---

## Summary

| Aspect | Brute Force | Optimized |
|--------|-------------|-----------|
| **Time** | O(n²) | O(n) |
| **Space** | O(1) | O(1) |
| **Approach** | Nested loops | Two pointers |
| **Scalability** | Poor | Excellent |
| **Readability** | Simple | Moderate |

For any array size > 1000, the optimized sliding window approach is **significantly faster**. Always prefer the O(n) solution for interviews and production code.
