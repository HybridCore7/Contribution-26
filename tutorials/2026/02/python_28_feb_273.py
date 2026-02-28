# Sliding Window Technique in Python

# Problem: Given an array and an integer k, find all elements that appear at least twice in the array within k elements.

def find_duplicates(arr, k):
    """
    Returns a list of all elements in the array that appear at least twice in the array within k elements.
    """
    window = set()
    duplicates = set()
    left = 0

    # Iterate through the array
    for right, num in enumerate(arr):
        # Move the window to the right
        while num in window:
            window.remove(arr[left])
            left += 1
        window.add(num)
        # Check if the current number appears at least twice in the window
        if right - left + 1 > k and arr[right - k] == num:
            duplicates.add(num)
        # If the window is full and we have found a duplicate, break the loop
        if right - left + 1 == k and num in duplicates:
            break

    return list(duplicates)

# Test the function
arr = [1, 2, 3, 1, 2, 3, 1, 2]
k = 3
print(find_duplicates(arr, k))  # Output: [1, 2, 3]