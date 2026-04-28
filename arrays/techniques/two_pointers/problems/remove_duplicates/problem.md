# Remove Duplicates from Sorted Array

[LeetCode Link](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)

## Problem Statement

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates **in-place** such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in `nums` to be `k`. After removing duplicates, return the number of unique elements `k`.

The first `k` elements of `nums` should contain the unique numbers in sorted order. The remaining elements beyond index `k - 1` can be ignored.

## Example Input/Output

### Example 1:
**Input:** `nums = [1,1,2]`  
**Output:** `2, nums = [1,2,_]`  
**Explanation:** Your function should return `k = 2`, with the first two elements of `nums` being `1` and `2` respectively. It does not matter what you leave beyond the returned `k` (hence they are underscores).

### Example 2:
**Input:** `nums = [0,0,1,1,1,2,2,3,3,4]`  
**Output:** `5, nums = [0,1,2,3,4,_,_,_,_,_]`  
**Explanation:** Your function should return `k = 5`, with the first five elements of `nums` being `0`, `1`, `2`, `3`, and `4` respectively. It does not matter what you leave beyond the returned `k` (hence they are underscores).

## Pattern Used

Two Pointers Technique

## Clues to Identify Pattern

- The array is sorted in non-decreasing order
- Need to remove duplicates in-place
- Must maintain the relative order of elements
- Required to return the count of unique elements

## Approach 1: Brute Force

See [brute_force_approach.py](brute_force_approach.py) for implementation.

This approach uses a set to track unique elements and then overwrites the array with unique values.

## Approach 2: Optimized (Two Pointers)

See [two_pointers_approach.py](two_pointers_approach.py) for implementation.

This approach uses two pointers: one to iterate through the array and another to track the position where the next unique element should be placed.

## Key Learning

- In-place array modifications can significantly reduce space complexity
- Two pointers technique is highly effective for problems involving sorted arrays
- Understanding the problem constraints (sorted, in-place) helps in choosing the right algorithm

## Edge Cases

- Empty array: `nums = []` → return `0`
- All elements are the same: `nums = [1,1,1,1]` → return `1`, `nums = [1,_,_,_]`
- No duplicates: `nums = [1,2,3,4]` → return `4`, `nums = [1,2,3,4]`
- Single element: `nums = [5]` → return `1`, `nums = [5]`

## Mistakes to Avoid

- Modifying the array beyond the `k` elements (the problem allows ignoring elements after `k-1`)
- Not handling the in-place requirement correctly (avoid creating new arrays)
- Forgetting to return the count `k` instead of the modified array
- Using extra space when an O(1) space solution is possible