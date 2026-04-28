# Squares of a Sorted Array

[LeetCode Link](https://leetcode.com/problems/squares-of-a-sorted-array/description/)

## Problem Statement

Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Your solution should avoid the trivial approach of squaring every number and then sorting the result. Try to find an O(n) solution by using the fact that the input array is already sorted.

## Example Input/Output

**Example 1:**

Input: nums = [-4,-1,0,3,10]

Output: [0,1,9,16,100]

**Example 2:**

Input: nums = [-7,-3,2,3,11]

Output: [4,9,9,49,121]

## Pattern Used

- Two Pointers Technique
- Sorted array processing

## Clues to Identify Pattern

- The input array is sorted in non-decreasing order.
- Squaring negative numbers can produce large positive values.
- The largest squares come from the most extreme values at the array ends.
- A linear scan with two pointers can build the sorted result without an extra sort.

## Approach 1: Brute Force

Square every element and then sort the resulting array.

- Time Complexity: O(n log n)
- Space Complexity: O(n)
- Implementation: Create a new array of squares, sort it, and return the sorted squares.

See [brute_force_approach.py](brute_force_approach.py) for implementation.

## Approach 2: Optimized

Use two pointers at the start and end of the sorted input.

- Time Complexity: O(n)
- Space Complexity: O(n)
- Implementation:
  - Initialize `left = 0` and `right = n - 1`.
  - Create an output array of the same size.
  - Compare `abs(nums[left])` and `abs(nums[right])`.
  - Place the larger square at the current output position from the end.
  - Move the pointer that produced the larger square.
  - Repeat until all positions are filled.

This produces the result in non-decreasing order without a separate sort.

See [two_pointers_approach.py](two_pointers_approach.py) for implementation.

## Key Learning

- Sorted input enables an O(n) solution even when squaring changes value order.
- Two pointers can be used to compare extremes and build a sorted result from the back.
- When a transformation changes ordering, consider constructing the result in reverse.
- Avoid unnecessary sorting when the input already has useful structure.

## Edge Cases

- Empty array (`[]`)
- Single-element array (`[-1]`, `[0]`, `[5]`)
- All non-negative values (`[1,2,3]`)
- All non-positive values (`[-5,-4,-2]`)
- Mix of negative and positive values
- Large values near integer limits
- Zeros mixed with negative and positive values

## Mistakes to Avoid

- Squaring every value and then sorting the result as the optimal solution.
- Assuming the squared values preserve the original order.
- Filling the output result from the front instead of from the back.
- Comparing values without using absolute value for negative numbers.
- Forgetting to move the correct pointer after placing a square into the output.
