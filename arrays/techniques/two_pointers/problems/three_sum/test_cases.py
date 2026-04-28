from brute_force_approach import solve as bf_approach
from two_pointers_approach import solve as tp_approach

def run_tests():
    test_cases = [
        # 1. Your original standard case
        (([-1, 0, 1, 2, -1, -4], ), [[-1, -1, 2], [-1, 0, 1]]),
        
        # 2. No triplets sum to zero
        (([1, 2, 3, 4], ), []),
        
        # 3. Multiple zeros (Tests if you handle duplicates and zero logic correctly)
        (([0, 0, 0, 0], ), [[0, 0, 0]]),
        
        # 4. Small array (Should return empty since we need at least 3 numbers)
        (([0, 1], ), []),
        
        # 5. Only one valid triplet exists
        (([-2, 0, 2], ), [[-2, 0, 2]]),
        
        # 6. Duplicates that shouldn't result in duplicate triplets
        (([-2, 0, 0, 2, 2], ), [[-2, 0, 2]])
    ]
    
    for inputs, expected in test_cases:
        print(f"Brute Force approach: {bf_approach(*inputs)}")
        print(f"Two Pointer approach: {tp_approach(*inputs)}")
        print(f"Expected: {expected}")
        print("-"*50)

if __name__ == "__main__":
    run_tests()