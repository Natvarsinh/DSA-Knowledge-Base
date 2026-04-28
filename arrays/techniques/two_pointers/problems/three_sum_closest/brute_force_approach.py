def solve(nums, target):
    """
    Finds the sum of three distinct elements in the array that is closest to the target value.
    
    This function uses a brute force approach by checking all possible triplets in the array.
    The array is first sorted to ensure the triplets are considered in order, though the order
    doesn't affect the closest sum calculation in this implementation.
    
    Time Complexity: O(n^3) - Due to three nested loops iterating over all possible triplets.
    Space Complexity: O(1) - Sorting is done in-place, and no additional space is used beyond a few variables.
    """
    n = len(nums)
    
    nums.sort()
    closest_sum = 0
    min_diff = float('inf')
    
    for i in range(0, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                current_sum = nums[i] + nums[j] + nums[k]
                diff = abs(current_sum - target)
                
                if current_sum == target:
                    return current_sum
                
                if diff < min_diff:
                    min_diff = diff
                    closest_sum = current_sum
    
    return closest_sum