# Two Pointers Exercise
## Problem Description

This exercise focuses on the concept of using two pointers in Python to solve problems efficiently.

```python
def two_sum(nums, target):
    """
    This function takes a list of numbers and a target number as input.
    It returns a tuple containing the indices of two numbers that add up to the target.

    :param nums: A list of integers.
    :type nums: List[int]
    :param target: The target sum.
    :type target: int
    :return: A tuple containing the indices of two numbers that add up to the target.
    :rtype: Tuple[int, int]
    """
    
    # Create a dictionary to store the numbers we have seen so far and their indices
    num_dict = {}
    
    # Iterate over the list of numbers with their indices
    for i, num in enumerate(nums):
        
        # Calculate the complement of the current number
        complement = target - num
        
        # Check if the complement is already in our dictionary
        if complement in num_dict:
            
            # If it is, return its index and the current index
            return (num_dict[complement], i)
        
        # If not, add the current number and its index to our dictionary
        num_dict[num] = i
    
    # If we have iterated over the entire list and haven't found a solution, return None
    return None

# Test the function
print(two_sum([2, 7, 11, 15], 9))  # Output: (0, 1)
print(two_sum([3, 2, 4], 6))  # Output: (1, 2)
print(two_sum([3, 3], 6))  # Output: (0, 1)