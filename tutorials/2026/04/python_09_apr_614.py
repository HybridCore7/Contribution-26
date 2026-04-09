# Monotonic Stack Implementation in Python
=============================================

A monotonic stack is a data structure that always maintains either monotonically increasing or decreasing order of elements.

```python
class MonotonicStack:
    def __init__(self):
        """
        Initialize an empty monotonic stack.
        """
        self.stack = []

    def push(self, x):
        """
        Push an element onto the stack if it's not already present and maintains monotonically increasing order.
        """
        # Check if the stack is empty or x is greater than the top of the stack
        while self.stack and x <= self.stack[-1]:
            # Remove elements from the stack until we find a valid position for x
            self.stack.pop()
        # Push x onto the stack
        self.stack.append(x)

    def pop(self):
        """
        Pop an element from the stack if it's not empty.
        """
        # Check if the stack is not empty
        if self.stack:
            # Remove and return the top element of the stack
            return self.stack.pop()
        else:
            # Raise an error if the stack is empty
            raise IndexError("Cannot pop from an empty stack")

    def peek(self):
        """
        Return the top element of the stack without removing it.
        """
        # Check if the stack is not empty
        if self.stack:
            # Return the top element of the stack
            return self.stack[-1]
        else:
            # Raise an error if the stack is empty
            raise IndexError("Cannot peek into an empty stack")

    def isEmpty(self):
        """
        Check if the stack is empty.
        """
        # Check if the stack is empty
        return len(self.stack) == 0

# Example usage:
if __name__ == "__main__":
    monotonic_stack = MonotonicStack()
    print(monotonic_stack.isEmpty())  # Output: True

    # Push elements onto the stack
    for i in range(5):
        monotonic_stack.push(i)
    print("Stack:", monotonic_stack.stack)  # Output: [0, 1, 2, 3, 4]

    # Pop elements from the stack
    while not monotonic_stack.isEmpty():
        print(monotonic_stack.pop())  # Output: 4, 3, 2, 1, 0

    print("Stack:", monotonic_stack.stack)  # Output: []