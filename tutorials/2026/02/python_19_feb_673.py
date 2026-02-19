# Merge Sort Algorithm in Python

# Merge Sort is a divide-and-conquer algorithm that splits an array into two halves,
# recursively sorts each half, and then merges the two sorted halves.

def merge_sort(arr):
    # Base case: If the array has 1 or fewer elements, it's already sorted.
    if len(arr) <= 1:
        return arr

    # Find the middle index to split the array into two halves.
    mid = len(arr) // 2

    # Recursively sort the left and right halves of the array.
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted left and right halves.
    return merge(left_half, right_half)

def merge(left, right):
    # Initialize an empty list to store the merged result.
    merged = []
    left_index = 0
    right_index = 0

    # Compare elements from the left and right arrays and append the smaller one to the merged array.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left or right arrays.
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)