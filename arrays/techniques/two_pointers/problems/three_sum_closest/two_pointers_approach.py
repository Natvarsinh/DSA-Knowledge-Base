def solve(nums, target):
    """
    Finds the sum of three distinct elements in the array that is closest to the target value.
    
    This function uses an optimized two-pointer approach. The array is sorted first, then for each
    element, two pointers (left and right) are used to find the pair that, combined with the fixed
    element, gives a sum closest to the target. This avoids checking all possible triplets.
    
    Time Complexity: O(n^2) - Sorting takes O(n log n), and the two-pointer traversal is O(n^2).
    Space Complexity: O(1) - Sorting is done in-place, and no additional space is used beyond a few variables.
    """
    n = len(nums)
    
    nums.sort()
    closest_sum = 0
    min_diff = float('inf')
    for idx in range(0, n):
        left = idx +1
        right = n - 1
        
        while left < right:
            current_sum = nums[idx] + nums[left] + nums[right]
            diff = abs(current_sum - target)
            if diff < min_diff:
                min_diff = diff
                closest_sum = current_sum
            
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum
    
    return closest_sum