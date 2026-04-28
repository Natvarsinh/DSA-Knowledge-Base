from brute_force_approach import solve as bf_approach
from two_pointers_approach import solve as tp_approach

def run_tests():
    test_cases = [
        # 1. Standard Case: Target is between possible sums
        (([-1, 2, 1, -4], 1), 2),        # (-1 + 1 + 2 = 2) is closest to 1
        
        # 2. Exact Match: The target sum is achievable
        (([1, 1, 1, 0], -100), 2),       # (0 + 1 + 1 = 2) is the smallest possible sum
        
        # 3. Exact Match: The target sum is achievable
        (([0, 2, 1, -3], 1), 0),         # (-3 + 2 + 1 = 0)
        
        # 4. Large Target: Target is much higher than the maximum possible sum
        (([1, 2, 3, 4], 100), 9),        # (2 + 3 + 4 = 9) is the highest possible sum
        
        # 5. Small Target: Target is much lower than the minimum possible sum
        (([1, 2, 3, 4], -100), 6),       # (1 + 2 + 3 = 6) is the lowest possible sum
        
        # 6. Duplicates: Handling repeated numbers correctly
        (([1, 1, 1, 1], 0), 3),          # Only one possible sum: 3
        
        # 7. All Negatives: Ensure pointer logic works with negative sums
        (([-10, -5, -2, -1], -20), -17)  # (-10 + -5 + -2 = -17) is closest to -20
    ]
    
    for inputs, expected in test_cases:
        print(f"Brute Force approach: {bf_approach(*inputs)}")
        print(f"Two Pointer approach: {tp_approach(*inputs)}")
        print(f"Expected: {expected}")
        print("-"*50)

if __name__ == "__main__":
    run_tests()