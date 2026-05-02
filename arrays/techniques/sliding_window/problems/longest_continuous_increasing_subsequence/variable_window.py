def solve(nums):
    n = len(nums)
    if n == 0:
        return 0
    
    max_length = 1
    current_length = 1
    
    for pointer in range(1, n):
        if nums[pointer] > nums[pointer - 1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1
    
    return max_length