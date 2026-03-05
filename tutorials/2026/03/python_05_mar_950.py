# Two Pointers Technique in Python
=====================================

The two pointers technique is a common algorithmic approach used to solve various problems, especially those involving arrays or linked lists. In this example, we'll use it to solve the "Remove Duplicates from Sorted Array" problem.

```python
def remove_duplicates(nums):
    # If the input array is empty, return it as it is
    if not nums:
        return nums
    
    # Initialize two pointers, one at the beginning and one at the second element
    i = 0
    j = 1
    
    # Iterate through the array with the second pointer
    while j < len(nums):
        # If the current element is not a duplicate, move it next to the first element
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
        # Move the second pointer forward
        j += 1
    
    # Return the modified array (all duplicates removed)
    return nums[:i+1]

# Example usage
nums = [1, 1, 2, 2, 3, 3, 3, 4, 5]
print(remove_duplicates(nums))  # Output: [1, 2, 3, 4, 5]