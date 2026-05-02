def solve(cardPoints, k):
    n = len(cardPoints)
    total_sum = sum(cardPoints)
    
    if k == n:
        return total_sum
    
    left = 0
    maximum_points = 0
    right = n - k
    window_sum = sum(cardPoints[left:right])
        
    maximum_points = max(maximum_points, total_sum - window_sum)
    
    while right < n:
        window_sum -= cardPoints[left]
        window_sum += cardPoints[right]
        right += 1
        left += 1
        maximum_points = max(maximum_points, total_sum - window_sum)
    
    return maximum_points