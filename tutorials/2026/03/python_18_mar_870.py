# Divide and Conquer in Python
# A simple implementation of merge sort using divide and conquer technique

def merge_sort(arr):
    # Base case: If the array has one or zero elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Find the middle point and split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively call merge_sort on both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves back into a single array
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    # Compare elements from both arrays and add the smaller one to the merged array
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Add any remaining elements from either array to the merged array
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged

# Test the merge_sort function with an example array
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original Array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted Array:", sorted_arr)