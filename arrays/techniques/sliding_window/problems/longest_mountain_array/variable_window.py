def solve(arr):
    n = len(arr)
    longest_mountain = 0
    
    if n < 3:
        return 0
    
    pointer = 1
    while pointer < n - 1:
        # if condition executed when peak found
        if arr[pointer - 1] < arr[pointer] > arr[pointer + 1]:
            # find the left
            left = pointer - 1
            while left > 0 and arr[left -1] < arr[left]:
                left -= 1
                
            # find the right
            right = pointer + 1
            while right < n - 1 and arr[right] > arr[right + 1]:
                right += 1
                
            # calculate mountain length
            mountain_length = right - left + 1
            longest_mountain = max(longest_mountain, mountain_length)
            
            # skip the position that we covered
            pointer = right + 1
        else:
            pointer += 1
    
    return longest_mountain