# Import the built-in HashMap class from the collections module
from collections import HashMap

# Define a function to create a new HashMap
def create_hash_map():
    # Create an empty HashMap
    hash_map = HashMap()
    
    # Add some key-value pairs to the HashMap
    hash_map['one'] = 1
    hash_map['two'] = 2
    hash_map['three'] = 3
    
    # Define a function to get the value for a given key
    def get_value(key):
        return hash_map.get(key)
    
    # Define a function to update the value for a given key
    def update_value(key, new_value):
        if key in hash_map:
            hash_map[key] = new_value
        else:
            raise KeyError(f'Key {key} not found')
    
    # Define a function to delete a key-value pair from the HashMap
    def delete_key(key):
        if key in hash_map:
            del hash_map[key]
        else:
            raise KeyError(f'Key {key} not found')
    
    return {
        'get_value': get_value,
        'update_value': update_value,
        'delete_key': delete_key,
        'hash_map': hash_map
    }

# Create a new HashMap and store it in the 'hash_map' variable
hash_map = create_hash_map()

# Test the HashMap by getting the value for key 'one'
print(hash_map['get_value']['one'])  # Output: 1

# Update the value for key 'two'
hash_map['update_value']['two'] = 10
print(hash_map['update_value']['two'])  # Output: 10

# Delete the key-value pair for key 'three'
hash_map['delete_key']['three']

try:
    print(hash_map['get_value']['three'])
except KeyError as e:
    print(e)  # Output: Key three not found