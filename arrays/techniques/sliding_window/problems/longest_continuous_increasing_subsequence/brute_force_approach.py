def solve(nums):
    n = len(nums)
    if n == 0:
        return 0
    
    max_length = 1
    for i in range(n):
        current = 1
        for j in range(i+1, n):
            if nums[j] > nums[j - 1]:
                current += 1
            else:
                break
        max_length = max(max_length, current)
    return max_length