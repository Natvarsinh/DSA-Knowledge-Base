import copy
from brute_force_approach import solve as bf_approach
from two_pointers_approach import solve as tp_approach

def run_tests():
    test_cases = [
        # 1. Standard Case: Mix of unique numbers and duplicates
        (([1, 1, 2, 2, 3, 4, 4],), 4),  # Unique: [1, 2, 3, 4]
        
        # 2. No Duplicates: Array is already unique
        (([1, 2, 3, 4, 5],), 5),        # Unique: [1, 2, 3, 4, 5]
        
        # 3. All Duplicates: Every element is the same
        (([1, 1, 1, 1, 1],), 1),        # Unique: [1]
        
        # 4. Empty Array: Edge case for size zero
        (([],), 0),                     # Unique: None
        
        # 5. Single Element: Minimum size with no duplicates possible
        (([1],), 1),                    # Unique: [1]
        
        # 6. Negative Numbers: Ensuring logic holds for negative integers
        (([-3, -3, -2, 0, 0, 1],), 4)   # Unique: [-3, -2, 0, 1]
    ]
    
    for inputs, expected in test_cases:
        bf_inputs = copy.deepcopy(inputs)
        tp_inputs = copy.deepcopy(inputs)
        print(f"Brute Force approach: {bf_approach(*bf_inputs)}")
        print(f"Two Pointer approach: {tp_approach(*tp_inputs)}")
        print(f"Expected: {expected}")
        print("-"*50)

if __name__ == "__main__":
    run_tests()