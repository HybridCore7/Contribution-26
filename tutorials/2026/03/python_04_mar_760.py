# Hash Map Implementation in Python

class HashMap:
    def __init__(self, size):
        """
        Initializes the hash map with a given size.
        
        Args:
        size (int): The size of the hash map.
        """
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """
        Calculates the hash value of a given key.
        
        Args:
        key (str): The key to be hashed.
        
        Returns:
        int: The hash value of the key.
        """
        return hash(key) % self.size

    def put(self, key, value):
        """
        Puts a key-value pair into the hash map.
        
        Args:
        key (str): The key to be put.
        value (any): The value to be put.
        """
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                break
        else:
            self.table[index].append((key, value))

    def get(self, key):
        """
        Gets the value of a given key from the hash map.
        
        Args:
        key (str): The key to be retrieved.
        
        Returns:
        any: The value of the key if found, otherwise None.
        """
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        """
        Deletes a key-value pair from the hash map.
        
        Args:
        key (str): The key to be deleted.
        """
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                break

def main():
    # Create a hash map with a size of 10
    hash_map = HashMap(10)

    # Put some key-value pairs into the hash map
    hash_map.put('apple', 5)
    hash_map.put('banana', 7)
    hash_map.put('cherry', 3)

    # Get the values of some keys
    print(hash_map.get('apple'))  # Output: 5
    print(hash_map.get('banana'))  # Output: 7
    print(hash_map.get('cherry'))  # Output: 3

    # Delete a key-value pair
    hash_map.delete('banana')
    print(hash_map.get('banana'))  # Output: None

if __name__ == "__main__":
    main()