def solve(arr):
    n = len(arr)
    longest_mountain = 0
    
    if n < 3:
        return longest_mountain
    
    for start in range(n):
        for end in range(start + 2, n):
            subArray = arr[start: end+1]
            
            peak_idx = -1
            is_mountain = True
            
            i = 1
            while i < len(subArray) and subArray[i] > subArray[i-1]:
                i += 1
                
            if i == 1 or i == len(subArray):
                is_mountain = False
            else:
                peak_idx = i - 1
                while i < len(subArray):
                    if subArray[i] >= subArray[i-1]:
                        is_mountain = False
                        break
                    i += 1
            
            if is_mountain:
                longest_mountain = max(longest_mountain, len(subArray))
    
    return longest_mountain