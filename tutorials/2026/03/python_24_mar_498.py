# Binary Search in Python

def binary_search(arr, target):
    """
    Searches for an element in a sorted array using binary search.

    Parameters:
    arr (list): A sorted list of elements.
    target: The element to be searched.

    Returns:
    int: The index of the target element if found, -1 otherwise.
    """

    # Initialize two pointers, one at the start and one at the end of the array
    low = 0
    high = len(arr) - 1

    # Continue the search until the two pointers meet
    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2
        
        # If the target is found at the middle index, return the index
        if arr[mid] == target:
            return mid
        # If the target is less than the middle element, move the high pointer
        elif arr[mid] > target:
            high = mid - 1
        # If the target is greater than the middle element, move the low pointer
        else:
            low = mid + 1

    # If the target is not found, return -1
    return -1


# Example usage
if __name__ == "__main__":
    arr = [2, 4, 6, 8, 10]
    target = 6
    
    index = binary_search(arr, target)
    
    if index != -1:
        print(f"Target {target} found at index {index}")
    else:
        print(f"Target {target} not found in the array")