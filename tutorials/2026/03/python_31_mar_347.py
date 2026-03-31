# Segment Tree implementation in Python
class SegmentTree:
    def __init__(self, nums):
        """
        Initialize the segment tree with a list of numbers.
        
        Args:
            nums (list): A list of numbers to be used for building the segment tree.
        """
        self.n = len(nums)
        # Calculate the size of the segment tree
        self.size = 1 << (self.n - 1).bit_length()
        # Initialize the leaf nodes with the given numbers
        self.tree = [0] * (2 * self.size)
        for i in range(self.n):
            self.tree[self.size + i] = nums[i]
        # Compute the values for the internal nodes using a bottom-up approach
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def query(self, left, right):
        """
        Query the segment tree for the sum of elements in a given interval.
        
        Args:
            left (int): The left boundary of the interval (inclusive).
            right (int): The right boundary of the interval (exclusive).
        
        Returns:
            int: The sum of elements in the given interval.
        """
        # Initialize the result to zero
        res = 0
        # Initialize the current node index to the root node
        i = self.size + left
        # Iterate from the root node down to a leaf node
        while i > 1:
            # If the right boundary is greater than the current node's right boundary, 
            # then we can ignore this node as it does not affect our result
            if right < i // 2:
                i = (i + 1) // 2
            else:
                # Otherwise, add the value of this node to our result and move on to its left child
                res += self.tree[i]
                i //= 2
        return res

    def update(self, idx, val):
        """
        Update the segment tree with a new value at a given index.
        
        Args:
            idx (int): The index where we want to update the value.
            val (int): The new value for the specified index.
        """
        # Start from the leaf node corresponding to the updated index
        i = self.size + idx
        # Update the values of the nodes along the path from the leaf node up to the root node
        while i > 1:
            if idx < i // 2:
                self.tree[i] = val
            else:
                # The left child's value is the sum of its own value and its right child's value
                self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
            # Move up to the parent node
            i //= 2

# Example usage:
if __name__ == "__main__":
    # Create a list of numbers
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    # Build the segment tree
    st = SegmentTree(nums)
    # Print the sum of elements in the first three intervals
    print(st.query(0, 2))  # Output: 5