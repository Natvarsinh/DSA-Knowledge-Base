# Longest Continuous Increasing Subsequence

[LeetCode Link](https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/)

## Problem Statement

Given an unsorted array of integers `nums`, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices `l` and `r` (`l < r`) such that it is:

`[nums[l], nums[l + 1], ..., nums[r - 1], nums[r]]`

and for each `l <= i < r`, `nums[i] < nums[i + 1]`.

## Example Input/Output

**Example 1:**

Input: `nums = [1, 3, 5, 4, 7]`

Output: `3`

Explanation: The longest continuous increasing subsequence is `[1, 3, 5]`.

**Example 2:**

Input: `nums = [2, 2, 2, 2, 2]`

Output: `1`

Explanation: Every element is equal, so the longest strictly increasing subarray has length `1`.

**Example 3:**

Input: `nums = [1, 3, 5, 7, 8, 9]`

Output: `6`

Explanation: The entire array is strictly increasing.

## Pattern Used

Sliding Window (Fixed / Growing Window)

## Clues to Identify Pattern

- The problem asks for a contiguous subarray, not a subsequence with gaps.
- You need the longest run of strictly increasing values.
- The window expands while the sequence stays increasing and resets when it breaks.
- The goal is to track a maximum length while scanning the array once.

## Approach 1 (Brute Force)

Check every starting index and extend the contiguous subarray while it remains strictly increasing.

1. Iterate over each index `i` as the start of a potential subarray.
2. From `i`, extend forward while `nums[j] > nums[j - 1]`.
3. Track the longest run found.

**Time Complexity:** O(n²) in the worst case, because each start index may scan forward.

**Space Complexity:** O(1)

See [brute_force_approach.py](brute_force_approach.py) for implementation.

## Approach 2 (Optimized)

Use a single pass through the array and maintain two counters:
- `current_length` for the current increasing run
- `max_length` for the longest run seen so far

1. Start with `current_length = 1`.
2. For each element from index `1` to `n - 1`:
   - If `nums[i] > nums[i - 1]`, increment `current_length`.
   - Otherwise, reset `current_length` to `1`.
3. Update `max_length` after each step.

**Time Complexity:** O(n)

**Space Complexity:** O(1)

See [variable_window.py](variable_window.py) for implementation.

## Key Learning

- For contiguous subarray problems, identify whether a sliding window with dynamic boundaries can track the required property.
- Strictly increasing means equal values break the sequence.
- Resetting the current window when the condition fails is often enough for maximum-length subarray problems.
- One-pass scanning with local state is the most efficient solution for this problem.

## Edge Cases

- Empty array: return `0`.
- Single element array: return `1`.
- All equal elements: return `1`.
- Entire array strictly increasing: return `n`.
- Sequence breaks frequently: make sure to reset the current run correctly.

## Mistakes to Avoid

- Treating non-decreasing subsequences as valid; the requirement is strictly increasing.
- Forgetting to handle the empty array case.
- Using a subarray pattern when the problem explicitly requires contiguous elements.
- Not updating `max_length` after the final run.
- Resetting the count incorrectly when the increasing condition fails.
