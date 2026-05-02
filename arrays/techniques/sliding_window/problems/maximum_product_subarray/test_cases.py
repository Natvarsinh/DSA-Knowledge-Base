from brute_force_approach import solve as bf_approach
from sliding_window import solve as sw_approach

def run_tests():
    test_cases = [
        # Standard cases
        (([2, 3, -2, 4],), 6),          # Your initial case
        (([2, 3, 4],), 24),             # All positives
        
        # Negative number logic
        (([-2, 3, -4],), 24),           # Two negatives (even count)
        (([2, -5, -2, -4, 3],), 24),    # Three negatives (odd count)
        (([-1, -2, -3],), 6),           # All negatives
        
        # The Zero Factor
        (([-2, 0, -1],), 0),            # Zero is the best result
        (([2, 3, 0, 4],), 6),           # Maximum is on one side of the zero
        
        # Boundary & 32-bit constraints
        (([0, 2],), 2),                 # Leading zero
        (([-1],), -1),                  # Single negative element
        (([100000, 20000],), 2000000000), # Large product (close to 32-bit limit)
        (([0], ), 0),
        (([0, 0, 0], ), 0),
    ]
    
    for inputs, expected in test_cases:
        print(f"Brute Force approach: {bf_approach(*inputs)}")
        print(f"Variable Window approach: {sw_approach(*inputs)}")
        print(f"Expected: {expected}")
        print("-"*50)

if __name__ == "__main__":
    run_tests()