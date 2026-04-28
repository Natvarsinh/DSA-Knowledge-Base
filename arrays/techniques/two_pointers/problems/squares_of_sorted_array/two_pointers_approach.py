def solve(nums):
    """
    Computes the squares of sorted array elements and returns them in sorted order.
    
    This function uses the two-pointer technique to efficiently solve the problem.
    Since the input array is sorted, the largest squares are at either end of the array.
    Two pointers compare squares from both ends and place the larger one at the end
    of the result array, working backwards.
    
    Args:
        nums (list[int]): A sorted array of integers (can contain negative numbers).
    
    Returns:
        list[int]: A list of squared values in ascending order.
    
    Time Complexity: O(n) - Single pass through the array with two pointers.
    Space Complexity: O(n) - For the result array (excluding output space, O(1)).
    """
    n = len(nums)
    left, right = 0, n - 1
    result = [None] * n
    writingPointer = n - 1
    while left <= right:
        leftSquare = nums[left] * nums[left]
        rightSquare = nums[right] * nums[right]
        if leftSquare >= rightSquare:
            result[writingPointer] = leftSquare
            left += 1
        else:
            result[writingPointer] = rightSquare
            right -= 1
        writingPointer -= 1
        
    return result