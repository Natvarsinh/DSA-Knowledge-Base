# Sliding Window

## 1. Intuition

Imagine you are looking through a physical window at a long street. You can only see a certain section of the street at one time. To see the next part, you don't go back to the start and walk forward again; you simply `slide` your gaze (the window) one step to the right.

In DSA, the `window` is a sub-segment of your data. Instead of re-calculating everything inside the window from scratch every time it moves, you just subtract what left the window and add what just entered.


## 2. Why it is needed

In many array problems, a naive "Brute Force" approach uses nested loops to check every possible subarray. This often results in a time complexity of $O(N^2)$. The Sliding Window technique allows us to convert those nested loops into a single loop, bringing the complexity down to $O(N)$.


## 3. Pattern Recognition Clues

You should consider Sliding Window when the problem involves:
- **Linear data structures**: Arrays, strings, or linked lists.
- **Subarrays or Substrings**: You are asked to find something contiguous.
- **Optimization or Constraint**: Keywords like `Longest`, `Shortest`, `Maximum`, or `Minimum` given a specific sum or condition.


## 4. Step-by-Step Working

1. **Initialize**: Start two pointers (`left` and `right`) at the beginning of the data.
2. **Expand**: Move the right pointer to add elements to your `window`.
3. **Check**: Does the current window meet the problem's condition?
4. **Shrink**: If the condition is violated (or if it's a fixed size), move the `left` pointer to remove elements until the window is valid again.
5. **Update**: Keep track of the `maximum`/`minimum` result found during the process.


## 5. Variations

There are two main flavors of this technique:
1. **Fixed Window**: The window size $K$ is constant (e.g., "Find the max sum of any subarray of size 3").
2. **Dynamic Window**: The window size grows or shrinks based on a condition (e.g., "Find the smallest subarray with a sum $\ge S$").


## 6. Generic Template (Python)

```python
def sliding_window_template(arr):
    left = 0
    current_state = 0 #Can be sum, frequency map, etc.
    result = 0

    for right in range(len(arr)):
        # 1. Add element at 'right' to state
        current_state += arr[right]

        # 2. Shrink window from 'left' if condition is violated
        while condition_violated(current_state):
            current_state -= arr[left]
            left += 1
        
        # 3. Update result
        result = max(result, right - left + 1)
    return result
```


## 7. Common Mistakes

- **Wrong Window Calculation**: Using `right - left` instead of `right - left + 1` to find the current window size.
- **Premature Updates**: Updating the global result (like `max_length`) before the window has actually reached a `valid` state after shrinking.
- **State Resetting**: Re-initializing or clearing your tracking variables (like a sum or a frequency map) inside the loop, which defeats the purpose of `sliding`.
- **While vs. If**: Using an `if` statement to shrink the window when a `while` loop is necessary to handle cases where multiple elements need to be removed to satisfy the condition.


## 8. Edge Cases

- **Empty Input**: An empty array `[]` or string `""`.
- **K > N**: When the required window size $K$ is larger than the total number of elements $N$.
- **All Unique vs. All Identical**: Inputs like `[1, 1, 1, 1]` or `[1, 2, 3, 4]` often reveal flaws in how the pointers move.
- **No Solution**: Scenarios where no subarray satisfies the condition (e.g., finding a sum of 100 in an array of 1s).


## 9. Time & Space Complexity

- **Time Complexity**: $O(N)$. Even though there is a `while` loop inside a `for` loop, each element is visited by `left` and `right` at most once.
- **Space Complexity**: $O(1)$ (constant) or $O(K)$ if you use a Hash Map to store frequencies of elements in the window.


## 10. Example Problems

Here are example problems that use the Sliding Window technique:

### Fixed Window Problems
- [Maximum Points You Can Obtain from Cards](problems/maximum_cards_points/problem.md) - Collect maximum points by taking cards from both ends using a fixed window approach

### Variable Window Problems
- [Longest Continuous Increasing Subsequence](problems/longest_continuous_increasing_subsequence/problem.md) - Find the length of the longest strictly increasing subarray
- [Longest Mountain in Array](problems/longest_mountain_array/problem.md) - Identify the longest mountain-shaped subarray
- [Maximum Product Subarray](problems/maximum_product_subarray/problem.md) - Find the contiguous subarray with the maximum product
- [Minimum Size Subarray Sum](problems/minimum_size_subarray_sum/problem.md) - Find the minimal length subarray with a sum greater than or equal to a target


## Why is Sliding Window $O(N)$?

It is a common misconception that a `while` loop inside a `for` loop automatically results in $O(N^2)$. In the Sliding Window technique, we use `Amortized Analysis` to understand the true complexity.

1. **The Movement of Pointers**
    
    The algorithm is controlled by two pointers: `left` and `right`.
    - The `right` pointer (the `lead`) moves from the start to the end of the array exactly once.
    - The `left` pointer (the `tail`) only moves forward. It never moves back to a previous position.

2. **The Total Work Done**
    
    Instead of looking at the loops, look at the `elements`:
    - Each element is `visited` by the `right` pointer exactly once.
    - Each element is `discarded` by the `left` pointer at most once.

- Because every element enters and leaves the `window` only one time, the total number of operations is approximately $2N$.

3. **The Caterpillar Analogy**

    Think of a caterpillar moving across a leaf.
   - The head (`right` pointer) stretches forward.
   - The body (`left` pointer) pulls forward to catch up.
   - Even if the body moves several steps at once to `shrink`, it can never travel further than the head has already gone.

- **Complexity Summary**:
    - **Total Moves**: $N$ (right) + $N$ (left) = $2N$
    - **Big O Notation**: $O(2N) \rightarrow \mathbf{O(N)}$


## Comparison Table: Fixed vs. Variable Window

| Feature | Fixed Window | Variable Window |
| ------- | ------------ | --------------- |
| Window Size | Remains constant ($K$) | Changes based on a condition |
| When to Move `left` | Every time `right` moves (after the first $K$ elements) | Only when the condition is met/valid |
| Typical Goal | Max/Min sum of size $K$ | Smallest/Largest window meeting a condition |
| Complexity | $O(N)$ | $O(N)$ |


## Scenarios 

- Identify problems involving contiguous subarrays or substrings where you need to maintain a window of elements and slide it across the array.
- Look for tasks where you need to track a subset of elements within the array that satisfies specific conditions.


## Clue 

Look for problems mentioning subarray sums, cumulative sums, or range sums, and hints that precomputing sums might optimize the solution.