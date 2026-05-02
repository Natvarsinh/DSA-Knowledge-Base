# Maximum Product Subarray

[LeetCode Link](https://leetcode.com/problems/maximum-product-subarray/description/)

## Problem Statement

Given an integer array `nums`, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.

## Examples

- **Input:** `nums = [2, 3, -2, 4]`  
  **Output:** `6`  
  **Explanation:** The subarray `[2, 3]` has the largest product `6`.

- **Input:** `nums = [-2, 3, -4]`  
  **Output:** `24`  
  **Explanation:** The subarray `[-2, 3, -4]` has the largest product `24` (two negatives make positive).

- **Input:** `nums = [0, 2]`  
  **Output:** `2`  
  **Explanation:** The subarray `[2]` has the largest product `2`.

## Pattern Used

Dynamic Programming / Sliding Window Variant

This problem involves finding the maximum product subarray, which requires handling negative numbers that can flip the sign of the product. It's similar to Kadane's algorithm but adapted for products instead of sums.

## Clues to Identify Pattern

- The problem asks for the maximum product of a contiguous subarray.
- Negative numbers can turn a potential minimum product into a maximum when multiplied by another negative.
- Zeros can reset the product, making subarrays on either side independent.
- The solution needs to track both the maximum and minimum products ending at each position.

## Approach 1: Brute Force

[View Implementation](brute_force_approach.py)

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)

This approach checks all possible subarrays by using nested loops. For each starting index `i`, it computes the product for all subarrays starting from `i` to `j`, updating the maximum product found.

## Approach 2: Optimized (Dynamic Programming)

[View Implementation](sliding_window.py)

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

This approach uses dynamic programming to keep track of the maximum and minimum products ending at each position. When encountering a negative number, it swaps the min and max to handle sign flips. Zeros reset the products.

## Key Learning

- Always consider the impact of negative numbers on products; they can turn minima into maxima.
- Zeros act as separators, resetting the product calculation.
- Tracking both min and max products is crucial for handling sign changes efficiently.
- The optimal solution runs in linear time, making it suitable for large arrays.

## Edge Cases

- **Single element:** Return the element itself.
- **All negative numbers:** The largest product will be the largest single negative number or the product of even number of negatives.
- **Contains zeros:** Zeros can split the array; consider subarrays on both sides.
- **All zeros:** Return 0.
- **Large numbers:** Ensure the product fits in 32-bit integer (handled by problem constraints).

## Mistakes to Avoid

- Forgetting to handle zeros properly; they should reset the current product.
- Not swapping min and max when encountering negatives, leading to incorrect results.
- Assuming the maximum product is always positive; it could be negative if all elements are negative.
- Using integer overflow-prone calculations without considering the 32-bit constraint (though test cases ensure it's fine).