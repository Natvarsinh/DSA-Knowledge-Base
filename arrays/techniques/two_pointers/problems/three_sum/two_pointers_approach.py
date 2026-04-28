def solve(nums):
    """
    Solves the three-sum problem using a two-pointer approach.
    
    This function finds all unique triplets in the given array that sum to zero.
    The array is first sorted, then for each element, two pointers are used to find
    pairs that sum to the negative of that element.
    
    Time Complexity: O(n^2) - Sorting takes O(n log n), two-pointer search is O(n^2).
    Space Complexity: O(1) - Uses constant extra space (excluding output space).
    """
    n = len(nums)
    if n < 3:
        return []
    
    nums.sort()
    
    
    output = []
    for idx, num in enumerate(nums):
        start = idx + 1
        end = n - 1
        if idx > 0 and num == nums[idx - 1]:
            continue
        
        while start < end:
            total = num + nums[start] + nums[end]
            if total == 0:
                output.append([num, nums[start], nums[end]])
                start += 1
                end -= 1
                
                while start < end and nums[start] == nums[start - 1]:
                    start += 1
                while start < end and nums[end] == nums[end + 1]:
                    end -= 1
            elif total < 0:
                start += 1
            else:
                end -= 1
    return output