def solve(nums):
    n = len(nums)
    max_product = nums[0]
    
    for i in range(n):
        max_product = max(max_product, nums[i])
        last_product = nums[i]
        for j in range(i+1, n):
            last_product = last_product * nums[j]
            max_product = max(max_product, last_product)
            
    return max_product
