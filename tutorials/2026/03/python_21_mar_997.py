# Sliding Window Technique in Python
=====================================

The sliding window technique is an optimization method used to find patterns or solutions within a larger dataset by moving a "window" of elements over the data.

```python
def max_sum_subarray(arr, k):
    # Initialize variables to keep track of maximum sum and window start
    max_sum = float('-inf')
    window_start = 0

    # Iterate through the array with the sliding window
    for window_end in range(len(arr)):
        # Calculate the sum of elements within the current window
        window_sum = sum(arr[window_start:window_end + 1])

        # If the window size is greater than k, move the start of the window forward
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            # Update the window start by moving it one step forward
            window_start += 1

    return max_sum


# Example usage
arr = [1, 2, 3, 4, 5]
k = 3
result = max_sum_subarray(arr, k)
print(f"The maximum sum of a subarray of size {k} is: {result}")