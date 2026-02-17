def merge_sort(arr):
    # Base case: If the array has only one element, it is already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle of the array
    mid = len(arr) // 2

    # Divide the array into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the two sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    # Initialize an empty list to store the merged array
    merged = []

    # Initialize indices for the left and right arrays
    left_index = 0
    right_index = 0

    # Merge the two arrays
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left array
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # Append any remaining elements from the right array
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    # Return the merged array
    return merged


# Test the merge sort function
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)