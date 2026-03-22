# Merge Sort in Python
=====================================

Merge sort is a divide-and-conquer algorithm that splits the input into two halves, recursively sorts them, and then merges them back together.

```python
def merge_sort(arr):
    # Base case: If the array has one or zero elements, it's already sorted.
    if len(arr) <= 1:
        return arr

    # Find the middle of the array to split it into two halves.
    mid = len(arr) // 2

    # Recursively sort the left and right halves.
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted left and right halves back together.
    return merge(left_half, right_half)


def merge(left, right):
    # Initialize an empty list to store the merged result.
    merged = []

    # Compare elements from both lists and add the smaller one to the merged list.
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    # Add any remaining elements from either list to the merged list.
    merged.extend(left)
    merged.extend(right)

    return merged


# Example usage:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)