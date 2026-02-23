def calculate_prefix_sum(arr):
    """
    Calculate the prefix sum of a given array.
    The prefix sum of an array is a new array where each element is the sum of all the elements before it.
    """
    # Initialize an empty list to store the prefix sum
    prefix_sum = [0] * (len(arr) + 1)
    
    # Iterate over the input array
    for i in range(len(arr)):
        # For each element, add the current element to the prefix sum at the current index
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]
    
    # Return the prefix sum list
    return prefix_sum

def calculate_suffix_sum(arr):
    """
    Calculate the suffix sum of a given array.
    The suffix sum of an array is a new array where each element is the sum of all the elements after it.
    """
    # Initialize an empty list to store the suffix sum
    suffix_sum = [0] * (len(arr) + 1)
    
    # Iterate over the input array in reverse
    for i in range(len(arr) - 1, -1, -1):
        # For each element, add the current element to the suffix sum at the current index
        suffix_sum[i] = suffix_sum[i + 1] + arr[i]
    
    # Return the suffix sum list
    return suffix_sum

def calculate_total_sum(arr):
    """
    Calculate the total sum of a given array.
    The total sum of an array is the sum of all its elements.
    """
    # Initialize a variable to store the total sum
    total_sum = 0
    
    # Iterate over the input array
    for num in arr:
        # Add each element to the total sum
        total_sum += num
    
    # Return the total sum
    return total_sum

# Example usage
arr = [1, 2, 3, 4, 5]
prefix_sum = calculate_prefix_sum(arr)
suffix_sum = calculate_suffix_sum(arr)
total_sum = calculate_total_sum(arr)

print("Prefix sum:", prefix_sum)
print("Suffix sum:", suffix_sum)
print("Total sum:", total_sum)