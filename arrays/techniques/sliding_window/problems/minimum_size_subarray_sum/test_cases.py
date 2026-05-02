from brute_force_approach import solve as bf_approach
from variable_window import solve as sw_approach

def run_tests():
    test_cases = [
        # 1. Standard Case: The example we walked through
        (([2, 3, 1, 2, 4, 3], 7), 2),
        
        # 2. No Solution: Total sum is less than target
        (([1, 2, 3], 10), 0),
        
        # 3. Single Element Match: One number is exactly the target
        (([1, 4, 7, 2], 7), 1),
        
        # 4. Entire Array: We need every element to reach the target
        (([1, 1, 1], 3), 3),
        
        # 5. Large Elements: Elements much larger than the target
        (([10, 2, 3], 5), 1),
        
        # 6. Target at the very end: The window slides all the way right
        (([1, 2, 3, 10], 10), 1),
        
        # 7. Multiple identical solutions: Finding the first or last valid one
        (([1, 2, 3, 4, 5], 11), 3), # [2,3,4] is 9 (X), [3,4,5] is 12 (O)
        
        # 8. Empty Array: Handling an empty input
        (([], 7), 0)
    ]
    
    for inputs, expected in test_cases:
        print(f"Brute Force approach: {bf_approach(*inputs)}")
        print(f"Variable Window approach: {sw_approach(*inputs)}")
        print(f"Expected: {expected}")
        print("-"*50)

if __name__ == "__main__":
    run_tests()