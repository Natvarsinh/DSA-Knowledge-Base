def solve(nums):
    """
    Remove duplicates from a sorted array in place and return the new length.

    Time Complexity:
    O(n), where n is the length of the input array. The function performs a single pass
    through the array using two pointers.

    Space Complexity:
    O(1), as the function modifies the array in place without using any additional space
    proportional to the input size.
    """
    
    if not nums:
        return 0
    
    left, right = 0, 1
    
    while right < len(nums):
        if nums[left] != nums[right]:
            left += 1
            nums[left] = nums[right]
        right += 1
    
    return left+1