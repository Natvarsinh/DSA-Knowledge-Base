def solve(nums, target):
    n = len(nums)
    min_length = float("inf")
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum >= target:
                window_length = j - i + 1
                min_length = min(min_length, window_length)
                break
    
    return min_length if min_length != float("inf") else 0