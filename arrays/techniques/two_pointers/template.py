"""
Two Pointers Template
"""

def two_pointer_template(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        current = arr[left] + arr[right]
        
        if current == target:
            return [left, right]
        elif current < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 6]
    print(two_pointer_template(arr, 6))