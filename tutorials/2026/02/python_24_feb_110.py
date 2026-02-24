# Monotonic Stack Implementation in Python

# A monotonic stack is a data structure that maintains a sequence of elements such that for all x and y in the sequence,
# if x <= y then the element corresponding to x is less than or equal to the element corresponding to y.

class MonotonicStack:
    def __init__(self):
        # Initialize the monotonic stack with an empty list
        self.stack = []

    def push(self, val):
        # If the stack is empty or the new value is greater than the top value, push the value to the top
        if not self.stack or val >= self.stack[-1]:
            self.stack.append(val)
        else:
            # If the new value is less than the top value, find the index where it should be inserted
            idx = self.binary_search(self.stack, val)
            # Insert the value at the correct index
            self.stack.insert(idx, val)

    def pop(self):
        # If the stack is not empty, pop the top value
        if self.stack:
            return self.stack.pop()
        else:
            # If the stack is empty, raise an exception
            raise IndexError("Cannot pop from an empty stack")

    def peek(self):
        # If the stack is not empty, return the top value
        if self.stack:
            return self.stack[-1]
        else:
            # If the stack is empty, raise an exception
            raise IndexError("Cannot peek an empty stack")

    def binary_search(self, arr, val):
        # Perform a binary search to find the correct index
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < val:
                left = mid + 1
            else:
                right = mid - 1
        return left

# Example usage:
if __name__ == "__main__":
    stack = MonotonicStack()
    stack.push(1)
    stack.push(3)
    stack.push(2)
    print(stack.peek())  # Output: 3
    stack.push(5)
    print(stack.peek())  # Output: 5
    stack.push(4)
    print(stack.peek())  # Output: 5
    stack.pop()
    print(stack.peek())  # Output: 4
    stack.pop()
    print(stack.peek())  # Output: 2
    stack.pop()
    print(stack.peek())  # Output: 1
    print(stack.pop())  # Output: 1
    print(stack.pop())  # Output: 2
    try:
        print(stack.pop())  # Raises IndexError
    except IndexError as e:
        print(e)