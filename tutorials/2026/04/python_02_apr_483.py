# Binary Search in Python

def binary_search(arr, target):
    # Step 1: Define the start and end indices of the array
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        # Step 2: Calculate the middle index
        mid = (low + high) // 2
        
        # Step 3: Compare the target with the middle element
        if arr[mid] == target:
            return mid  # Return the index of the target element
        elif arr[mid] < target:
            low = mid + 1  # Move the start pointer to the right half
        else:
            high = mid - 1  # Move the end pointer to the left half
    
    # Step 4: If the target is not found, return None
    return None

# Example usage
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23
index = binary_search(arr, target)

if index is not None:
    print(f"Target {target} found at index {index}")
else:
    print(f"Target {target} not found in the array")

# Example with duplicate elements
arr = [2, 5, 8, 8, 12, 16, 23, 38, 56, 72, 91]
target = 8
index = binary_search(arr, target)

if index is not None:
    print(f"Target {target} found at index {index}")
else:
    print(f"Target {target} not found in the array")