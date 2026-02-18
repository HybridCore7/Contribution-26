# Divide and Conquer in Python

def merge_sort(arr):
    # Base case: if the array has 1 or fewer elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves back together
    return merge(left_half, right_half)


def merge(left, right):
    # Create a new array to store the merged result
    merged = []
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

    # If there are remaining elements in either half, append them to the merged array
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


# Test the merge sort function
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    print("Sorted array:", merge_sort(arr))