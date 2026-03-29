# Prefix Sum Tutorial

def calculate_prefix_sum(arr):
    """
    Calculate the prefix sum of an array.

    Args:
        arr (list): The input array.

    Returns:
        list: A new array where each element is the sum of all elements up to that index.
    """
    # Initialize a new array with the same length as the input array, filled with zeros
    prefix_sum_arr = [0] * len(arr)
    
    # Iterate over the input array from left to right
    for i in range(len(arr)):
        # For each element in the current position, add its value to the corresponding prefix sum
        prefix_sum_arr[i] += arr[i]
        
    return prefix_sum_arr

def main():
    # Create a sample input array
    arr = [1, 2, 3, 4, 5]
    
    # Print the original array
    print("Original Array:", arr)
    
    # Calculate and print the prefix sum array
    prefix_sum_arr = calculate_prefix_sum(arr)
    print("Prefix Sum Array:", prefix_sum_arr)

def test_example():
    """
    Test example to demonstrate the functionality of the prefix sum calculation.
    """
    # Create a sample input array with different values
    arr = [1, 3, -2, -4, 5]
    
    # Calculate and print the prefix sum array
    prefix_sum_arr = calculate_prefix_sum(arr)
    print("Prefix Sum Array:", prefix_sum_arr)

if __name__ == "__main__":
    main()