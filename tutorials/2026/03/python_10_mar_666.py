# Two Pointers Technique
# This technique is used to solve problems that involve sorting, searching, or manipulating elements in a list or array.

def two_pointers(arr):
    # Step 1: Initialize two pointers, one at the start and one at the end of the list
    i = 0
    j = len(arr) - 1

    # Step 2: Continue the process until the two pointers meet
    while i < j:
        # Step 3: If the elements at the two pointers are not equal, swap them
        if arr[i] != arr[j]:
            # Step 4: Swap the elements
            arr[i], arr[j] = arr[j], arr[i]
            # Step 5: Move the pointer that points to the smaller element one step forward
            if arr[i] < arr[j]:
                i += 1
            else:
                j -= 1
        else:
            # Step 6: If the elements at the two pointers are equal, move both pointers one step forward
            i += 1
            j -= 1

def print_array(arr):
    # Step 7: Print the sorted array
    print("Sorted array:", arr)

# Example usage
arr = [5, 2, 8, 1, 9, 3, 7, 6, 4]
print("Original array:", arr)
two_pointers(arr)
print_array(arr)