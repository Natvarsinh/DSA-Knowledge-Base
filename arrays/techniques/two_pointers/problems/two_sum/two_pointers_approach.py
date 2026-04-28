def solve(arr, target):
    """
    Solves the two-sum problem using a two-pointer approach.
    
    This function finds two indices in the given sorted array such that the elements
    at those indices add up to the target value by moving pointers from both ends.
    
    Time Complexity: O(n) - Single pass through the array with two pointers.
    Space Complexity: O(1) - Uses constant extra space.
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return [left, right]
        elif sum < target:
            left += 1
        else:
            right -= 1
            
    return [-1, -1]