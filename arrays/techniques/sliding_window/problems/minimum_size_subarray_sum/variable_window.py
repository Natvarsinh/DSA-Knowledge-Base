def solve(nums, target):
    left = 0
    current_sum = 0
    min_length = float("inf")
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        while current_sum >= target:
            window_size = right - left + 1
            min_length = min(min_length, window_size)
            
            if min_length == 1:
                return 1
            
            current_sum -= nums[left]
            left += 1
    
    return min_length if min_length != float("inf") else 0