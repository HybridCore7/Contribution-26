# Divide and Conquer Algorithm
# This code demonstrates a basic divide and conquer algorithm for finding the maximum element in an unsorted list.

def merge_sort(arr):
    # Base case: If the list has only one element, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Divide the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the two sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    # Initialize an empty list to store the merged result
    merged = []
    
    # Initialize indices for the left and right lists
    left_index = 0
    right_index = 0
    
    # Merge smaller elements first
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Append any remaining elements from the left list
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    
    # Append any remaining elements from the right list
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    
    return merged


# Test the algorithm with a sample list
arr = [12, 11, 13, 5, 6, 7]
print("Original list:", arr)
sorted_arr = merge_sort(arr)
print("Sorted list:", sorted_arr)

# Example with a list of floats
arr_floats = [3.5, 2.1, 1.8, 4.2, 0.9]
print("\nOriginal list:", arr_floats)
sorted_arr_floats = merge_sort(arr_floats)
print("Sorted list:", sorted_arr_floats)