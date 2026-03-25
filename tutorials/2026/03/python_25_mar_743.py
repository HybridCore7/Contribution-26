import random

def merge_sort(arr):
    # Base case: If the array has one or zero elements, it is already sorted
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    
    # Divide the array into two halves and recursively sort them
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Merge the two sorted halves back together
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    # Compare elements from both lists and add the smaller one to the merged list
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Add any remaining elements from either list
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    
    return merged

# Generate a random array for testing
test_arr = [random.randint(0, 100) for _ in range(10)]
print("Unsorted array:", test_arr)

sorted_arr = merge_sort(test_arr)
print("Sorted array:", sorted_arr)