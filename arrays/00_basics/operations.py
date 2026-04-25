"""
Array Basic Operations
"""

def traverse(arr):
    print("Traversing Array:")
    for i in range(len(arr)):
        print(f"Index {i}: {arr[i]}")
        
def search(arr, target):
    for idx, value in enumerate(arr):
        if target == value:
            return idx
    return -1

def insert(arr, index, value):
    if index < 0 or index > (len(arr) - 1):
        return arr

    return arr[:index] + [value] + arr[index:]

def delete(arr, index):
    if index < 0 or index > (len(arr) - 1):
        return arr
    
    return arr[:index] + arr[index+1:]

def update(arr, index, value):
    if index < 0 or index > (len(arr) - 1):
        return arr
    
    arr[index] = value

    return arr

def run_tests():
    arr = [1, 2, 3, 4]

    traverse(arr)

    print("Search 3:", search(arr, 3))

    print("Insert 99 at index 2:", insert(arr, 2, 99))

    print("Delete index 1:", delete(arr, 1))

    print("Update index 0:", update(arr, 0, 100))
    
if __name__ == "__main__":
    run_tests()