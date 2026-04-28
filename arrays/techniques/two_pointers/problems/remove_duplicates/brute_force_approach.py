def solve(nums):
    """
    Remove duplicates from an array in place using a set and return the new length.

    This is a brute force approach that works for both sorted and unsorted arrays,
    but uses extra space for the set.

    Time Complexity:
    O(n), where n is the length of the input array. The loop runs in O(n), and set operations
    (add and lookup) are O(1) on average.

    Space Complexity:
    O(k), where k is the number of unique elements in the array (worst case O(n)).
    This is not optimal for space, as it uses a set to track seen elements.
    """
    
    seen = set()
    
    index = 0
    for idx, num in enumerate(nums):
        if num not in seen:
            seen.add(num)
            nums[index] = num
            
            index += 1
    
    return index