# Heap Operations in Python
=====================================

## Overview

This script demonstrates the basic heap operations in Python, including insertion, deletion, and retrieval of elements.

## Code

```python
import heapq

class MinHeap:
    def __init__(self):
        """
        Initializes an empty min-heap.
        """
        self.heap = []

    def insert(self, value):
        """
        Inserts a new element into the heap.

        :param value: The value to be inserted.
        """
        # Create a new tuple with the value and its index
        new_value = (value, 0)
        # Push the tuple onto the heap
        heapq.heappush(self.heap, new_value)

    def delete_min(self):
        """
        Deletes and returns the minimum element from the heap.

        :return: The deleted minimum element.
        :raises IndexError: If the heap is empty.
        """
        # Check if the heap is not empty
        if self.heap:
            min_value = heapq.heappop(self.heap)[0]
            return min_value
        else:
            raise IndexError("Heap is empty")

    def retrieve_min(self):
        """
        Returns the minimum element from the heap without deleting it.

        :return: The minimum element.
        :raises IndexError: If the heap is empty.
        """
        # Check if the heap is not empty
        if self.heap:
            min_value = heapq.heappop(self.heap)[0]
            # Push the tuple back onto the heap to maintain the heap property
            heapq.heappush(self.heap, (min_value, 0))
            return min_value
        else:
            raise IndexError("Heap is empty")

# Example usage:
if __name__ == "__main__":
    min_heap = MinHeap()
    
    # Insert elements into the heap
    min_heap.insert(5)
    min_heap.insert(3)
    min_heap.insert(1)
    min_heap.insert(4)

    print(min_heap.delete_min())  # Output: 1
    print(min_heap.retrieve_min())  # Output: 3
    print(min_heap.delete_min())  # Output: 3