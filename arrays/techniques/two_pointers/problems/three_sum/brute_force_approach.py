def solve(nums):
    """
    Solves the three-sum problem using a brute force approach.
    
    This function finds all unique triplets in the given array that sum to zero
    by checking all possible combinations of three elements using three nested loops.
    A set is used to ensure uniqueness of triplets.
    
    Time Complexity: O(n^3) - Three nested loops iterating over all combinations.
    Space Complexity: O(n) - Uses a set to store unique triplets.
    """
    n = len(nums)
    
    if n < 3:
        return []
    
    output = set()
    
    nums.sort()
    
    for i in range(0, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    output.add(tuple(sorted([nums[i], nums[j], nums[k]])))
    
    return [list(triplet) for triplet in output]