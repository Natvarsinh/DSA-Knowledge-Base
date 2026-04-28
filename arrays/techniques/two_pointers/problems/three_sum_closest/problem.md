# 3Sum Closest

[LeetCode Link](https://leetcode.com/problems/3sum-closest/description/)

## Problem Statement

Given an integer array `nums` of length `n` and an integer `target`, find three integers at distinct indices in `nums` such that the sum is closest to `target`.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

## Example Input/Output

**Example 1:**

Input: nums = [-1, 2, 1, -4], target = 1

Output: 2

Explanation: The sum that is closest to target is `-1 + 2 + 1 = 2`.

**Example 2:**

Input: nums = [0, 0, 0], target = 1

Output: 0

Explanation: The only possible sum is `0 + 0 + 0 = 0`.

## Pattern Used

Two Pointers

## Clues to Identify Pattern

- Need to find a triplet whose sum is closest to a target.
- The problem asks for a value, not the indices or the actual triplet.
- The array can be sorted to make pair search efficient.
- Fix one number and use two pointers to explore the remaining two numbers.

## Approach 1: Brute Force

Use three nested loops to check every possible triplet and track the closest sum.

- **Time Complexity:** O(n³)
- **Space Complexity:** O(1)
- **Implementation:** For every `i`, `j`, `k` with `i < j < k`, compute `nums[i] + nums[j] + nums[k]` and update the closest sum if the absolute difference to `target` is smaller.
- **See implementation:** [brute_force_approach.py](brute_force_approach.py)

## Approach 2: Optimized

Sort the array, then for each element use two pointers to find the best matching pair.

- **Time Complexity:** O(n²)
- **Space Complexity:** O(1) if sorting in-place, otherwise O(n)
- **Implementation:** Sort `nums`. For each index `i`, set `left = i + 1` and `right = n - 1`. Compute the triplet sum. Move `left` right when the sum is less than `target`, move `right` left when the sum is greater than `target`, and update the closest sum along the way.
- **See implementation:** [two_pointers_approach.py](two_pointers_approach.py)

## Key Learning

- Sorting the array enables the two pointers pattern for pair search.
- Fixing one element and searching for the remaining two reduces complexity from O(n³) to O(n²).
- Always compare absolute differences to maintain the closest sum.
- If an exact target match is found, you can return immediately.

## Edge Cases

- Array length exactly 3: return the sum of all elements.
- Negative and positive numbers mixed.
- Large negative or large positive `target` values.
- Duplicate values in the array.
- Exact target match exists.

## Mistakes to Avoid

- Returning the first sum instead of the closest sum.
- Forgetting to sort before using two pointers.
- Using the same element twice.
- Not updating the closest sum when a better candidate is found.
- Failing to handle the case where `target` equals the triplet sum exactly.
