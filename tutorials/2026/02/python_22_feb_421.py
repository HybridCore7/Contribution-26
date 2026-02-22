# Trie Data Structure in Python
=====================================================

A Trie, also known as a prefix tree, is a tree-like data structure that is used to store a dynamic set or associative array where the keys are usually strings.

```python
class TrieNode:
    def __init__(self):
        # Initialize the node with an empty dictionary to store children and a boolean to mark the end of a word
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        # Initialize the Trie with a root node
        self.root = TrieNode()

    def insert(self, word):
        # Start at the root node
        node = self.root
        # Iterate over each character in the word
        for char in word:
            # If the character is not in the node's children, add it
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to the child node
            node = node.children[char]
        # Mark the end of the word
        node.is_end_of_word = True

    def search(self, word):
        # Start at the root node
        node = self.root
        # Iterate over each character in the word
        for char in word:
            # If the character is not in the node's children, return False
            if char not in node.children:
                return False
            # Move to the child node
            node = node.children[char]
        # Return whether the word is in the Trie
        return node.is_end_of_word

    def starts_with(self, prefix):
        # Start at the root node
        node = self.root
        # Iterate over each character in the prefix
        for char in prefix:
            # If the character is not in the node's children, return False
            if char not in node.children:
                return False
            # Move to the child node
            node = node.children[char]
        # Return True if we have checked all characters in the prefix
        return True

# Example usage
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("banana")

print(trie.search("apple"))  # Output: True
print(trie.search("app"))    # Output: True
print(trie.search("banana")) # Output: True
print(trie.search("bana"))   # Output: False

print(trie.starts_with("app")) # Output: True
print(trie.starts_with("ban")) # Output: True
print(trie.starts_with("ora")) # Output: False