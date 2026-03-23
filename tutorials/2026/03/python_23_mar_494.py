# Segment Tree Implementation in Python
=====================================

A segment tree is a data structure that can be used to find the minimum or maximum value of an interval within a given array.

```python
class SegmentTree:
    def __init__(self, arr):
        # Calculate the size of the segment tree based on the input array
        n = len(arr)
        self.tree = [0] * (4 * n)
        
        # Build the segment tree recursively
        self._build_tree(arr, 0, 0, n - 1)

    def _build_tree(self, arr, index, start, end):
        # Base case: if the current interval is a single element
        if start == end:
            self.tree[index] = arr[start]
        else:
            # Calculate the mid-point of the current interval
            mid = (start + end) // 2
            
            # Recursively build the left and right subtrees
            self._build_tree(arr, index * 2 + 1, start, mid)
            self._build_tree(arr, index * 2 + 2, mid + 1, end)
            
            # Update the value of the current node in the tree
            self.tree[index] = min(self.tree[index * 2 + 1], self.tree[index * 2 + 2])

    def query(self, start, end):
        # Call the recursive helper function to find the minimum value in the specified interval
        return self._query(0, 0, start, end)

    def _query(self, index, start, end, query_start, query_end):
        # Base case: if the current interval is outside of the query range
        if end < query_start or start > query_end:
            return float('inf')
        
        # If the entire query range fits within the current interval
        if start >= query_start and end <= query_end:
            return self.tree[index]
        
        # Calculate the mid-point of the current interval
        mid = (start + end) // 2
        
        # Recursively search for the minimum value in the left and right subtrees
        return min(self._query(index * 2 + 1, start, mid, query_start, query_end),
                   self._query(index * 2 + 2, mid + 1, end, query_start, query_end))

# Example usage:
arr = [3, 5, 1, 4, 2]
segment_tree = SegmentTree(arr)

print(segment_tree.query(0, 3))  # Output: 1
print(segment_tree.query(2, 4))  # Output: 4