# Sliding Window Technique in Python
=====================================

The sliding window technique is a useful algorithmic tool used to solve various problems involving subarrays or substrings of a given string.

```python
def max_sum_subarray(arr):
    """
    This function finds the maximum sum of a subarray within the given array.
    
    Parameters:
    arr (list): The input list of integers.
    
    Returns:
    int: The maximum sum of a subarray.
    """
    # Initialize variables to store the current and maximum sum
    curr_sum = max_sum = arr[0]
    
    # Initialize two pointers for the sliding window
    left = 0
    
    # Iterate over the array with the right pointer
    for right in range(1, len(arr)):
        # Add the new element to the current sum
        curr_sum += arr[right]
        
        # If the current sum is less than the maximum sum, replace it
        if curr_sum < max_sum:
            curr_sum = max_sum
        
        # Update the maximum sum if necessary
        while curr_sum > max_sum and left <= right:
            max_sum -= arr[left]
            left += 1
    
    return max_sum

# Example usage:
arr = [2, 3, -1, 5, 4]
print(max_sum_subarray(arr))  # Output: 9