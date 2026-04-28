def solve(arr, target):
    """
    Solves the two-sum problem using brute force approach.
    
    This function finds two indices in the given array such that the elements
    at those indices add up to the target value.
    
    Time Complexity: O(n^2) - Due to nested loops iterating over all pairs.
    Space Complexity: O(1) - Uses constant extra space.
    """
    
    n = len(arr)
    for i in range(0, n):
        for j in range(i+1, n):
            sum = arr[i] + arr[j]
            if target == sum:
                return [i, j]
    
    return [-1, -1]