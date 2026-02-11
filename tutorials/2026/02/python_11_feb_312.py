# Prefix Sum

## Introduction

Prefix sum is a technique used in algorithms to improve the time complexity of certain operations. It's particularly useful when performing range queries or updating elements in a sorted array.

## Algorithm

The prefix sum algorithm works by maintaining a separate array where each element represents the cumulative sum of the elements in the original array up to that point. This allows for efficient calculation of the sum of a range of elements in O(1) time.

## Implementation

```python
class PrefixSum:
    def __init__(self, arr):
        self.arr = arr
        self.prefix_sum = [0] * (len(arr) + 1)
        self.prefix_sum[0] = 0

        # Calculate prefix sum
        for i in range(1, len(arr) + 1):
            self.prefix_sum[i] = self.prefix_sum[i-1] + self.arr[i-1]

    def sum_range(self, start, end):
        # Return sum of range [start, end]
        return self.prefix_sum[end] - self.prefix_sum[start-1]

    def update(self, index, value):
        # Update value at index in original array
        self.arr[index] = value

        # Update prefix sum
        for i in range(index, len(self.prefix_sum)):
            self.prefix_sum[i] = self.prefix_sum[i-1] + self.arr[i]

def main():
    # Example usage
    arr = [1, 2, 3, 4, 5]
    ps = PrefixSum(arr)

    # Calculate sum of range [1, 3]
    print(ps.sum_range(1, 3))  # Output: 9

    # Update value at index 3
    ps.update(3, 10)

    # Calculate sum of range [1, 4]
    print(ps.sum_range(1, 4))  # Output: 13

if __name__ == "__main__":
    main()