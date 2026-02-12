# Monotonic Stack Implementation in Python

# Define a class to implement the monotonic stack
class MonotonicStack:
    # Initialize the stack with an empty list
    def __init__(self):
        self.stack = []

    # Push an element onto the stack
    def push(self, x):
        # While the stack is not empty and the top element is less than the new element
        while self.stack and self.stack[-1] < x:
            # Pop the top element from the stack
            self.stack.pop()
        # Add the new element to the top of the stack
        self.stack.append(x)

    # Pop an element from the stack
    def pop(self):
        # If the stack is not empty
        if self.stack:
            # Remove and return the top element from the stack
            return self.stack.pop()
        # If the stack is empty, raise an IndexError
        else:
            raise IndexError("Cannot pop from an empty stack")

    # Get the top element of the stack without removing it
    def top(self):
        # If the stack is not empty
        if self.stack:
            # Return the top element of the stack
            return self.stack[-1]
        # If the stack is empty, raise an IndexError
        else:
            raise IndexError("Cannot get top from an empty stack")

    # Check if the stack is empty
    def is_empty(self):
        # Return True if the stack is empty, False otherwise
        return len(self.stack) == 0

    # Check if the stack is not empty
    def is_not_empty(self):
        # Return True if the stack is not empty, False otherwise
        return len(self.stack) > 0

    # Print the stack
    def print_stack(self):
        # Print each element in the stack
        print(self.stack)


# Example usage
if __name__ == "__main__":
    # Create a new monotonic stack
    stack = MonotonicStack()

    # Push some elements onto the stack
    stack.push(5)
    stack.push(10)
    stack.push(3)
    stack.push(8)
    stack.push(4)

    # Print the stack
    print("Stack:", end=" ")
    stack.print_stack()

    # Get the top element
    print("Top element:", stack.top())

    # Pop an element
    print("Popped element:", stack.pop())

    # Print the stack
    print("Stack after pop:", end=" ")
    stack.print_stack()

    # Check if the stack is empty
    print("Is stack empty?", stack.is_empty())

    # Pop another element
    print("Popped element:", stack.pop())

    # Check if the stack is empty
    print("Is stack empty?", stack.is_empty())