# Longest Mountain in Array

[LeetCode Link](https://leetcode.com/problems/longest-mountain-in-array/description/)

## Problem Statement

You may recall that an array `arr` is a mountain array if and only if:

- `arr.length >= 3`
- There exists some index `i` (0-indexed) with `0 < i < arr.length - 1` such that:
  - `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`
  - `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

Given an integer array `arr`, return the length of the longest subarray, which is a mountain. Return `0` if there is no mountain subarray.

## Examples

### Example 1:
```
Input: [2, 1, 4, 7, 3, 2, 5]
Output: 5
Explanation: The longest mountain is [1, 4, 7, 3, 2] with length 5.
```

### Example 2:
```
Input: [1, 2, 1]
Output: 3
Explanation: The mountain is [1, 2, 1] with length 3.
```

### Example 3:
```
Input: [1, 2, 3, 4, 5]
Output: 0
Explanation: No mountain subarray exists.
```

## Pattern Used

Two Pointers / Sliding Window (Variable Window)

## Clues to Identify Pattern

- The problem requires finding subarrays with specific structural properties (strictly increasing then strictly decreasing)
- Need to efficiently scan the array to identify potential peaks and expand around them
- Variable window size suggests using two pointers to dynamically adjust the window boundaries
- The need to find the maximum length among valid subarrays indicates a pattern of expanding from potential centers

## Approach 1: Brute Force

Check all possible subarrays of length ≥ 3 and verify if each forms a valid mountain by:
1. Finding if there's a peak where left side increases and right side decreases
2. Tracking the maximum valid mountain length found

**Time Complexity:** O(n³) - nested loops for all subarrays, plus O(n) to check each subarray  
**Space Complexity:** O(1) - only constant extra space used

See [brute_force_approach.py](brute_force_approach.py) for implementation.

## Approach 2: Optimized (Two Pointers)

Use a single pass with two pointers to efficiently find mountains:
1. Iterate through the array looking for peaks (where `arr[i-1] < arr[i] > arr[i+1]`)
2. For each peak found, expand leftward while strictly increasing and rightward while strictly decreasing
3. Track the maximum mountain length found
4. Skip processed elements to avoid redundant checks

**Time Complexity:** O(n) - single pass through the array  
**Space Complexity:** O(1) - only constant extra space used

See [variable_window.py](variable_window.py) for implementation.

## Key Learning

- **Peak Detection:** Efficiently identify potential mountain peaks by checking the condition `arr[i-1] < arr[i] > arr[i+1]`
- **Expansion Strategy:** Once a peak is found, expand left and right independently to find the full mountain boundaries
- **Single Pass Optimization:** By skipping already processed elements after finding a mountain, we achieve O(n) time complexity
- **Strict Inequality:** Remember that mountains require strictly increasing/decreasing sequences, not just non-decreasing

## Edge Cases

- **Array length < 3:** Return 0 (no mountain possible)
- **No peak exists:** Arrays that are strictly increasing, strictly decreasing, or flat
- **Multiple peaks:** Arrays with multiple potential mountains, need to find the longest one
- **Peaks at boundaries:** Mountains that start at index 0 or end at the last index
- **Plateaus:** Cases where elements are equal (violates strict inequality requirement)

## Mistakes to Avoid

- **Not checking strict inequalities:** Using `<=` or `>=` instead of `<` and `>` will incorrectly identify plateaus as mountains
- **Incorrect peak detection:** Missing the condition that peak must have both left and right neighbors
- **Off-by-one errors:** When expanding left/right boundaries, ensure indices stay within array bounds
- **Not handling short arrays:** Arrays with length < 3 should return 0 immediately
- **Double-counting elements:** When skipping after processing a mountain, ensure the pointer jumps correctly to avoid missing subsequent mountains