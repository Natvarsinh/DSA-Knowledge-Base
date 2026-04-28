def solve(nums):
    """
    Squares each element in the input list and sorts the list in ascending order.
    
    Time Complexity: O(n log n) - O(n) for squaring elements, O(n log n) for sorting
    Space Complexity: O(1) - modifies the list in place
    """
    for idx in range(0, len(nums)):
        square = nums[idx] * nums[idx]
        nums[idx] = square
    
    nums.sort()
    return nums