from brute_force_approach import solve as bf_approach
from variable_window import solve as sw_approach

def run_tests():
    test_cases = [
        # 1. Standard case: Multiple increasing parts, middle one is longest
        (([1, 3, 5, 4, 7], ), 3),
        
        # 2. Entirely strictly increasing: Length equals array length
        (([1, 2, 3, 4, 5], ), 5),
        
        # 3. Entirely strictly decreasing: Length should be 1 (each element is its own subsequence)
        (([5, 4, 3, 2, 1], ), 1),
        
        # 4. Array with duplicates: "Strictly increasing" means 2,2 breaks the streak
        (([2, 2, 2, 2, 2], ), 1),
        
        # 5. Sawtooth pattern: Multiple small increasing sequences
        (([1, 3, 2, 4, 3, 5], ), 2),
        
        # 6. Negative numbers and zero: Testing sign changes
        (([-10, -5, 0, 5, 3], ), 4),
        
        # 7. Single element: Minimum possible array
        (([10], ), 1),
        
        # 8. Two elements (increasing):
        (([1, 2], ), 2),
        
        # 9. Two elements (decreasing):
        (([2, 1], ), 1),
        
        # 10. Empty array: 
        (([], ), 0)
    ]
    
    for inputs, expected in test_cases:
        print(f"Brute Force approach: {bf_approach(*inputs)}")
        print(f"Variable Window approach: {sw_approach(*inputs)}")
        print(f"Expected: {expected}")
        print("-"*50)

if __name__ == "__main__":
    run_tests()