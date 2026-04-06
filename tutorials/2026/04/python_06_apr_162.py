# Sliding Window Technique in Python
=====================================

The sliding window technique is a powerful algorithm used to solve problems that involve finding elements within a larger set of data that meet certain conditions.

```python
def max_sum_subarray(arr, k):
    """
    Returns the maximum sum of a subarray of size k.
    
    Parameters:
    arr (list): The input array.
    k (int): The size of the subarray.
    
    Returns:
    int: The maximum sum of a subarray of size k.
    """
    # Initialize the window boundaries
    left = 0
    right = 0
    
    # Initialize the current sum and the maximum sum found so far
    curr_sum = 0
    max_sum = float('-inf')
    
    # Expand the window to the right
    while right < len(arr):
        # Add the element at the right boundary to the current sum
        curr_sum += arr[right]
        
        # If the window size is greater than k, shrink the left boundary
        if right - left + 1 > k:
            curr_sum -= arr[left]
            left += 1
        
        # Update the maximum sum found so far
        max_sum = max(max_sum, curr_sum)
        
        # Expand the window to the right
        right += 1
    
    return max_sum

# Test the function
arr = [1, 2, 3, 4, 5]
k = 3
print("Maximum sum of subarray of size", k, "is:", max_sum_subarray(arr, k))