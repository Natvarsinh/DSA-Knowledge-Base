from brute_force_approach import solve as bf_approach
from fixed_window import solve as sw_approach

def run_tests():
    test_cases = [
        # 1. Standard case: Mix of left and right
        (([1, 2, 3, 4, 5, 6, 1], 3), 12),
        
        # 2. Take all cards from the left
        (([10, 20, 30, 1, 1, 1], 3), 60),
        
        # 3. Take all cards from the right
        (([1, 1, 1, 100, 200, 300], 3), 600),
        
        # 4. Corrected: High values near one end
        (([1, 2, 1000, 1000, 3, 4], 3), 1007),
        
        # 5. k equals total cards
        (([1, 7, 2, 3, 4, 5], 6), 22),
        
        # 6. Large values buried too deep (k=3 can't reach the second 1000)
        (([1000, 1, 1, 1000, 1, 1], 3), 1002), 
        
        # 7. Identical values
        (([5, 5, 5, 5, 5], 2), 10),
        
        # 8. Negative points (if allowed by constraints)
        (([-1, -2, 10, -1], 2), 9),
        
        # 9. Smallest possible array
        (([10], 1), 10),
        
        # 10. All cards are high except the very ends
        (([1, 100, 100, 100, 1], 2), 101),
        
        # 11. k is 1 (Choose between the two ends)
        (([5, 10, 15, 20, 8], 1), 8)
    ]
    
    for inputs, expected in test_cases:
        print(inputs)
        print(f"Brute Force approach: {bf_approach(*inputs)}")
        print(f"Fixed Window approach: {sw_approach(*inputs)}")
        print(f"Expected: {expected}")
        print("-"*50)

if __name__ == "__main__":
    run_tests()