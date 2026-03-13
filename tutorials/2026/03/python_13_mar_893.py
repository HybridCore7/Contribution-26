# String Hashing Example in Python

# Import the hashlib library for generating hashes
import hashlib

def hash_string(input_string):
    # Create a new SHA-256 hash object
    hash_object = hashlib.sha256()
    
    # Convert the input string to bytes and update the hash object
    hash_object.update(input_string.encode('utf-8'))
    
    # Get the hexadecimal representation of the hash
    hex_hash = hash_object.hexdigest()
    
    return hex_hash

def main():
    # Test the function with a sample string
    input_str = "Hello, World!"
    print(f"Hashing '{input_str}'...")
    
    # Generate and print the hash for the input string
    hash_value = hash_string(input_str)
    print(f"Hash value: {hash_value}")
    
    # Verify by hashing again with same input to get same output
    print(f"Verification: Hash of '{input_str}' again is: {hash_string(input_str)}")
    
# Call the main function
if __name__ == "__main__":
    main()