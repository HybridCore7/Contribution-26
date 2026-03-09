# Two Pointers Technique
# =======================

# Problem Statement: Find the first duplicate in an array
def first_duplicate(nums):
    # Create a set to store unique elements
    unique_nums = set()
    
    # Iterate through the array with two pointers
    for i in range(len(nums)):
        # Check if the current element is already in the set
        if nums[i] in unique_nums:
            # If it is, return the current index as the first duplicate
            return i
        # If not, add the current element to the set
        unique_nums.add(nums[i])
    
    # If no duplicates are found, return None
    return None


# Example usage:
if __name__ == "__main__":
    # Test case 1: Array with a duplicate
    nums = [2, 1, 3, 5, 3, 2]
    print(first_duplicate(nums))  # Output: 1

    # Test case 2: Array without duplicates
    nums = [1, 2, 3, 4, 5]
    print(first_duplicate(nums))  # Output: None

    # Test case 3: Empty array
    nums = []
    print(first_duplicate(nums))  # Output: None