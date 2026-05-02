def solve(nums):
    n = len(nums)
    global_max = nums[0]
    min_so_far = max_so_far = 1
    
    # if n == 1:
    #     return global_max

    current = 0
    while current < n:
        if nums[current] == 0:
            max_so_far = min_so_far = 0
            global_max = max(global_max, max_so_far)
        elif nums[current] < 0:
            min_so_far, max_so_far = max_so_far, min_so_far
        
        min_so_far *= nums[current]
        max_so_far *= nums[current]
        
        if nums[current] > max_so_far:
            max_so_far = nums[current]
        
        if nums[current] < min_so_far:
            min_so_far = nums[current]
        global_max = max(global_max, max_so_far)
        current += 1
    
    return global_max