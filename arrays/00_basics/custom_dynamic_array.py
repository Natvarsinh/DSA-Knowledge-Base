class CustomDynamicArray:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * self.capacity
        
    def resize(self, ):
        self.capacity = self.capacity * 2
        resizedArray = [None] * self.capacity
        for idx, value in enumerate(self.array):
            resizedArray[idx] = value
        
        self.array = resizedArray
    
    def isArrayFull(self, ):
        if self.capacity == self.size:
            return True
        return False
        
    def append(self, value):
        if self.isArrayFull():
            self.resize()
        
        self.array[self.size] = value
        self.size += 1
        
    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index is out of range")
        
        if self.isArrayFull():
            self.resize()
            
        for idx in range(self.size, index, -1):
            self.array[idx] = self.array[idx - 1]
        
        self.array[index] = value
        self.size += 1
        
    def delete(self, index = None):
        if index is None:
            index = self.size - 1
        
        if index < 0 or index >= self.size:
            raise IndexError("Index is out of range")
        
        for idx in range(index, self.size - 1):
            self.array[idx] = self.array[idx + 1]
        
        self.array[self.size] = None
        self.size -= 1
            
    def search(self, target):
        for idx in range(0, self.size):
            if self.array[idx] == target:
                return idx
        return -1
    
    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index is out of range")
        return self.array[index]
    
    def update(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index is out of range")
        
        self.array[index] = value
        
        
def test_dynamic_array():
    print("--- Starting End-to-End Tests ---")
    
    # 1. Initialize with capacity 3 to trigger resize quickly
    da = CustomDynamicArray(capacity=3)
    print(f"Initial State: Size={da.size}, Capacity={da.capacity}")

    # 2. Test Append and Automatic Resize
    print("\nTesting Append & Resize:")
    for val in [10, 20, 30, 40]:  # Adding 4 items to a capacity-3 array
        da.append(val)
    print(f"After 4 appends: Size={da.size}, Capacity={da.capacity}")
    # Expected: Size 4, Capacity 6 (3 * 2)

    # 3. Test Get and Update
    print("\nTesting Access & Update:")
    print(f"Element at index 2: {da.get(2)}") # Expected: 30
    da.update(2, 35)
    print(f"After update at index 2: {da.get(2)}") # Expected: 35

    # 4. Test Insert (Middle and Start)
    print("\nTesting Insertion:")
    da.insert(1, 15) # Insert 15 at index 1
    # Current state should be: [10, 15, 20, 35, 40]
    print(f"After inserting 15 at index 1, index 2 is: {da.get(2)}") # Expected: 20

    # 5. Test Delete (Middle and End)
    print("\nTesting Deletion:")
    da.delete(1) # Remove 15
    print(f"After deleting index 1, index 1 is: {da.get(1)}") # Expected: 20
    da.delete() # Remove last element (40)
    print(f"After deleting end, size is: {da.size}") # Expected: 3

    # 6. Test Search
    print("\nTesting Search:")
    print(f"Index of 35: {da.search(35)}") # Expected: 2
    print(f"Index of 99 (not present): {da.search(99)}") # Expected: -1

    # 7. Test Edge Cases (Error Handling)
    print("\nTesting Error Handling:")
    try:
        da.get(10)
    except IndexError as e:
        print(f"Caught expected error: {e}")

    print("\n--- All tests completed! ---")

# Calling the test function
test_dynamic_array()