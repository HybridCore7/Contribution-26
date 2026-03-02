# Merge Sort Algorithm in Python

# Function to merge two sorted lists
def merge(left, right):
    # Initialize an empty list to store the merged result
    merged = []
    # Initialize two pointers for the left and right lists
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
    # Append any remaining elements from the left or right lists
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

# Function to perform merge sort on a list
def merge_sort(lst):
    # Base case: if the list has 1 or 0 elements, it is already sorted
    if len(lst) <= 1:
        return lst
    # Divide the list into two halves
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]
    # Recursively sort the left and right halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    # Merge the sorted left and right halves
    return merge(left_half, right_half)

# Example usage:
if __name__ == "__main__":
    # Test the merge sort function with a list of numbers
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", numbers)
    print("Sorted list:", merge_sort(numbers))