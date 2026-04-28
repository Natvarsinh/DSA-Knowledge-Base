# Two Pointers

## 1. Intuition

Imagine you are trying to find two people in a line who have a specific combined height. Instead of checking every possible pair (which takes a long time), you put one scout at the beginning and one at the end. Depending on whether their combined height is too short or too tall, you move the scouts toward each other.  

By moving pointers strategically, you eliminate many unnecessary comparisons.


## 2. Why this technique is needed

Usually, the alternative to Two Pointers is a Nested Loop (checking every `i` and `j`).
- **Without it**: You might compare every element with every other element, resulting in $O(n^2)$ time.
- **With it**: You often process each element at most once, bringing the time down to $O(n)$. 


## 2.5 Learner's Journey: From Misconceptions to Understanding

Before diving deep into two pointers, many learners (including myself) assume that this technique is primarily used to achieve O(n) time complexity for array problems. However, after practicing various problems, I realized this isn't always the case.

### Initial Assumption
- Two pointers = O(n) time complexity
- Always faster than brute force

### Reality After Practice
Looking at the solved problems:
- [Remove Duplicates](problems/remove_duplicates/problem.md): O(n) - indeed linear time
- [Squares of Sorted Array](problems/squares_of_sorted_array/problem.md): O(n) - linear time
- [Two Sum](problems/two_sum/problem.md): O(n log n) if using two pointers (due to sorting), or O(n) with hashmap
- [Three Sum](problems/three_sum/problem.md): O(n²) - two pointers inside a loop
- [Three Sum Closest](problems/three_sum_closest/problem.md): O(n²) - similar to three sum

The key insight is that two pointers help reduce complexity in specific scenarios, but the overall time depends on the problem structure. For finding pairs, it can be O(n), but for triplets, it becomes O(n²) because you need nested loops.

This technique shines when:
- The array is sorted
- You need to find pairs/triplets with specific conditions
- You want to avoid nested loops where possible

But don't expect it to always give O(n) - sometimes it's O(n²), which is still better than O(n³) brute force.


- The data is sorted (arrays or strings).
- The goal involves finding a pair, a triplet, or a subarray.
- The problem mentions `reversing`, `palindromes` or `removing duplicates`.
- You need to compare elements at different positions simultaneously.


## 4. Step-by-Step Working

1. **Initialize**: Place two pointers (`left` and `right`) at specific starting positions.
2. **Loop**: While the pointers haven't met (or reached the end).
3. **Evaluate**: Check the condition (e.g., `sum == target`).
4. **Move**: Based on the evaluation, decide which pointer to move (increment `left` or decrement `right`).


## 5. Variations

There are two main `flavors` of Two Pointers:
1. **Opposite Ends**: Pointers move toward each other (e.g., Palindromes, Two Sum in a sorted array).
2. **Slow & Fast**: Both move in the same direction but at different speeds (e.g., Detecting a cycle in a linked list).


## 6. Generic Template (Python)

```python
def two_pointers_template(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # 1. Process/Calculate logic
        current_val = arr[left] + arr[right]

        # 2. Decide movement
        if current_val == target:
            return [left, right]
        elif current_val < target:
            left += 1
        else:
            right -= 1
    
    return -1
```


## 7. Common Mistakes

- **Forgetting to Sort**: The `opposite ends` logic usually requires a sorted array to work.
- **Infinite Loops**: Forgetting to update a pointer inside the loop.
- **Off-by-One**: Using `left <= right` when you should use `left < right` (or vice-versa).


## 8. Edge Cases

- Array has only 0 or 1 element.
- All elements are the same.
- The target sum/condition is never met.


## 9. Time & Space Complexity

- **Time**: Usually $O(n)$ because each pointer travels the length of the array once. (Note: If you have to sort first, it becomes $O(n \log n)$).
- **Space**: $O(1)$ because you are only storing two integer variables (the pointers).


## 10. Example Problems

1. **[Remove Duplicates from Sorted Array](problems/remove_duplicates/problem.md)**: Given a sorted array, remove the duplicates in-place such that each element appears only once and returns the new length.
2. **[Squares of a Sorted Array](problems/squares_of_sorted_array/problem.md)**: Given a sorted array, return squares in sorted order using two pointers.
3. **[Two Sum](problems/two_sum/problem.md)**: Find two numbers that sum to target (can use two pointers if sorted).
4. **[Three Sum](problems/three_sum/problem.md)**: Find triplets that sum to zero.
5. **[Three Sum Closest](problems/three_sum_closest/problem.md)**: Find triplet sum closest to target.


## Two Pointers vs. Simple Loops

| Approach | Logic | Complexity |
| -------- | ----- | ---------- |
| Nested Loops | Checks every single possible combination ($i$ and $j$). | $O(n^2)$ |
| Two Pointers | Uses the sorted property to skip impossible pairs. | $O(n)$ |


## Scenarios

- Look for problems where you need to iterate through the array with two pointers, typically starting from different ends or positions within the array.
- Consider tasks that involve comparing or manipulating elements from two different parts of the array simultaneously.


## Clue 

Look for problem descriptions mentioning a sorted array or the need to compare elements from both ends of the array.