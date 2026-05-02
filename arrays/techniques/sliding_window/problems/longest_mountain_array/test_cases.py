from brute_force_approach import solve as bf_approach
from variable_window import solve as sw_approach

def run_tests():
    test_cases = [
        # 1. Standard Case: A clear mountain in the middle
        (([2, 1, 4, 7, 3, 2, 5],), 5), 
        
        # 2. Smallest Possible Mountain: Minimum length of 3
        (([1, 2, 1],), 3),
        
        # 3. No Mountain (Always Increasing): No descent
        (([1, 2, 3, 4, 5],), 0),
        
        # 4. No Mountain (Always Decreasing): No climb
        (([5, 4, 3, 2, 1],), 0),
        
        # 5. Flat Peak: Violates the "strictly" increasing/decreasing rule
        (([1, 2, 2, 1],), 0),
        
        # 6. Multiple Mountains: Testing if it finds the longest one
        (([0, 1, 0, 2, 5, 2, 1, 0],), 6),
        
        # 7. Mountains at the Boundaries: Mountain starts or ends at array edges
        (([2, 3, 2, 0, 0],), 4), # At the start
        (([0, 0, 2, 3, 2],), 4), # At the end
        
        # 8. "Valley" Shape: Down then up (not a mountain)
        (([3, 2, 1, 2, 3],), 0),
        
        # 9. Short Array: Length less than 3 cannot be a mountain
        (([1, 2],), 0),
        
        # 10. All Identical Elements: Completely flat
        (([2, 2, 2, 2],), 0)
    ]
    
    for inputs, expected in test_cases:
        print(f"Brute Force approach: {bf_approach(*inputs)}")
        print(f"Variable Window approach: {sw_approach(*inputs)}")
        print(f"Expected: {expected}")
        print("-"*50)

if __name__ == "__main__":
    run_tests()