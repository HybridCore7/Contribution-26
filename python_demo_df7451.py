# Simple Substitution Cipher Tutorial

# Learning Objective:
# This tutorial will teach you how to build a simple substitution cipher
# in Python. A substitution cipher is a method of encryption where each
# letter in the plaintext is replaced by a letter or symbol in the ciphertext,
# according to a fixed system. We will focus on a monoalphabetic substitution
# cipher where each letter of the alphabet is consistently replaced by another.
# You will learn about:
# - Dictionaries for mapping characters
# - String manipulation and iteration
# - Functions for organization and reusability
# - Handling both uppercase and lowercase letters
# - Dealing with non-alphabetic characters

# --- Part 1: Setting up the Cipher Key ---

# A substitution cipher relies on a "key" which defines the mapping
# between the original alphabet and the substituted alphabet.
# For this example, we'll create a simple, arbitrary substitution.
# The order of characters in 'alphabet' must match the order in 'cipher_key'.
alphabet = "abcdefghijklmnopqrstuvwxyz"
cipher_key = "zyxwutsrqponmlkjihgfedcba" # This is a simple reverse alphabet cipher.

# We need to ensure our cipher key is the same length as the alphabet.
# This is a basic validation check.
if len(alphabet) != len(cipher_key):
    raise ValueError("Alphabet and cipher key must be of the same length.")

# To make encryption and decryption efficient, we'll create dictionaries.
# Dictionaries are perfect for mapping one value to another.

# Create an encryption dictionary: maps original letters to cipher letters.
# Example: 'a' maps to 'z', 'b' maps to 'y', and so on.
encryption_map = {}
for i in range(len(alphabet)):
    # For each index 'i', we take the 'i'-th letter from the alphabet
    # and map it to the 'i'-th letter from the cipher_key.
    encryption_map[alphabet[i]] = cipher_key[i]

# Create a decryption dictionary: maps cipher letters back to original letters.
# This is simply the reverse of the encryption map.
decryption_map = {}
for i in range(len(alphabet)):
    # For each index 'i', we take the 'i'-th letter from the cipher_key
    # and map it back to the 'i'-th letter from the alphabet.
    decryption_map[cipher_key[i]] = alphabet[i]

# --- Part 2: The Encryption Function ---

def encrypt_message(message, encryption_map):
    """
    Encrypts a message using the provided substitution cipher map.

    Args:
        message (str): The plaintext message to encrypt.
        encryption_map (dict): A dictionary mapping plaintext characters to ciphertext characters.

    Returns:
        str: The encrypted ciphertext message.
    """
    encrypted_text = "" # Initialize an empty string to build our encrypted message.

    # We iterate through each character in the input message.
    for char in message:
        # We need to handle both uppercase and lowercase letters.
        # First, check if the character is an uppercase letter.
        if 'A' <= char <= 'Z':
            # Convert to lowercase to use our map, then convert back to uppercase.
            # The 'ord()' function gets the ASCII value, and 'chr()' converts it back.
            # 'ord('A')' is 65. 'ord('a')' is 97.
            # We subtract 'A' (or 65) to get an index from 0-25 for our alphabet.
            # Then we look up the substitution using the lowercase version.
            # Finally, we add 'A' back to get the uppercase substituted character.
            lowercase_char = char.lower()
            encrypted_char = encryption_map.get(lowercase_char, lowercase_char) # .get() handles missing keys gracefully
            encrypted_text += encrypted_char.upper()
        # Next, check if the character is a lowercase letter.
        elif 'a' <= char <= 'z':
            # If it's a lowercase letter, we directly look it up in our map.
            # The .get() method is useful here: if the character is NOT in our map
            # (e.g., it's a number or punctuation), it will return the character itself
            # instead of raising an error.
            encrypted_text += encryption_map.get(char, char)
        else:
            # If the character is not a letter (e.g., space, punctuation, numbers),
            # we leave it unchanged. This is important for preserving message structure.
            encrypted_text += char

    return encrypted_text # Return the fully encrypted message.

# --- Part 3: The Decryption Function ---

def decrypt_message(message, decryption_map):
    """
    Decrypts a message using the provided substitution cipher map.

    Args:
        message (str): The ciphertext message to decrypt.
        decryption_map (dict): A dictionary mapping ciphertext characters to plaintext characters.

    Returns:
        str: The decrypted plaintext message.
    """
    decrypted_text = "" # Initialize an empty string for the decrypted message.

    # Similar to encryption, we iterate through each character of the message.
    for char in message:
        # Again, handle uppercase and lowercase.
        if 'A' <= char <= 'Z':
            # Convert to lowercase to use our map, then convert back to uppercase.
            lowercase_char = char.lower()
            decrypted_char = decryption_map.get(lowercase_char, lowercase_char)
            decrypted_text += decrypted_char.upper()
        elif 'a' <= char <= 'z':
            # For lowercase, directly use the decryption map.
            decrypted_text += decryption_map.get(char, char)
        else:
            # Non-alphabetic characters are passed through as is.
            decrypted_text += char

    return decrypted_text # Return the fully decrypted message.

# --- Part 4: Example Usage ---

# Let's test our cipher!
original_message = "Hello, World! This is a secret message 123."

print(f"Original Message: {original_message}")

# Encrypt the message using our pre-defined maps.
encrypted_message = encrypt_message(original_message, encryption_map)
print(f"Encrypted Message: {encrypted_message}")

# Decrypt the message to see if we get the original back.
decrypted_message = decrypt_message(encrypted_message, decryption_map)
print(f"Decrypted Message: {decrypted_message}")

# Let's try with a different message to ensure it works.
another_message = "Python programming is fun."
encrypted_another = encrypt_message(another_message, encryption_map)
decrypted_another = decrypt_message(encrypted_another, decryption_map)

print("\n--- Another Example ---")
print(f"Original: {another_message}")
print(f"Encrypted: {encrypted_another}")
print(f"Decrypted: {decrypted_another}")