from brute_force_approach import solve as bf_approach
from hashmap_approach import solve as hm_approach
from two_pointers_approach import solve as tp_approach

def run_tests():
    test_cases = [
        (([1, 2, 3, 4, 6], 6), [1, 3]),   # Standard case (2 + 4 = 6)
        (([1, 2, 3], 10), [-1, -1]),      # No solution
        (([5, 5], 10), [0, 1]),           # Exact match with duplicates
        (([0, 4, 3, 0], 0), [0, 3]),      # Zeroes as part of the target
        (([-3, 4, 3, 90], 0), [0, 2]),    # Negative numbers (if applicable)
        (([1, 2, 3, 4, 5, 6], 11), [4, 5]) # Pair at the very end
    ]
    
    for inputs, expected in test_cases:
        print(f"Brute Force approach: {bf_approach(*inputs)}")
        print(f"Hash Map approach: {hm_approach(*inputs)}")
        print(f"Two Pointer approach: {tp_approach(*inputs)}")
        print(f"Expected: {expected}")
        print("-"*50)

if __name__ == "__main__":
    run_tests()