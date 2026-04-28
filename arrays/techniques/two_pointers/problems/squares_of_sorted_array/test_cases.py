import copy
from brute_force_approach import solve as bf_approach
from two_pointers_approach import solve as tp_approach

def run_tests():
    test_cases = [
        # 1. Standard Mixed (Negative and Positive)
        (([-4, -1, 0, 3, 10],), [0, 1, 9, 16, 100]),
        
        # 2. All Positives (Order stays the same)
        (([1, 2, 3, 5],), [1, 4, 9, 25]),
        
        # 3. All Negatives (Order reverses)
        (([-5, -3, -2, -1],), [1, 4, 9, 25]),
        
        # 4. All Zeros
        (([0, 0, 0, 0],), [0, 0, 0, 0]),
        
        # 5. Single Element
        (([ -7],), [49]),
        
        # 6. Large Negative vs Small Positive (The "Left" side dominates)
        (([-10, -1, 2, 3],), [1, 4, 9, 100]),
        
        # 7. Array with Duplicates
        (([-2, -2, 1, 2, 2],), [1, 4, 4, 4, 4])
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