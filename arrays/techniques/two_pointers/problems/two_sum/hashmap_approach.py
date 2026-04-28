def solve(arr, target):
    """
    Solves the two-sum problem using a hashmap approach.
    
    This function finds two indices in the given array such that the elements
    at those indices add up to the target value using a dictionary for O(1) lookups.
    
    Time Complexity: O(n) - Single pass through the array with O(1) hashmap operations.
    Space Complexity: O(n) - Uses a hashmap to store elements and their indices.
    """
    hash_map = {}
    for idx, num in enumerate(arr):
        remaining = target - num
        if remaining in hash_map:
            return [hash_map[remaining], idx]
        hash_map[num] = idx
    return [-1, -1]