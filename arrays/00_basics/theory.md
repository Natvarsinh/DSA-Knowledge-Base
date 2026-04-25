# Data Structures: Arrays 🧱

## Table of Contents
- [Introduction](#introduction)
- [Static Arrays](#static-arrays)
- [Dynamic Arrays](#dynamic-arrays)
- [Comparison: Static vs. Dynamic Arrays](#comparison-static-vs-dynamic-arrays)
- [Additional Notes](#additional-notes)

## Introduction
Arrays are fundamental linear data structures that store elements of the same type in contiguous memory. This document covers static and dynamic arrays, their mechanics, complexities, and use cases.

## Static Arrays

### 1. Definition
A **static array** is a fixed-size collection of elements stored in contiguous memory locations, accessed via indices.

### 2. Core Concept
The key feature is **index-based access**. Elements are stored sequentially, allowing direct calculation of any element's memory address using the base address and element size.

### 3. Internal Working ⚙️
When declaring an array (e.g., `int arr[5]`), memory allocates a single contiguous block:
- **Base Address**: Location of the first element (index 0).
- **Offset Calculation**: For `arr[i]`, the address is `Base Address + (index * size_of_data_type)`. This enables fast access.

### 4. Time and Space Complexity ⏱️
- **Space Complexity**: $O(n)$, where $n$ is the number of elements.
- **Time Complexity**:
  - Access: $O(1)$
  - Search (linear): $O(n)$
  - Search (binary, if sorted): $O(\log n)$
  - Insertion/Deletion: $O(n)$ (due to element shifting)

### 5. Operations
| Operation    | Complexity | Reason                          |
|--------------|------------|---------------------------------|
| **Access**   | $O(1)$    | Direct index calculation.       |
| **Search**   | $O(n)$    | May require checking all elements. |
| **Insertion**| $O(n)$    | Shift elements to create space. |
| **Deletion** | $O(n)$    | Shift elements to close gaps.   |

### 6. When to Use ✅
- Known element count in advance.
- Frequent index-based access needed.
- Cache-friendly memory locality required.

### 7. When NOT to Use ❌
- Frequent insertions/deletions in the middle or front.
- Highly dynamic sizes.
- Fragmented memory environments.

### 8. Real-World Analogy 🏠
Imagine a street of identical houses:
- Each has a unique address (index).
- Jump directly to any house (index) for $O(1)$ access.
- Inserting a new house mid-street requires moving all subsequent houses ($O(n)$).

## Dynamic Arrays

Dynamic arrays overcome static arrays' fixed-size limitation by resizing at runtime (e.g., `ArrayList` in Java, `vector` in C++, or `lists` in Python).

### 1. The Magic of Resizing
Since memory must be contiguous, a dynamic array can't simply `expand` into the next memory block—that space might already be taken by other data. Instead, it follows a specific growth strategy:
1. **Capacity vs. Size**: The array keeps track of its Size (number of elements currently inside) and its Capacity (the total space currently allocated in memory).
2. **The Threshold**: When you try to add an element but `Size == Capacity`, the array is full.
3. **The Double-and-Copy**: The system allocates a new, larger block of memory (usually double the old size).
4. **Migration**: It copies all existing elements from the old array to the new one.
5. **Cleanup**: It deletes the old, smaller array to free up memory.

See the implementation: [custom_dynamic_array.py](custom_dynamic_array.py)

### 2. Amortized Time Complexity ⏳
- **Append**: Usually $O(1)$, but $O(n)$ during resizes (copying elements).
- Overall, amortized $O(1)$ due to infrequent resizes.

### 3. Trade-offs: Memory vs. Speed ⚖️
Doubling capacity speeds operations but wastes memory (up to 50% unused right after resize).

### 4. Resize Operation Details
| Feature       | Details                          |
|---------------|----------------------------------|
| Trigger       | Size == Capacity on insert.      |
| Growth Factor | Typically 1.5x or 2x (doubling). |
| Complexity    | $O(n)$ per resize, amortized $O(1)$. |
| Mechanism     | Allocate → Copy → Free old space.|

## Comparison: Static vs. Dynamic Arrays

| Feature      | Static Array          | Dynamic Array              |
|--------------|-----------------------|----------------------------|
| Size         | Fixed at creation     | Grows/shrinks at runtime  |
| Memory       | Single pre-allocated block | Re-allocated blocks       |
| Append Time  | N/A (can't exceed size)| Amortized $O(1)$          |
| Wasted Space | Minimal               | Up to 50% after resize    |

## Additional Notes

### Common Mistakes ⚠️
- **Off-by-one errors**: Arrays are 0-indexed; avoid accessing index `n` in an array of size `n`.
- **Memory overflow**: Accessing out-of-bounds indices.
- **Fixed size assumptions**: Attempting to exceed capacity in static arrays.

### Related Patterns 🔄
- Two Pointers
- Merge Intervals
- Sorting
- Sliding Window
- Prefix Sums