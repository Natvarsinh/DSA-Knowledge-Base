# Two Sum Problem

[LeetCode Link](https://leetcode.com/problems/two-sum/description/)

## Problem Statement

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Example Input/Output

**Example 1:**

Input: nums = [2,7,11,15], target = 9

Output: [0,1]

Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

**Example 2:**

Input: nums = [3,2,4], target = 6

Output: [1,2]

**Example 3:**

Input: nums = [3,3], target = 6

Output: [0,1]

## Patterns Used

- Two Pointers Technique (for sorted arrays)
- Hash Map / Dictionary (for unsorted arrays with original indices)

## Clues to Identify Pattern

- **Two Pointers:** Need to find pairs in a sorted array, optimal solution involves moving pointers from opposite ends, avoids nested loops
- **Hash Map:** Need fast lookups for complements, can use extra space for O(n) time, single pass possible, preserves original indices

## Approach 1: Brute Force

Use nested loops to check every possible pair of elements.

- **Time Complexity:** O(n²) - nested loops iterate over all pairs
- **Space Complexity:** O(1) - no extra space used
- **Implementation:** Check sum of every i,j pair where i < j

See [brute_force_approach.py](brute_force_approach.py) for implementation.

## Approach 2: Two Pointers

Sort the array first, then use two pointers starting from both ends.

- **Time Complexity:** O(n log n) for sorting + O(n) for two pointers = O(n log n)
- **Space Complexity:** O(1) if sorting in-place, O(n) if creating copy
- **Implementation:** Move left pointer right if sum < target, right pointer left if sum > target

*Note: This approach assumes the array can be sorted. If original indices are required, use a hash map approach instead.*

See [two_pointers_approach.py](two_pointers_approach.py) for implementation.

## Approach 3: Hash Map

Use a hash map (dictionary) to store elements and their indices as we iterate through the array.

- **Time Complexity:** O(n) - single pass through the array
- **Space Complexity:** O(n) - hash map stores up to n elements
- **Implementation:** For each element, check if target - current exists in hash map, if yes return indices, else add current to hash map

See [hashmap_approach.py](hashmap_approach.py) for implementation.

## Key Learning

- Two pointers technique is powerful for sorted arrays
- Trade-off between time and space: brute force is simple but slow, optimized requires sorting
- Always consider if the array can be modified or if indices matter
- Hash map can provide O(n) time with O(n) space for unsorted arrays

## Edge Cases

- Array with duplicate values (e.g., [3,3], target=6)
- No solution exists (return [-1,-1])
- Array with negative numbers
- Minimum array size (n=2)
- Target is sum of first and last elements

## Mistakes to Avoid

- Using the same element twice (ensure i != j)
- Not handling cases where no solution exists
- Forgetting to sort array before two pointers (if applicable)
- Confusing indices vs values in return statement
- Not considering time/space trade-offs for large arrays