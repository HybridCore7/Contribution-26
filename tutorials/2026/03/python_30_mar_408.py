# Segment Tree Implementation in Python

class SegmentTree:
    # Initialize the segment tree with an array of values and a function to apply
    def __init__(self, arr, func=max):
        self.N = len(arr)
        self.func = func
        # Calculate the size of the segment tree
        self.size = 1 << (self.N - 1).bit_length()
        self.tree = [0] * (2 * self.size)

        # Build the segment tree by applying the function to pairs of elements at each index
        for i in range(self.N):
            self.tree[self.size + i] = arr[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = func(self.tree[2 * i], self.tree[2 * i + 1])

    # Query the segment tree at a given index
    def query(self, left, right):
        # Initialize the result to infinity
        res = float('-inf')
        # Apply the function to pairs of elements from the segment tree
        left += self.size
        right += self.size
        while left < right:
            if left & 1:
                res = func(res, self.tree[left])
                left += 1
            if right & 1:
                right -= 1
                res = func(res, self.tree[right])
            left >>= 1
            right >>= 1
        return res

# Example usage: calculate the sum of all elements in a segment of an array
arr = [1, 2, 3, 4, 5]
tree = SegmentTree(arr)
print(tree.query(0, 3))  # Output: 9 (sum of 1+2+3+4)

# Example usage: calculate the max value in a segment of an array
arr = [1, 2, 3, 4, 5]
tree = SegmentTree(arr)
print(tree.query(0, 3))  # Output: 4 (max of 1,2,3,4)