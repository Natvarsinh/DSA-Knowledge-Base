def solve(cardPoints, k):
    total_sum = 0
    n = len (cardPoints)
    
    minimum_excluded = 0
    
    for point in cardPoints:
        total_sum += point
    if k == n:
        return total_sum
    
    window_size = n - k
    for i in range(0, k+1):
        window_sum = 0
        for j in range(i, i+window_size):
            window_sum += cardPoints[j]
        
        minimum_excluded = max(minimum_excluded, total_sum - window_sum)
    
    return minimum_excluded