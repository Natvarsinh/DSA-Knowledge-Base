"""
Sliding Window Templates
"""


def fixed_window(arr, k):
    """
    Fixed Window Template
    """
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum += arr[i]
        window_sum -= arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

def variable_window(arr, target):
    left = 0 
    current = 0
    result = 0
    
    for right in range(len(arr)):
        current += arr[right]
        
        while current > target:
            current -= arr[left]
            left += 1
        
        result = max(result, current)
    
    return result