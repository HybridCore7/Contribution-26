# Hash Map Implementation in Python

class Node:
    # Node class represents a single key-value pair in the hash map
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    # HashMap class represents the hash map data structure
    def __init__(self, size=1000):
        # Initialize the hash map with a given size
        self.size = size
        # Create a list of empty buckets
        self.buckets = [None] * self.size

    def hash_function(self, key):
        # Hash function to map keys to indices in the hash map
        return key % self.size

    def put(self, key, value):
        # Put a key-value pair into the hash map
        index = self.hash_function(key)
        node = self.buckets[index]

        # If the bucket is empty, create a new node
        if node is None:
            self.buckets[index] = Node(key, value)
            return

        # Find the existing node with the same key
        while node is not None:
            if node.key == key:
                node.value = value
                return
            node = node.next

        # If the key is not found, add the new node
        node.next = Node(key, value)

    def get(self, key):
        # Get the value associated with a key
        index = self.hash_function(key)
        node = self.buckets[index]

        # Traverse the linked list to find the key
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next

        # If the key is not found, return None
        return None

    def delete(self, key):
        # Delete a key-value pair from the hash map
        index = self.hash_function(key)
        node = self.buckets[index]

        # Find the existing node with the same key
        prev_node = None
        while node is not None:
            if node.key == key:
                if prev_node is None:
                    self.buckets[index] = node.next
                else:
                    prev_node.next = node.next
                return
            prev_node = node
            node = node.next

    def display(self):
        # Display the contents of the hash map
        for i in range(self.size):
            index = i
            node = self.buckets[index]
            print(f'Bucket {index}:', end=' ')
            while node is not None:
                print(f'({node.key}, {node.value}) -> ', end='')
                node = node.next
            print('None')

# Create a hash map with size 1000
hash_map = HashMap(1000)

# Put some key-value pairs into the hash map
hash_map.put('apple', 1)
hash_map.put('banana', 2)
hash_map.put('orange', 3)

# Display the contents of the hash map
print("Hash Map Contents:")
hash_map.display()

# Get a value from the hash map
print("Value for 'apple':", hash_map.get('apple'))

# Delete a key-value pair from the hash map
hash_map.delete('banana')

# Display the updated contents of the hash map
print("Updated Hash Map Contents:")
hash_map.display()