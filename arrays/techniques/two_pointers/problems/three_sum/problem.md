# 3 Sum Problem

[LeetCode Link](https://leetcode.com/problems/3sum/description/)

## Problem Statement

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

## Example Input/Output

**Input:** `nums = [-1, 0, 1, 2, -1, -4]`  
**Output:** `[[-1, -1, 2], [-1, 0, 1]]`

**Explanation:**  
- Triplets: `[-1, -1, 2]` sums to 0, `[-1, 0, 1]` sums to 0  
- No duplicates in the output

## Pattern Used

Two Pointers

## Clues to Identify Pattern

- Need to find combinations of 3 elements that sum to a target (0)
- Array can be sorted to handle duplicates and optimize search
- Avoid duplicate triplets in result
- Efficient solution involves fixing one element and finding two others

## Approach 1: Brute Force

Use three nested loops to check all possible triplets. Use a set to store unique triplets.

**Time Complexity:** O(n³)  
**Space Complexity:** O(n) for the set

See [brute_force_approach.py](brute_force_approach.py) for the implementation.

## Approach 2: Optimized (Two Pointers)

Sort the array first. For each element, use two pointers to find the other two that sum to `-nums[i]`. Skip duplicates.

**Time Complexity:** O(n²)  
**Space Complexity:** O(1) excluding output

See [two_pointers_approach.py](two_pointers_approach.py) for the implementation.

## Key Learning

- Sorting the array simplifies duplicate handling and enables two-pointer technique
- Two pointers can efficiently find pairs that sum to a target in a sorted array
- Skipping duplicates requires checking adjacent elements after sorting
- Time complexity improves from O(n³) to O(n²) with optimization

## Edge Cases

- Empty array: Return []
- Array with less than 3 elements: Return []
- All positive numbers: No triplets sum to 0
- All negative numbers: No triplets sum to 0
- Array with duplicates: Ensure no duplicate triplets in output
- Multiple zeros: Handle correctly (e.g., [0,0,0])

## Mistakes to Avoid

- Forgetting to sort the array before using two pointers
- Not skipping duplicate elements in the outer loop
- Not skipping duplicates when moving pointers after finding a triplet
- Using indices instead of values when checking for duplicates (after sorting)
- Not handling the case where the same element is used multiple times
- Time complexity exceeding O(n²) by not optimizing the search